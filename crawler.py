from bs4 import BeautifulSoup
import pandas as pd
import itertools
import requests
import config
import utils

# Load the URL list from the config file
url_list = config.url_list

# Initialize an empty list to hold company info
company_info = []

# Loop through each URL in the list, fix the range before running
for base_url, page in itertools.product(url_list, range(17)):
    url = f"{base_url}{page}"

    # Send a request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all company entries on the current page
    companies = soup.find_all('div', class_='w-100 h-auto shadow rounded-3 bg-white p-2 mb-3')

    # Loop through each company in url_list and extract details
    for company in companies:
        # Extract company name
        name = company.find('h2', class_="p-1 fs-5 h2 m-0 pt-0 ps-0 text-capitalize").get_text(strip=True) # type: ignore

        # Extract address
        if address_div := company.find('div', class_='logo_congty_diachi'): # type: ignore
            address = address_div.find_all('div')[1].get_text(strip=True) if len(address_div.find_all('div')) > 1 else '' # type: ignore
        elif address_div := company.find('div', class_='listing_diachi_nologo'): # type: ignore
            address = address_div.find_all('div')[1].get_text(strip=True) if len(address_div.find_all('div')) > 1 else '' # type: ignore

        # Extract phone number
        if phone_div := company.find('div', class_='listing_dienthoai'): # type: ignore
            phone = phone_div.find('a').get_text(strip=True) if phone_div.find('a') else '' # type: ignore
        elif phone_div := company.find('div', class_='p-2 pt-0 ps-0 pe-4 pb-0'): # type: ignore
            phone = phone_div.find('a').get_text(strip=True) if phone_div.find('a') else '' # type: ignore

        # Extract email and website
        email_section = company.find('div', class_='email_web_section') # type: ignore
        email = ''
        website = ''

        if email_section:
            if email_link := email_section.find('a', href=lambda href: href and 'mailto:' in href): # type: ignore
                email = email_link['href'].replace('mailto:', '').strip() # type: ignore

            if website_link := email_section.find( # type: ignore
                'a', href=lambda href: href and 'http' in href # type: ignore
            ) or company.find('a', href=lambda href: href and 'http' in href): # type: ignore
                website = website_link.get_text(strip=True)

        # Extract company link
        company_link = company.find('a', href=True)['href'] # type: ignore
        print(f'Getting data from {company_link}')

        # Visit the company's detailed page
        company_response = requests.get(company_link) # type: ignore
        company_soup = BeautifulSoup(company_response.content, 'html.parser')

        # Extract contact information from the detailed page
        contact_info = company_soup.find('div', class_='w-100 rounded-3 bg-white p-3 pt-4 mb-3 border-bottom')
        customer_name = None
        position = None
        customer_phone_number = None

        if contact_info:
            if customer_name_tag := contact_info.find('small', class_='red_color fw500'): # type: ignore
                customer_name = customer_name_tag.get_text(strip=True)
            if position_tag := contact_info.find('span', string='Chức vụ:'): # type: ignore
                position = position_tag.find_next('small').get_text(strip=True) # type: ignore
            if phone_tag := contact_info.find('span', string='Di động:'): # type: ignore
                customer_phone_number = phone_tag.find_next('small').get_text(strip=True) # type: ignore

        # Extract specialisation from the base URL
        specialisation = utils.extract_specialisation(base_url)

        # Append the extracted info to the list
        company_info.append({
            'Company Name': name,
            'Website': website,
            'Address': address,
            'Phone Number': phone,
            'Customer Name': customer_name,
            'Position': position,
            'Customer Phone Number': customer_phone_number,
            'Email Address': email,
            'Specialise': specialisation
        })

# Create a DataFrame from the list 
df = pd.DataFrame(company_info)

# Remove duplicate rows
df = df.drop_duplicates()

# Save the DataFrame to a CSV file
df.to_csv('company_info_cnh.csv', index=False, encoding='utf-8-sig')
print("Done.")

# url_list = config.url_list
# company_info = utils.scrape_companies(url_list)
# utils.save_to_csv(company_info, 'company_info1.csv')
# print("Done.")
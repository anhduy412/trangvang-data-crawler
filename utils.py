from bs4 import BeautifulSoup
import pandas as pd
import itertools
import requests

# Extract specialisation from the URL
# def extract_specialisation(url):
#     specialisation = url.split('cateprovinces/')[1].split('/')[1].split('-ở-tại')[0]
#     specialisation = requests.utils.unquote(specialisation) # type: ignore
#     specialisation = specialisation.replace('-', ' ')
#     return specialisation

# Function to fetch the content of a page
# def fetch_page_content(url):
#     response = requests.get(url)
#     return BeautifulSoup(response.content, 'html.parser')

# def extract_contact_info(company_soup):
#     contact_info = company_soup.find('div', class_='w-100 rounded-3 bg-white p-3 pt-4 mb-3 border-bottom')
#     customer_name = None
#     position = None
#     customer_phone_number = None

#     if contact_info:
#         if customer_name_tag := contact_info.find('small', class_='red_color fw500'):  # type: ignore
#             customer_name = customer_name_tag.get_text(strip=True)
#         if position_tag := contact_info.find('span', string='Chức vụ:'):  # type: ignore
#             position = position_tag.find_next('small').get_text(strip=True)  # type: ignore
#         if phone_tag := contact_info.find('span', string='Di động:'):  # type: ignore
#             customer_phone_number = phone_tag.find_next('small').get_text(strip=True)  # type: ignore
#     return customer_name, position, customer_phone_number

# Extract details of a single company
def extract_company_details(company, base_url):
    # Extract company name
    # name = company.find('h2', class_="p-1 fs-5 h2 m-0 pt-0 ps-0 text-capitalize").get_text(strip=True)  # type: ignore

    # Extract address
    # address = ''
    # if address_div := company.find('div', class_='logo_congty_diachi'):  # type: ignore
    #     address = address_div.find_all('div')[1].get_text(strip=True) if len(address_div.find_all('div')) > 1 else ''  # type: ignore
    # elif address_div := company.find('div', class_='listing_diachi_nologo'):  # type: ignore
    #     address = address_div.find_all('div')[1].get_text(strip=True) if len(address_div.find_all('div')) > 1 else ''  # type: ignore

    # Extract phone number
    # phone = ''
    # if phone_div := company.find('div', class_='listing_dienthoai'): # type: ignore
    #     phone = phone_div.find('a').get_text(strip=True) if phone_div.find('a') else ''  # type: ignore
    # elif phone_div := company.find('div', class_='p-2 pt-0 ps-0 pe-4 pb-0'):  # type: ignore
    #     phone = phone_div.find('a').get_text(strip=True) if phone_div.find('a') else ''  # type: ignore

    # Extract email and website
    email, website = extract_email_and_website(company)

    # Extract company link
    company_link = company.find('a', href=True)['href'] # type: ignore
    print(f'Getting data from {company_link}')

    # Visit the company's detailed page
    company_soup = fetch_page_content(company_link)

    # Extract contact information from the detailed page
    customer_name, position, customer_phone_number = extract_contact_info(company_soup)

    # Extract specialisation from the base URL
    specialisation = extract_specialisation(base_url)
    return {
        'Company Name': name,
        'Website': website,
        'Address': address,
        'Phone Number': phone,
        'Customer Name': customer_name,
        'Position': position,
        'Customer Phone Number': customer_phone_number,
        'Email Address': email,
        'Specialise': specialisation
    }

# Extract email and website from a company entry
# def extract_email_and_website(company):
#     email = ''
#     website = ''
#     email_section = company.find('div', class_='email_web_section') # type: ignore
#     if email_section:
#         if email_link := email_section.find('a', href=lambda href: href and 'mailto:' in href): # type: ignore
#             email = email_link['href'].replace('mailto:', '').strip() # type: ignore
#         if website_link := email_section.find('a', href=lambda href: href and 'http' in href) or company.find('a', href=lambda href: href and 'http' in href): # type: ignore
#             website = website_link.get_text(strip=True)
#     return email, website

# Function to extract contact information from the company's detailed page

# Scrape company information from the given URL list.
def scrape_companies(url_list):
    company_info = []
    for base_url, page in itertools.product(url_list, range(17)):
        url = f"{base_url}{page}"
        soup = fetch_page_content(url)

        # Find all company entries on the current page
        companies = soup.find_all('div', class_='w-100 h-auto shadow rounded-3 bg-white p-2 mb-3')

        # Extract details for each company
        for company in companies:
            company_details = extract_company_details(company, base_url)
            company_info.append(company_details)
    return company_info

# Save the scraped data to a CSV file
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df = df.drop_duplicates()
    df.to_csv(filename, index=False, encoding='utf-8-sig')
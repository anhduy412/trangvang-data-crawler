import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL of the website
base_url = "https://trangvangvietnam.com/cateprovinces/68660/v%E1%BA%ADn-t%E1%BA%A3i-container-%E1%BB%9F-t%E1%BA%A1i-tp.-h%E1%BB%93-ch%C3%AD-minh-(tphcm).html?page="

# Initialize an empty list to hold company info
company_info = []

# Loop through each page
for page in range(1, 3):  # Adjust the range based on the number of pages you want to crawl
    # Construct the full URL for the current page
    url = f"{base_url}{page}"

    # Send a request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all company entries on the current page
    companies = soup.find_all('div', class_='w-100 h-auto shadow rounded-3 bg-white p-2 mb-3')

    # Loop through each company entry and extract details
    for company in companies:
        name = company.find('h2', class_="p-1 fs-5 h2 m-0 pt-0 ps-0 text-capitalize").get_text(strip=True)

        if address_div := company.find('div', class_='logo_congty_diachi'):
            address = address_div.find_all('div')[1].get_text(strip=True) if len(address_div.find_all('div')) > 1 else ''
        elif address_div := company.find('div', class_='listing_diachi_nologo'):
            address = address_div.find_all('div')[1].get_text(strip=True) if len(address_div.find_all('div')) > 1 else ''
        else:
            address = ''

        if phone_div := company.find('div', class_='listing_dienthoai'):
            phone = phone_div.find('a').get_text(strip=True) if phone_div.find('a') else ''
        elif phone_div := company.find('div', class_='p-2 pt-0 ps-0 pe-4 pb-0'):
            phone = phone_div.find('a').get_text(strip=True) if phone_div.find('a') else ''
        else:
            phone = ''

        email_section = company.find('div', class_='email_web_section')

        # Initialize email and website to ''
        email = ''
        website = ''

        # Check if email_section is found
        if email_section:
            if email_link := email_section.find('a', href=lambda href: href and 'mailto:' in href):
                email = email_link['href'].replace('mailto:', '').strip()
            if website_link := email_section.find('a', href=lambda href: href and 'http' in href):
                website = website_link.get_text(strip=True)

        # Append the extracted info to the list
        company_info.append({
            'Company Name': name,
            'Website': website,
            'Address': address,
            'Phone Number': phone,
            # 'Customer name': customer_name,
            # 'Position': position,
            'Email Address': email
        })

# Create a DataFrame from the list
df = pd.DataFrame(company_info)

# Save the DataFrame to a CSV file
df.to_csv('company_info.csv', index=False, encoding='utf-8-sig')
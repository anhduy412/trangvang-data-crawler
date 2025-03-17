from bs4 import BeautifulSoup
import itertools
import requests
import pandas as pd

# Base URL of the website
# tphcm
# đồng nai
# bình dương
# bà rịa vũng tàu
# bình phước
# tây ninh
# long an
# tiền giang
url_list = [
    'https://trangvangvietnam.com/cateprovinces/486112/d%E1%BB%8Bch-v%E1%BB%A5-kho-b%C3%A3i-%E1%BB%9F-t%E1%BA%A1i-tp.-h%E1%BB%93-ch%C3%AD-minh-(tphcm).html?page=',
    'https://trangvangvietnam.com/cateprovinces/486112/d%E1%BB%8Bch-v%E1%BB%A5-kho-b%C3%A3i-%E1%BB%9F-t%E1%BA%A1i-%C4%91%E1%BB%93ng-nai.html?page=',
    'https://trangvangvietnam.com/cateprovinces/486112/d%E1%BB%8Bch-v%E1%BB%A5-kho-b%C3%A3i-%E1%BB%9F-t%E1%BA%A1i-b%C3%ACnh-d%C6%B0%C6%A1ng.html?page=',
    'https://trangvangvietnam.com/cateprovinces/486112/d%E1%BB%8Bch-v%E1%BB%A5-kho-b%C3%A3i-%E1%BB%9F-t%E1%BA%A1i-b%C3%A0-r%E1%BB%8Ba-v%C5%A9ng-t%C3%A0u.html?page=',
    'https://trangvangvietnam.com/cateprovinces/486112/d%E1%BB%8Bch-v%E1%BB%A5-kho-b%C3%A3i-%E1%BB%9F-t%E1%BA%A1i-b%C3%ACnh-ph%C6%B0%E1%BB%9Bc.html?page=',
    'https://trangvangvietnam.com/cateprovinces/486112/d%E1%BB%8Bch-v%E1%BB%A5-kho-b%C3%A3i-%E1%BB%9F-t%E1%BA%A1i-t%C3%A2y-ninh.html?page=',
    'https://trangvangvietnam.com/cateprovinces/486112/d%E1%BB%8Bch-v%E1%BB%A5-kho-b%C3%A3i-%E1%BB%9F-t%E1%BA%A1i-long-an.html?page=',
    'https://trangvangvietnam.com/cateprovinces/486112/d%E1%BB%8Bch-v%E1%BB%A5-kho-b%C3%A3i-%E1%BB%9F-t%E1%BA%A1i-ti%E1%BB%81n-giang.html?page='
]

# Initialize an empty list to hold company info
company_info = []

# Loop through each URL in the list
for base_url, page in itertools.product(url_list, range(1, 10)):
    # Construct the full URL for the current page
    url = f"{base_url}{page}"

    # Send a request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all company entries on the current page
    companies = soup.find_all('div', class_='w-100 h-auto shadow rounded-3 bg-white p-2 mb-3')

        # Loop through each company entry and extract details
    for company in companies:
        # Extract company name
        name = company.find('h2', class_="p-1 fs-5 h2 m-0 pt-0 ps-0 text-capitalize").get_text(strip=True)

        # Extract address
        if address_div := company.find('div', class_='logo_congty_diachi'):
            address = address_div.find_all('div')[1].get_text(strip=True) if len(address_div.find_all('div')) > 1 else ''
        elif address_div := company.find('div', class_='listing_diachi_nologo'):
            address = address_div.find_all('div')[1].get_text(strip=True) if len(address_div.find_all('div')) > 1 else ''
        else:
            address = ''

        # Extract phone number
        if phone_div := company.find('div', class_='listing_dienthoai'):
            phone = phone_div.find('a').get_text(strip=True) if phone_div.find('a') else ''
        elif phone_div := company.find('div', class_='p-2 pt-0 ps-0 pe-4 pb-0'):
            phone = phone_div.find('a').get_text(strip=True) if phone_div.find('a') else ''
        else:
            phone = ''

        # Extract email and website
        email_section = company.find('div', class_='email_web_section')
        email = ''
        website = ''

        if email_section:
            if email_link := email_section.find('a', href=lambda href: href and 'mailto:' in href):
                email = email_link['href'].replace('mailto:', '').strip()  # Extract email from href

            if website_link := email_section.find(
                'a', href=lambda href: href and 'http' in href
            ) or company.find('a', href=lambda href: href and 'http' in href):
                website = website_link.get_text(strip=True)

        # Extract company link
        company_link = company.find('a', href=True)['href']
        print(f'Getting data from {company_link}')

        # Visit the company's detailed page
        company_response = requests.get(company_link)
        company_soup = BeautifulSoup(company_response.content, 'html.parser')

        # Extract contact information from the detailed page
        contact_info = company_soup.find('div', class_='w-100 rounded-3 bg-white p-3 pt-4 mb-3 border-bottom')
        customer_name = None
        position = None
        if contact_info:
            if customer_name_tag := contact_info.find('small', class_='red_color fw500'):
                customer_name = customer_name_tag.get_text(strip=True)

            if position_tag := contact_info.find('span', string='Chức vụ:'):
                position = position_tag.find_next('small').get_text(strip=True)

        # Append the extracted info to the list in the correct order
        company_info.append({
            'Company Name': name,
            'Website': website,
            'Address': address,
            'Customer Name': customer_name,
            'Position': position,
            'Phone Number': phone,
            'Email Address': email
        })

# Create a DataFrame from the list
df = pd.DataFrame(company_info)

# Remove duplicate rows
df = df.drop_duplicates()

# Save the DataFrame to a CSV file
df.to_csv('company_info_with_contacts.csv', index=False, encoding='utf-8-sig')
print("Done.")
from bs4 import BeautifulSoup
import pandas as pd
import itertools
import requests

# Fetch the content of a page
def fetch_page_content(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def extract_companies_name(company):
    return company.find('h2', class_="p-1 fs-5 h2 m-0 pt-0 ps-0 text-capitalize").get_text(strip=True)

def extract_companies_address(company):
    address = ''
    if address_div := company.find('div', class_='logo_congty_diachi'):
        address = address_div.find_all('div')[1].get_text(strip=True) if len(address_div.find_all('div')) > 1 else ''
    elif address_div := company.find('div', class_='listing_diachi_nologo'):
        address = address_div.find_all('div')[1].get_text(strip=True) if len(address_div.find_all('div')) > 1 else ''
    return address

def extract_companies_phone(company):
    phone = ''
    if phone_div := company.find('div', class_='listing_dienthoai'):
        phone = phone_div.find('a').get_text(strip=True) if phone_div.find('a') else ''
    elif phone_div := company.find('div', class_='p-2 pt-0 ps-0 pe-4 pb-0'):
        phone = phone_div.find('a').get_text(strip=True) if phone_div.find('a') else ''
    return phone

def extract_email_and_website(company):
    email = ''
    website = ''
    email_section = company.find('div', class_='email_web_section')
    if email_section:
        if email_link := email_section.find('a', href=lambda href: href and 'mailto:' in href):
            email = email_link['href'].replace('mailto:', '').strip()
        if website_link := email_section.find('a', href=lambda href: href and 'http' in href) or company.find('a', href=lambda href: href and 'http' in href):
            website = website_link.get_text(strip=True)
    return email, website

def extract_contact_info(company_soup):
    contact_info = company_soup.find('div', class_='w-100 rounded-3 bg-white p-3 pt-4 mb-3 border-bottom')
    customer_name = None
    position = None
    customer_phone_number = None

    if contact_info:
        if customer_name_tag := contact_info.find('small', class_='red_color fw500'):
            customer_name = customer_name_tag.get_text(strip=True)
        if position_tag := contact_info.find('span', string='Chức vụ:'):
            position = position_tag.find_next('small').get_text(strip=True)
        if phone_tag := contact_info.find('span', string='Di động:'):
            customer_phone_number = phone_tag.find_next('small').get_text(strip=True)
    return customer_name, position, customer_phone_number

def extract_specialisation(url):
    specialisation = url.split('cateprovinces/')[1].split('/')[1].split('-ở-tại')[0]
    specialisation = requests.utils.unquote(specialisation) # type: ignore
    specialisation = specialisation.replace('-', ' ')
    return specialisation

def extract_company_details(company, base_url):
    company_link = company.find('a', href=True)['href']
    print(f'Getting data from {company_link}')
    company_soup = fetch_page_content(company_link)
    return {
        'Company Name': extract_companies_name(company),
        'Website': extract_email_and_website(company)[1],
        'Address': extract_companies_address(company),
        'Phone Number': extract_companies_phone(company),
        'Customer Name': extract_contact_info(company_soup)[0],
        'Position': extract_contact_info(company_soup)[1],
        'Customer Phone Number': extract_contact_info(company_soup)[2],
        'Email Address': extract_email_and_website(company)[0],
        'Specialise': extract_specialisation(base_url),
    }

def crawl_companies_info(url_list):
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

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df = df.drop_duplicates()
    df.to_csv(filename, index=False, encoding='utf-8-sig')
from utils.fetch_page_content import fetch_content
from utils.get_companies_name import get_name
from utils.get_companies_address import get_address
from utils.get_companies_phone import get_phone
from utils.get_companies_email_and_website import get_email_and_website
from utils.get_companies_contact import get_contact_info
from utils.get_companies_specialisation import get_specialisation
 
def get_detail_info(company, base_url):
    company_link = company.find('a', href=True)['href']
    print(f'Getting data from {company_link}')
    company_soup = fetch_content(company_link)
    return {
        'Company Name': get_name(company),
        'Website': get_email_and_website(company)[1],
        'Address': get_address(company),
        'Phone Number': get_phone(company),
        'Customer Name': get_contact_info(company_soup)[0],
        'Position': get_contact_info(company_soup)[1],
        'Customer Phone Number': get_contact_info(company_soup)[2],
        'Email Address': get_email_and_website(company)[0],
        'Specialise': get_specialisation(base_url)
    }
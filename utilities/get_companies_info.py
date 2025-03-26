from utilities.fetch_page_content import fetch_content
from utilities.get_companies_name import get_comp_name
from utilities.get_companies_address import get_comp_address
from utilities.get_companies_phone import get_comp_phone
from utilities.get_companies_email_and_website import extract_email_and_website
from utilities.get_companies_contact import extract_contact_info
from utilities.get_companies_specialisation import get_comp_specialisation
 
def get_comp_detail_info(company, base_url):
    company_link = company.find('a', href=True)['href']
    print(f'Getting data from {company_link}')
    company_soup = fetch_content(company_link)
    return {
        'Company Name': get_comp_name(company),
        'Website': extract_email_and_website(company)[1],
        'Address': get_comp_address(company),
        'Phone Number': get_comp_phone(company),
        'Customer Name': extract_contact_info(company_soup)[0],
        'Position': extract_contact_info(company_soup)[1],
        'Customer Phone Number': extract_contact_info(company_soup)[2],
        'Email Address': extract_email_and_website(company)[0],
        'Specialise': get_comp_specialisation(base_url)
    }
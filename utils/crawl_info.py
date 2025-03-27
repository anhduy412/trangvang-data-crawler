import itertools
from utils.fetch_page_content import fetch_content
from utils.get_companies_info import get_detail_info

def crawl_companies_info(url_list):
    company_info = []
    for base_url, page in itertools.product(url_list, range(2)):
        url = f"{base_url}{page}"
        soup = fetch_content(url)

        # Find all company entries on the current page
        companies = soup.find_all('div', class_='w-100 h-auto shadow rounded-3 bg-white p-2 mb-3')
        
        # Extract details for each company
        for company in companies:
            company_details = get_detail_info(company, base_url)
            company_info.append(company_details)
    return company_info
from utilities.crawl_info import crawl_companies_info

from utilities.save import save_to_csv
import config

# Crawl company info
company_info = crawl_companies_info(config.url_list)
save_to_csv(company_info, config.file_name)
print(f'Done, check {config.file_name} for data.')
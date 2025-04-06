from utils.crawl_info import crawl_companies_info
from utils.save_companies_info import save_to_csv
import config

# Crawl company info
company_info = crawl_companies_info(config.url_list)
save_to_csv(company_info, config.file_name)
print(f'Done, please check {config.file_name} for data.')
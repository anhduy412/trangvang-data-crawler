import config
import utils1 as utils

url_list = config.url_list
company_info = utils.crawl_companies_info(url_list)
utils.save_to_csv(company_info, 'company_info1.csv')
print("Done.")
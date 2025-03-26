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
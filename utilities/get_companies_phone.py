def get_comp_phone(company):
    phone = ''
    if phone_div := company.find('div', class_='listing_dienthoai'):
        phone = phone_div.find('a').get_text(strip=True) if phone_div.find('a') else ''
    elif phone_div := company.find('div', class_='p-2 pt-0 ps-0 pe-4 pb-0'):
        phone = phone_div.find('a').get_text(strip=True) if phone_div.find('a') else ''
    return phone
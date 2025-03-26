def get_comp_address(company):
    address = ''
    if address_div := company.find('div', class_='logo_congty_diachi'):
        address = address_div.find_all('div')[1].get_text(strip=True) if len(address_div.find_all('div')) > 1 else ''
    elif address_div := company.find('div', class_='listing_diachi_nologo'):
        address = address_div.find_all('div')[1].get_text(strip=True) if len(address_div.find_all('div')) > 1 else ''
    return address
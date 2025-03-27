def get_email_and_website(company):
    email_section = company.find('div', class_='email_web_section')
    email = ''
    website = ''
    if email_section:
        if email_link := email_section.find('a', href=lambda href: href and 'mailto:' in href):
            email = email_link['href'].replace('mailto:', '').strip()
        if website_link := email_section.find('a', href=lambda href: href and 'http' in href) or company.find('a', href=lambda href: href and 'http' in href):
            website = website_link.get_text(strip=True)
    return email, website
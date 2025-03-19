import requests

# Extract specialisation from the URL
def extract_specialisation(url):
    specialisation = url.split('cateprovinces/')[1].split('/')[1].split('-ở-tại')[0]
    specialisation = requests.utils.unquote(specialisation) # type: ignore
    specialisation = specialisation.replace('-', ' ')
    return specialisation
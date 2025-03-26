import requests

def get_comp_specialisation(url):
    specialisation = url.split('cateprovinces/')[1].split('/')[1].split('-%E1%BB%9F-t%E1%BA%A1i-')[0]
    specialisation = requests.utils.unquote(specialisation) # type: ignore
    specialisation = specialisation.replace('-', ' ')
    return specialisation
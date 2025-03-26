# List of URLs to scrape provinces: TPHCM, đồng nai, bình dương, bà rịa vũng tàu, bình phước, tây ninh, long an, tiền giang
url_list = [
    'https://trangvangvietnam.com/cateprovinces/37310/v%E1%BA%ADt-li%E1%BB%87u-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-tp.-h%E1%BB%93-ch%C3%AD-minh-(tphcm).html?page=',
    'https://trangvangvietnam.com/cateprovinces/37310/v%E1%BA%ADt-li%E1%BB%87u-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-%C4%91%E1%BB%93ng-nai.html?page=',
    'https://trangvangvietnam.com/cateprovinces/37310/v%E1%BA%ADt-li%E1%BB%87u-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-b%C3%ACnh-d%C6%B0%C6%A1ng.html?page=',
    'https://trangvangvietnam.com/cateprovinces/37310/v%E1%BA%ADt-li%E1%BB%87u-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-b%C3%A0-r%E1%BB%8Ba-v%C5%A9ng-t%C3%A0u.html?page=',
    'https://trangvangvietnam.com/cateprovinces/37310/v%E1%BA%ADt-li%E1%BB%87u-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-b%C3%A2n-ph%C6%B0%E1%BB%9Bc.html?page=',
    'https://trangvangvietnam.com/cateprovinces/37310/v%E1%BA%ADt-li%E1%BB%87u-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-t%C3%A2y-ninh.html?page=',
    'https://trangvangvietnam.com/cateprovinces/37310/v%E1%BA%ADt-li%E1%BB%87u-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-long-an.html?page=',
    'https://trangvangvietnam.com/cateprovinces/37310/v%E1%BA%ADt-li%E1%BB%87u-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-ti%E1%BB%81n-giang.html?page=',
    'https://trangvangvietnam.com/cateprovinces/37160/thi%E1%BA%BFt-k%E1%BA%BF-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-tp.-h%E1%BB%93-ch%C3%AD-minh-(tphcm).html?page=',
    'https://trangvangvietnam.com/cateprovinces/37160/thi%E1%BA%BFt-k%E1%BA%BF-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-%C4%91%E1%BB%93ng-nai.html?page=',
    'https://trangvangvietnam.com/cateprovinces/37160/thi%E1%BA%BFt-k%E1%BA%BF-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-b%C3%ACnh-d%C6%B0%C6%A1ng.html?page=',
    'https://trangvangvietnam.com/cateprovinces/37160/thi%E1%BA%BFt-k%E1%BA%BF-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-b%C3%A0-r%E1%BB%8Ba-v%C5%A9ng-t%C3%A0u.html?page=',
    'https://trangvangvietnam.com/cateprovinces/37160/thi%E1%BA%BFt-k%E1%BA%BF-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-b%C3%A2n-ph%C6%B0%E1%BB%9Bc.html?page=',
    'https://trangvangvietnam.com/cateprovinces/37160/thi%E1%BA%BFt-k%E1%BA%BF-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-t%C3%A2y-ninh.html?page=',
    'https://trangvangvietnam.com/cateprovinces/37160/thi%E1%BA%BFt-k%E1%BA%BF-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-long-an.html?page=',
    'https://trangvangvietnam.com/cateprovinces/37160/thi%E1%BA%BFt-k%E1%BA%BF-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-ti%E1%BB%81n-giang.html?page='
    'https://trangvangvietnam.com/cateprovinces/319435/c%C3%B4ng-ty-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-tp.-h%E1%BB%93-ch%C3%AD-minh-(tphcm).html?page=',
    'https://trangvangvietnam.com/cateprovinces/319435/c%C3%B4ng-ty-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-%C4%91%E1%BB%93ng-nai.html?page=',
    'https://trangvangvietnam.com/cateprovinces/319435/c%C3%B4ng-ty-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-b%C3%ACnh-d%C6%B0%C6%A1ng.html?page=',
    'https://trangvangvietnam.com/cateprovinces/319435/c%C3%B4ng-ty-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-b%C3%A0-r%E1%BB%8Ba-v%C5%A9ng-t%C3%A0u.html?page=',
    'https://trangvangvietnam.com/cateprovinces/319435/c%C3%B4ng-ty-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-b%C3%A2n-ph%C6%B0%E1%BB%9Bc.html?page=',
    'https://trangvangvietnam.com/cateprovinces/319435/c%C3%B4ng-ty-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-t%C3%A2y-ninh.html?page=',
    'https://trangvangvietnam.com/cateprovinces/319435/c%C3%B4ng-ty-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-long-an.html?page=',
    'https://trangvangvietnam.com/cateprovinces/319435/c%C3%B4ng-ty-x%C3%A2y-d%E1%BB%B1ng-%E1%BB%9F-t%E1%BA%A1i-ti%E1%BB%81n-giang.html?page='
]

# File name
file_name = 'data/company_info1.csv'
# list of URLs to scrape
# tphcm
# đồng nai
# bình dương
# bà rịa vũng tàu
# bình phước
# tây ninh
# long an
# tiền giang
url_list = [
    'https://trangvangvietnam.com/cateprovinces/258660/h%C3%A0n-thi%E1%BA%BFt-b%E1%BB%8B-h%C3%A0n-v%C3%A0-v%E1%BA%ADt-li%E1%BB%87u-h%C3%A0n-%E1%BB%9F-t%E1%BA%A1i-tp.-h%E1%BB%93-ch%C3%AD-minh-%28tphcm%29.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/258660/h%C3%A0n-thi%E1%BA%BFt-b%E1%BB%8B-h%C3%A0n-v%C3%A0-v%E1%BA%ADt-li%E1%BB%87u-h%C3%A0n-%E1%BB%9F-t%E1%BA%A1i-%C4%91%E1%BB%93ng-nai.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/258660/h%C3%A0n-thi%E1%BA%BFt-b%E1%BB%8B-h%C3%A0n-v%C3%A0-v%E1%BA%ADt-li%E1%BB%87u-h%C3%A0n-%E1%BB%9F-t%E1%BA%A1i-b%C3%ACnh-d%C6%B0%C6%A1ng.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/258660/h%C3%A0n-thi%E1%BA%BFt-b%E1%BB%8B-h%C3%A0n-v%C3%A0-v%E1%BA%ADt-li%E1%BB%87u-h%C3%A0n-%E1%BB%9F-t%E1%BA%A1i-b%C3%A0-r%E1%BB%8Ba-v%C5%A9ng-t%C3%A0u.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/258660/h%C3%A0n-thi%E1%BA%BFt-b%E1%BB%8B-h%C3%A0n-v%C3%A0-v%E1%BA%ADt-li%E1%BB%87u-h%C3%A0n-%E1%BB%9F-t%E1%BA%A1i-b%C3%ACnh-ph%C6%B0%E1%BB%9Bc.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/258660/h%C3%A0n-thi%E1%BA%BFt-b%E1%BB%8B-h%C3%A0n-v%C3%A0-v%E1%BA%ADt-li%E1%BB%87u-h%C3%A0n-%E1%BB%9F-t%E1%BA%A1i-t%C3%A2y-ninh.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/258660/h%C3%A0n-thi%E1%BA%BFt-b%E1%BB%8B-h%C3%A0n-v%C3%A0-v%E1%BA%ADt-li%E1%BB%87u-h%C3%A0n-%E1%BB%9F-t%E1%BA%A1i-long-an.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/258660/h%C3%A0n-thi%E1%BA%BFt-b%E1%BB%8B-h%C3%A0n-v%C3%A0-v%E1%BA%ADt-li%E1%BB%87u-h%C3%A0n-%E1%BB%9F-t%E1%BA%A1i-ti%E1%BB%81n-giang.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/492073/h%C3%A0n-c%C6%A1-kh%C3%AD-d%E1%BB%8Bch-v%E1%BB%A5-h%C3%A0n-laser-gi%C3%B3-%C4%91%C3%A1-h%E1%BB%93-quang-%C4%91i%E1%BB%87n%2C.-%E1%BB%9F-t%E1%BA%A1i-tp.-h%E1%BB%93-ch%C3%AD-minh-%28tphcm%29.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/492073/h%C3%A0n-c%C6%A1-kh%C3%AD-d%E1%BB%8Bch-v%E1%BB%A5-h%C3%A0n-laser-gi%C3%B3-%C4%91%C3%A1-h%E1%BB%93-quang-%C4%91i%E1%BB%87n%2C.-%E1%BB%9F-t%E1%BA%A1i-%C4%91%E1%BB%93ng-nai.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/492073/h%C3%A0n-c%C6%A1-kh%C3%AD-d%E1%BB%8Bch-v%E1%BB%A5-h%C3%A0n-laser-gi%C3%B3-%C4%91%C3%A1-h%E1%BB%93-quang-%C4%91i%E1%BB%87n%2C.-%E1%BB%9F-t%E1%BA%A1i-b%C3%ACnh-d%C6%B0%C6%A1ng.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/492073/h%C3%A0n-c%C6%A1-kh%C3%AD-d%E1%BB%8Bch-v%E1%BB%A5-h%C3%A0n-laser-gi%C3%B3-%C4%91%C3%A1-h%E1%BB%93-quang-%C4%91i%E1%BB%87n%2C.-%E1%BB%9F-t%E1%BA%A1i-b%C3%A0-r%E1%BB%8Ba-v%C5%A9ng-t%C3%A0u.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/492073/h%C3%A0n-c%C6%A1-kh%C3%AD-d%E1%BB%8Bch-v%E1%BB%A5-h%C3%A0n-laser-gi%C3%B3-%C4%91%C3%A1-h%E1%BB%93-quang-%C4%91i%E1%BB%87n%2C.-%E1%BB%9F-t%E1%BA%A1i-b%C3%ACnh-ph%C6%B0%E1%BB%9Bc.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/492073/h%C3%A0n-c%C6%A1-kh%C3%AD-d%E1%BB%8Bch-v%E1%BB%A5-h%C3%A0n-laser-gi%C3%B3-%C4%91%C3%A1-h%E1%BB%93-quang-%C4%91i%E1%BB%87n%2C.-%E1%BB%9F-t%E1%BA%A1i-t%C3%A2y-ninh.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/492073/h%C3%A0n-c%C6%A1-kh%C3%AD-d%E1%BB%8Bch-v%E1%BB%A5-h%C3%A0n-laser-gi%C3%B3-%C4%91%C3%A1-h%E1%BB%93-quang-%C4%91i%E1%BB%87n%2C.-%E1%BB%9F-t%E1%BA%A1i-long-an.html?page=',
    # 'https://trangvangvietnam.com/cateprovinces/492073/h%C3%A0n-c%C6%A1-kh%C3%AD-d%E1%BB%8Bch-v%E1%BB%A5-h%C3%A0n-laser-gi%C3%B3-%C4%91%C3%A1-h%E1%BB%93-quang-%C4%91i%E1%BB%87n%2C.-%E1%BB%9F-t%E1%BA%A1i-ti%E1%BB%81n-giang.html?page=',
]

file_name = 'data/company_info.csv'
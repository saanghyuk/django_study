
import json # ranks?limit=10이 json파일로 와서 import
import urllib.request as req
from urllib.error import URLError, HTTPError



# 다음 주식 요청 url
url = "https://finance.daum.net/api/search/ranks?limit=10"

# try:
# 요청
res = req.urlopen(url).info()
print(res)


# except HTTPError as e:
#     print('Download Failed.')
#     print('HttpError Code:', e)
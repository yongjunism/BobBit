import requests 
client_id = 'R5V8X2w9Pkvb5_9XWb1P'
client_secret = 'EuFmp6rjVk'

keyword = '계란 가격' 
url = 'https://openapi.naver.com/v1/search/news.json' 
headers = {'X-Naver-Client-Id':client_id, 'X-Naver-Client-Secret':client_secret} 
params = {'query':keyword, 'sort':'date', 'display':3} 
r = requests.get(url, params = params, headers = headers)

j = r.json()
print(j.keys())
print(j['items'][0])
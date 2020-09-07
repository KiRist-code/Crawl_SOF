import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

class searchSOF():

    baseUrl = 'https://stackoverflow.com/'
    search = input()
    
    search_url = url + quote_plu(search)
    html = urlopen(search_url)
    source = html.read() # 바이트코드 type으로 소스를 읽는다.
    html.close() # urlopen을 진행한 후에는 close를 한다.

    soup = BeautifulSoup(source, "html5lib")
    result = soup.find_all(class_="result-link")

    for i in result:
        title = result.get_text()
        embed_input[i][0] = title #n번째 0째줄은 title, 1째줄은 url
        link = result.a.get('href')
        result_url = 'https://stackoverflow.com' + link
        embed_input[i][1] = result_url

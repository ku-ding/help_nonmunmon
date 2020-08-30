from requests_html import HTMLSession
import pandas as pd

def crawler(maxpage):
    session = HTMLSession()
    result = {}
    result['naver'] = [] #카테고리 ['site_name']

    for i in range(1, maxpage+1):
        #str 부분은 페이지 넘버, url 넣는 부분
        set_url = 'https://terms.naver.com/list.nhn?cid=41989&categoryId=41989&so=st1.dsc&viewType=&categoryType=&page='+str(i)
        url = session.get(set_url)    
        base = url.html.find('div.info_area')  

        for d in base:
            concept = {}
            concept['name'] = d.find('a')[0].text  # 단어 이름
            text_url = list(d.find('div.subject')[0].absolute_links)[0] #단어 url
            set_url = text_url
            url = session.get(set_url)
            try: #단어 뜻 (단어 뜻이 여러 개 일때 값이 다르기 때문에 예외처리함)
                concept['text'] = url.html.find('p.txt')[0].text
            except: 
                concept['text'] = url.html.find('dd')[0].text
            
            concept['url'] = text_url
            result['naver'].append(concept)

    return result


#어느 페이지까지 크롤링할건지 파라미터로 넘기기
data = crawler(2)
#print(data)
save_file = pd.DataFrame(data['naver'], columns = ['name', 'text', 'url'])
save_file.to_csv('test.csv', encoding ='utf-8-sig', index = False)


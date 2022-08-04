# 할리스 커피숍 매장 정보 크롤링
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime

def getHollysStoreInfo(result):

    for page in range(1,53+1):
        Hollys_url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}'
        # print(Hollys_url)
        html = urllib.request.urlopen(Hollys_url)
        soup = BeautifulSoup(html, 'html.parser')
        tbody = soup.find('tbody')

        for store in tbody.find_all('tr'):
            if len(store) <= 3: break

            store_td = store.find_all('td')

            store_name = store_td[1].string
            store_sido = store_td[0].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            
            result.append([store_name]+[store_sido]+[store_address]+[store_phone])

    #result
    print('완료!!')

def main():
    result = []
    print('할리스 매장 크롤링 >>>')
    getHollysStoreInfo(result)

    # 판다스 데이터 프레임 생성
    columns = ['store','sido-gu', 'address','phone']
    Hollys_df= pd.DataFrame(result, columns=columns)

    # csv 저장, 경로를 './'로 지정해서 저장하면 StudyBigData 스키마에 저장됨(파이썬과 주피터 노트북의 경로가 다름)
    Hollys_df.to_csv('./hollys_shop_info.csv',index=True, encoding='utf-8')
    # 밑에처럼 경로 지정해서 저장하면, day03 폴더에 저장됨
    # Hollys_df.to_csv('C:/localRepository/StudyBigData/day03/hollys_shop_info.csv',index=True, encoding='utf-8')
    print('저장완료')

    del result[:]

if __name__ == '__main__':
    main()


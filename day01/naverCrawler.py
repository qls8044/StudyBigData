import os
import sys
from tracemalloc import start
import urllib.request
import urllib.parse
import datetime
import time
import json

client_id = 'OJJDKJIS2WTSrYwSwd1y'
client_secret = 'nu1hjpck0k'

# request는 클라이언트가 서버한테 요청하는 것, 클라이언트 거임
# response는 서버가 요청 받은 것을 처리하고 클라이언트한테 결과 값을 보내는 것, 서버거임


# url 접속 요청 후 응답 리턴 함수
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header('X-Naver-Client-Id', client_id)
    req.add_header('X-Naver-Client-Secret',client_secret)

    try: #request가 끊기면 오류가 생겼을 때, 처리하는 방법 정의
        res = urllib.request.urlopen(req)
        if res.getcode() == 200: #200은 ok이고, 400번대는 일반 error, 500번대는 server error
            print(f'[({datetime.datetime.now()})] Url Request success')
            return res.read().decode('utf-8') #에러가 날만한 상황을 제시함
    except Exception as e:
        print(e)
        print(f'[{datetime.datetime.now()}] Error for URL : {url}')
        return None # 에러가 나면 이렇게 해라고 지정


# 핵심함수, 네이버 API 검색
def getNaverSearch(node, srcText, start, display):
    base = 'https://openapi.naver.com/v1/search'
    node = f'/{node}.json'
    text = urllib.parse.quote(srcText) # url 주소에 맞춰서 파싱
    params = f'?query={text}&start={start}&display={display}'

    url = base + node + params
    resDecode = getRequestUrl(url)

    if resDecode==None:
        return None
    else:
        return json.loads(resDecode)

def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    originallink = post['originallink']
    link = post['link']
    pubDate = datetime.datetime.strptime(post['pubDate'],'%a, %d %b %Y %H:%M:%S +0900')
    pubDate = pubDate.strftime('%Y-%m-%d %H:%M:$S') # 2022-08-02 15:50:00

    jsonResult.append({'cnt':cnt, 'title':title, 'description':description, 'originallink':originallink, 'link':link})


# 실행 최초 함수
def main():
    node = 'news'
    srcText = input('검색어를 입력하세요 : ')
    cnt = 0
    jsonResult = []

    jsonRes = getNaverSearch(node, srcText, 1, 50)
     # print(jsonRes)
    total = jsonRes['total'] # 총 검색된 뉴스 개수가 total임

    while ((jsonRes != None) and (jsonRes['display'] != 0)):
        for post in jsonRes['items']:
            cnt += 1
            getPostData(post,jsonResult, cnt)

        start = jsonRes['start'] + jsonRes['display'] # 이케하면 처음에는 1~50까지 그 다음에는 (1+50)51~100까지 등등 데이터가 다 나올 때까지 반복됨
        jsonRes = getNaverSearch(node, srcText, start, 50)

    print(f'전체 검색 : {total} 건')

    # file output
    with open(f'./{srcText}_naver_{node}.json', mode='w', encoding='utf-8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(jsonFile)
    print(f'가져온 데이터 : {cnt} 건')
    print(f'{srcText}_naver_{node}.json SAVED')

if __name__ == '__main__': # __가 들어간 함수는 내가 지정하는 함수가 아니라 내장되어있는 내장함수임
    main()  #  if __name__=="__main__"이라는 조건문을 넣어주고 그 아래는 직접 실행시켰을 때만 실행되길 원하는 코드들을 넣어주는 것



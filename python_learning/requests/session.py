import requests

def session_test():
    session1 = requests.Session()
    url = 'http://www.baidu.com/login'
    data = {'wd': '<UNK>'}
    session1.post(url, data=data)
    url2 = 'http://www.baidu.com/search'
    data = {'hospital': '北大人民医院'}


    # newsession = requests.Session()
    # response = newsession.get(url, data=data, cookies=session1.cookies)
    response = session1.post(url2, data=data)
    
    print(response.text)
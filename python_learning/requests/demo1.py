import requests

def get_html():
    params = {"key1": "value1", "key2": "value2"}
    url = "http://python.org"
    r = requests.get(url, params=params)
    print(r.url)

def post_html():
    data = {"key1": "value1", "key2": "value2"}
    url = "http://httpbin.org/post"
    r = requests.post(url, data=data)
    print(r.json())

if __name__ == '__main__':
    post_html()
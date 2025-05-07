import requests
import lxml.etree


url = 'https://book.douban.com/subject/37129165/?icn=index-latestbook-subject'

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    selector = lxml.etree.HTML(response.text) # 使用 etree 对html进行解析
    name = selector.xpath('//*[@id="wrapper"]/h1/span/text()') # 解析完成之后使用xpath进行匹配
    print(name)


if __name__ == '__main__':
    get_html(url)
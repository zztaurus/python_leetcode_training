import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    bs_info = BeautifulSoup(response.text, 'html.parser')
    for tags in bs_info.find_all('div', attrs={'class': 'pl2'}):
        a_tags = tags.find_all('a')
        for a_tag in a_tags:
            print(a_tag.get('href'))
            print(a_tag.get('title'))
        print("=" * 20)


if __name__ == '__main__':
    urls = tuple(f'https://book.douban.com/top250?start={ page * 25 }' for page in range(25))
    for url in urls:
        get_html(url)
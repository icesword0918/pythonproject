import re
import requests
from requests.exceptions import RequestException
import json
from multiprocessing import Pool


def get_one_page(url):
    try:
        # 设置请求头，模拟浏览器访问
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            # print(response.text)
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+).*?</i>'
                         + '.*?data-src="(.*?)"'
                         + '.*?name"><a.*?>(.*?)</a>'
                         + '.*?star">(.*?)</p>'
                         + '.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>'
                         + '.*?fraction">(.*?)</i>.*?</dd>', re.S)  # re.S 表示 ‘.’可以匹配换行符
    items = re.findall(pattern, html)
    for item in items:
        # 返回一个生成器对象
        yield {'index': item[0], 'image': item[1], 'title': item[2], 'actor': item[3].strip()[3:],
               'releasetime': item[4].strip()[5:], 'score': item[5] + item[6]}


def write_to_file(content):
    # a以追加的形式把结果写入文件,并设置以utf-8编码
    with open('result.txt', 'a', encoding='utf-8') as f: f.write(json.dumps(content, ensure_ascii=False) + '\n')
    f.close()


def main(offset):
    url = 'https://maoyan.com/board/7' + str(offset)
    print(url)
    html = get_one_page(url)
    # print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    # 创建进程池
    pool = Pool()
    # 第一个参数是函数，第二个参数是一个迭代器，将迭代器中的数字作为参数依次传入函数中（这里用列表推导式创建列表）
    pool.map(main, [i * 10 for i in range(10)])

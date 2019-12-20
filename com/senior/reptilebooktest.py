import re
import requests
from requests import RequestException
import time
import json

class Book():
   def __call__(self, *args, **kwargs):
       self.run()

   def run(self):
        try:
            url = "http://www.bookschina.com/24hour/"
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                html = response.text
                self.get_data(html)
                # print(html)
            else:
                print("连接超时")
        except RequestException:
            print("错误")

   def get_data(self,html):
       # print(html)
       dd_list = re.findall('.*?name"><a.*?>(.*?)</a>.*?author"><a.*?>(.*?)</a>.*?publisher"><a.*?>(.*?)</a>.*?sellPrice">&yen;(.*?)</span>.*?priceTit">(.*?)</span><del class="">&yen;(.*?)</del>', html)
       print(dd_list)
       # for i in dd_list.:
          # print(dd_list[i])

"""       pattern = re.compile(
           '<dd>.*?bookList.*?>(.*?)</i>.*?name.*?a.*?>(.*?)</a>.*?author.*?>(.*?)</a>.*?publisher.*?>(.*?)</a>.*?'
           'priceWrap.*?>(.*?)</a></dd>',
           re.S)
       items = re.findall(pattern, html)
       for item in items:
           # 返回一个生成器对象
           yield {'index': item[0], 'image': item[1], 'title': item[2], 'author': item[3].strip()[3:],
                  'publisher': item[4].strip()[5:], 'score': item[5] + item[6]}"""


if __name__=='__main__':
    book=Book()
    book()

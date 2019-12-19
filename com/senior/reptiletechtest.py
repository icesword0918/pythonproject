# 1、python的网络请求
import urllib.request
import urllib.parse
import urllib3
import requests
from bs4 import BeautifulSoup  # 导入Beautiful Soup库

# 1)urllib模块
# 打开指定需要爬取的网页
response=urllib.request.urlopen('https://www.baidu.com/')
html=response.read()  # 读取网页代码
print(html)   # 打印读取内容

"""
# 将数据使用urlencode编码处理后，再使用encoding设置为utf-8编码
data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
# 打开指定需要爬取的网页
response1=urllib.request.urlopen('https://httpbin.org/post',data=data)
html1=response1.read()  # 读取网页代码
print(html1)   # 打印读取内容
"""

# 2)rullib3模块
# 创建PoolManager对象,用于处理与线程池的连接以及线程安全的所有细节
http=urllib3.PoolManager()
# 对需要爬取的网页发送请求
response2=http.request('get','https://www.baidu.com/')
print(response2.data)


# 3)requests模块
response4=requests.get('https://www.baidu.com/')
print(response4.status_code)  # 打印状态码
print(response4.url)  # 打印请求url
print(response4.headers)  # 打印头部信息
print(response4.cookies)   # 打印cookie信息
print(response4.text)  # 以文本形式打印网页源码
print(response4.content)   # 以字节流形式打印网页源码

# 2、请求headers处理
url='https://www.baidu.com/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.288'}
response5=requests.get(url,headers=headers)  # 发送网络请求
print()
print("请求headers处理")
print(response5.content)

# 3、网络超时
for a in  range(0,20):
    try:
        # 设置超时时间未0.25秒
        response6=requests.get('https://www.baidu.com/',timeout=0.25)
        print(response6.status_code)   # 打印状态码
    except Exception as e:             # 捕获异常
        print('异常'+str(e))           # 打印异常信息

# 导入requests.exceptions模块中的3种异常类
from requests.exceptions import ReadTimeout,HTTPError,RequestException
# 循环发送请求20次
for a in range(0,20):
    try:
        # 设置超时时间未0.25秒
        response6=requests.get('https://www.baidu.com/',timeout=0.25)
        print(response6.status_code)   # 打印状态码
    except ReadTimeout:             # 超时异常
        print("timeout")
    except HTTPError:    # Http异常
        print("httperror")
    except RequestException:   # 请求异常
        print('reqerror')


# 4、代理服务
"""
proxy={'http':'183.154.50.123:9999','https':'183.154.50.123:9999'}  # 设置代理ip与对应的端口号
# 对需要爬取的网页发送请求
response7=requests.get('https://www.baidu.com/',proxies=proxy)
print(response7.content)
"""

# 5、HTML解析之Beautiful Soup
# 创建Beautiful Soup对象打开需要解析的html文件
soup=BeautifulSoup(open('index.html','r', encoding='UTF-8'),'lxml')
print(soup.prettify())  # 打印格式化后的代码

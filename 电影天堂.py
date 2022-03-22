#1.定位到大窗口
#2.从大窗口中提取子页面的链接地址
#3.请求子页面的链接地址，拿到我们想要的下载地址
import requests
import re

domain = "https://www.dytt89.com/"
resp = requests.get(domain)  #verify=False
resp.encoding = "gb2312"

#拿到ul里面的li
obj1 = re.compile(r"2022必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名　(?P<moviename>.*?)<br />'
                  r'.*?<a href="(?P<download>.*?)">', re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for it in result1:
    ul = it.group("ul")
        #提取子页面连接：
    result2 = obj2.finditer(ul)
    for itt in result2:
        #拼接子页面url地址 ：域名 +子页面地址
        chlid_href = domain + itt.group("href").strip("/")
        child_href_list.append(chlid_href)
        #print(itt.group("href"))

#提取子页面内容
for href in child_href_list:
    child_resp = requests.get(href)
    child_resp.encoding = "gb2312"

    result3 = obj3.search(child_resp.text)
    print(result3.group("moviename"))
    print(result3.group("download"))
    #break #测试

resp.close()
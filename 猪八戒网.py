# -*- coding = utf-8 -*-
# @Time :2022/2/16 9:16

#拿页面源代码
#提取解析数据
import requests
from lxml import etree

url = 'https://chongqing.zbj.com/search/f/?kw=saas'
resp = requests.get(url)
#print(resp.text)

#解析
html = etree.HTML(resp.text)
#每一个服务商的div
divs = html.xpath('/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div')
for div in divs:
    price = div.xpath('./div/div/a[2]/div[2]/div[1]/span[1]/text()')[0].strip('¥')
    title = "saas".join(div.xpath('./div/div/a[2]/div[2]/div[2]/p/text()'))
    Company_name = div.xpath('./div/div/a[1]/div[1]/p/text()')#.replace('\n\n', '\n\n','        ')
    location = div.xpath('./div/div/a[1]/div[1]/div/span/text()')[0]
    Company_name.pop(0)
    #for Company_name in Company_name:

    print(title, end='')
    print(Company_name, end='')
    print(location, end='')
    print(price)



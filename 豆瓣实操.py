#拿源代码
#通过re提取内容
import requests
import re
import csv

url = "https://movie.douban.com/top250?start="


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
}

for i in range(0, 250, 25):
    url_i = url + str(i)
    print(url_i)
    resp = requests.get(url = url_i, headers=headers)

    page_content = resp.text

    #解析数据
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                     r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                     r'.*?<span class="rating_num" property="v:average">'
                     r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)

    result = obj.finditer(page_content)
    f = open("data.csv", mode="a", encoding="utf-8")
    csvwriter = csv.writer(f)
    for it in result:
        # print(it.group("name"))
        # print(it.group("score"), "评分")
        # print(it.group("num"), "人评价")
        # print(it.group("year").strip(), "年")
        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
    f.close()
    print("over")


# resp.close()
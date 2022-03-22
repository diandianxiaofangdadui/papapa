# -*- coding = utf-8 -*-
# @Time :2022/3/3 9:59
import requests
import random
import json
import pymysql


class Tianjin():
    def __init__(self):
        self.content = pymysql.connect(
            host='172.168.1.209',
            user='sqluser', password='kangzhou008',
            database='cuiqi',
            charset='utf8'
        )
        self.cursor = self.content.cursor()
    def random(self):
        i = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'o', 'p', 'q', 's', 't', 'u', 'v', 'w',
             'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z',
             0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ]
        a = ''.join(map(str, random.choices(i, k=4)))
        return a
    def get_ip(self):
        url = 'http://121.43.158.142:7777/get'
        while True:
            try:
                ip = requests.get(url=url, timeout=2).text
                break
            except:
                pass
        ip_dic = {"http": "http://" + ip, "https": "https://" + ip}
        return ip_dic
    def main(self):
        a = self.random()
        self.url = 'https://tps.ylbz.tj.gov.cn/csb/1.0.0/guideGetMedList'
        headers = {
            "Accept": "application/json,text/plain, */*",
            'Accept-Encoding': 'gzip,deflate, br',
            'Accept-Language': 'zh-CN,zh;q = 0.9',
            'Connection': 'keep-alive',
            'Content-Length': '52',
            'Content-Type': 'application/json',
            'Host': 'tps.ylbz.tj.gov.cn',
            'Origin': 'https: // tps.ylbz.tj.gov.cn',
            'Referer': 'https://tps.ylbz.tj.gov.cn/drugGuide/tps-local/b/',
            'sec-ch-ua': '" Not A;Brand";v = "99", "Chromium";v = "96", "Google Chrome";v = "96"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
        }
        data = {
            "content": "%",
            "verificationCode": a
        }
        resp = requests.post(url = self.url, headers = headers, data = json.dumps(data),proxies = self.get_ip(),timeout = 10).json()
        for dic_2 in resp["data"]['list']:
            medid = dic_2["medid"]          # medid
            genname = dic_2["genname"]      # 药品名称
            prodname = dic_2["prodname"]    # 商品名
            dosform = dic_2["dosform"]      # 剂型
            spec = dic_2["spec"]            # 规格
            pac = dic_2["pac"]              # 包装
            minSalunt = dic_2["minSalunt"]  # 采购单位
            prodentp = dic_2["prodentp"]    # 生产企业
            aprvno = dic_2["aprvno"]        # 批准文号

            sql = "insert into 天津(`药品名称(通用名)`, 商品名, 剂型, 规格, 包装, 采购单位, 生产企业, 批准文号, medid) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (str(genname), str(prodname), str(dosform), str(spec), str(pac), str(minSalunt), str(prodentp), str(aprvno),str(medid)))
            self.content.commit()
            print("成功存入数据库")

if __name__ == '__main__':
    run = Tianjin()
    run.main()


import time

import requests
from lxml import etree
import pymysql


class japic():
    def __init__(self):
        self.url = "https://database.japic.or.jp/ctrl/attDocsList"
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                      'application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '213',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'Target=small; JSESSIONID=640DD4A1269ABEEC2E50A19F750C2CC8; FirstAccessDate="2022-03-01 '
                      '14:38:05"; UserLoginPassword = ""; UserMailAddress= ""; LastLoginDate= ""; Jointed = ""; '
                      'LastAccessDate="2022-03-01 14:55:55"',
            'Host': 'database.japic.or.jp',
            'Origin': 'https://database.japic.or.jp',
            'Referer': 'https://database.japic.or.jp/ctrl/attDocsForm',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Microsoft Edge";v="98"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62 '
        }

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
        conn = pymysql.connect(host='172.168.1.209', user='sqluser', password='kangzhou008', database='cuiqi',
                               charset='utf8')
        cursor = conn.cursor()
        baseurl = "https://database.japic.or.jp/ctrl/attDocsList2?pageNumber="
        for i in range(1, 257):  # 按每页100项来取，一共256页
            url = baseurl + str(i)
            data1 = {  # 医疗用途
                'rowsPerPage': '100',
                'screenType': '1',
                'compulsiveDisplay': '0',
                'highlight': '1',
                'processType': '1',
            }
            while True:
                try:
                    res1 = requests.post(url=url, headers=self.headers, data=data1, proxies=self.get_ip())
                    if res1.status_code == 200:
                        res1 = res1.text
                        # print(res1)
                        break
                except:

                    pass
            html = etree.HTML(res1)
            all_datas = html.xpath('//table[@class="table"]')  # 销售名称
            # print(all_datas)
            for data in all_datas:
                sale_name = str(data.xpath('./tr[1]/td[2]/table/tr/td/font/text()')[0]).lstrip().rstrip()  # 销售名称

                Active_ingredients = str(
                    data.xpath('./tr[2]/td[2]/table/tr/td/font/text()')[0]).lstrip().rstrip()  # 有效成分

                company = str(data.xpath('./tr[3]/td[2]/font/text()')).replace(r'\n', '').replace(
                    r'\t', '').replace(r'\r', '').replace(r'\xa0', '').replace(' ', '').replace('\']', '').replace(
                    '[\'', '')  # 公司名
                print(sale_name)
                #save_japic = """
                #    insert into japic (sale_name,Active_ingredients,company) values(%s,%s,%s)
                """

                cursor.execute(save_japic, (str(sale_name), str(Active_ingredients), str(company)))
                conn.commit()

                # print(sale_name)
                #
                print(Active_ingredients)
                print(company)
            print("成功保存第%d页" % i) """


if __name__ == '__main__':
    run = japic()
    run.main()


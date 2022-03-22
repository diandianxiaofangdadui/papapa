import requests
import json
import pymysql
content = pymysql.connect(
            host='172.168.1.209',
            user='sqluser', password='kangzhou008',
            database='cuiqi',
            charset='utf8'
        )
cursor = content.cursor()
# url = "https://fuwu.nhsa.gov.cn/tps/web/mgr/pubonlnQury/query"
# headers = {
# 'Accept':'application/json, text/plain, */*',
# 'Accept-Encoding':'gzip, deflate, br',
# 'Accept-Language':'zh-CN,zh;q=0.9',
# # 'accountType':'',
# # 'Authorization':'',
# 'Cache-Control':'no-cache',
# 'Connection':'keep-alive',
# 'Content-Length':'23',
# 'Content-Type':'application/json;charset=UTF-8',
# 'Cookie':'__jsluid_s=5ed40e75c539c1c2596927c0b3d482d9',
# 'Host':'fuwu.nhsa.gov.cn',
# 'Origin':'https://fuwu.nhsa.gov.cn',
# 'Pragma':'no-cache',
# 'Referer':'https://fuwu.nhsa.gov.cn/tps/portal/drug/list',
# # "refreshToken":'',
# 'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
# 'sec-ch-ua-mobile':'?0',
# 'sec-ch-ua-platform':'"Windows"',
# 'Sec-Fetch-Dest':'empty',
# 'Sec-Fetch-Mode':'cors',
# 'Sec-Fetch-Site':'same-origin',
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
# 'X-XSRF-TOKEN':'null'
# }
# data = {
#     'prntAdmdvs':'100000',
# }
# resp = requests.post(url, headers = headers, data = json.dumps(data))
# # print(resp.json())
# # print(type(resp.json()))
#
# lst1 = resp.json().get('data')
# for provincecode in lst1:               #遍历省份代码
#     # print(provincecode)
#     # print(type(provincecode))
#     Provincecode = provincecode.get('admdvs')
#     #print(Provincecode)



url_2 = "https://fuwu.nhsa.gov.cn/tps/web/mgr/pubonlnQury/getDrugPubonlnListPage"
headers_2 = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'accountType':'',
    'Authorization':'',
    'Connection':'keep-alive',
    'Content-Length':'209',
    'Content-Type':'application/json;charset=UTF-8',
    'Cookie':'__jsluid_s=2cdda488b6237fa562f839850db0ab62; UM_distinctid=17edd696596459-08910bb1392548-978153c-1fa400-17edd696597df4; CNZZDATA1279360307=1697884403-1644383123-https%253A%252F%252Ffuwu.nhsa.gov.cn%252F%7C1644383123',
    'Host':'fuwu.nhsa.gov.cn',
    'Origin':'https://fuwu.nhsa.gov.cn',
    'Referer':'https://fuwu.nhsa.gov.cn/tps/portal/drug/list',
    "refreshToken":'',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'X-XSRF-TOKEN':'null'
        }
data_2= {
    "current": "1",
    "drugCode": "",
    "drugName": "",
    "inda": "",
    "itemname": "",
    "maxPric": "",
    "minPric": "",
    "pricList": "",
    "pricOrder": "0",
    "prodentpName": "",
    "rpupProvCodeList": "110000",
    "size": "500",
    "uniquelyId": "anuyf0fm5use596y"
}
resp_2 = requests.post(url= url_2, headers= headers_2, data = json.dumps(data_2))
    #time.sleep(20)
    #print(resp_2.json())
dic2 = resp_2.json().get('data')
dic3 = dic2.get('records')
    # print(dic3)
    # print(type(dic3))
for dic in dic3:   #遍历获取药品所有信息
        # print(dic)
        # print(type(dic))
    Name = dic.get('drugName') #药品名称
    ProdentpName = dic.get('prodentpName') #中选企业
    Spec = dic.get('spec') #规格
    Pac = dic.get('pac') #包装
    Rute = dic.get('rute') #给药途径
    Dosform = dic.get('dosform')#剂型
    Inda = dic.get('inda') #适应症
    DrugCode = dic.get('drugCode') #药品代码
    Itemname = dic.get('itemname') #项目名称
    PubonlnPric = dic.get('pubonlnPric') #中选价(元)
    print(Dosform)
    print(Name)
    print(ProdentpName)
    print(Spec)
    print(Pac)
    print(Rute)
    print(Dosform)
    print(Inda)
    print(DrugCode)
    print(Itemname)
    print(PubonlnPric)
    sql = "insert into `国家组织集中采购药品中选价格查询（北京市）`(药品名称, 中选企业, 规格, 包装, 给药途径, 剂型, 适应症, 药品代码, 项目名称, `中选价(元)`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (str(Name), str(ProdentpName), str(Spec), str(Pac), str(Rute), str(Dosform), str(Inda), str(DrugCode), str(Itemname), str(PubonlnPric)))
    content.commit()
    print("成功存入数据库")



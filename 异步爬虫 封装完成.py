
import requests
import asyncio
import aiohttp
import aiofiles
import json



class Xi():
    def __init__(self):
        self.b_id = "4305713956"
        self.url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"'+ self.b_id +'"}'

    async def aiodownload(self,cid,b_id,title):
        data = {
            "book_id":b_id,
            "cid":f"{b_id}|{cid}",
            "need_bookinfo":1
        }
        data = json.dumps(data)
        url2 = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url2) as resp:
                dic = await resp.json()
                async with aiofiles.open(title, mode="w",encoding="utf-8") as f:
                    await f.write(dic["data"]["novel"]["content"])  # 写入小说内容


    async def getCatalog(self):
        resp = requests.get(self.url)
        tasks = []
        #print(resp.text)
        for a in resp.json()["data"]["novel"]["items"]: # 章节目录
            cid = a["cid"]
            title = a["title"]
            #print(cid,title)
            #准备异步任务
            tasks.append(self.aiodownload(cid=cid, b_id=self.b_id, title=title))
        await asyncio.wait(tasks)
        print("完成")

if __name__ == '__main__':
    work = Xi()
    asyncio.run(work.getCatalog())

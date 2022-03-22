# -*- coding = utf-8 -*-
# @Time :2022/3/3 13:57

import aiohttp
import asyncio
import aiofiles

urls = [
    "http://kr.shanghai-jiuxin.com/file/bizhi/20211216/txou21cum2u.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20211216/tuq3oc3stms.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20211216/pb4sa13r20q.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20211216/oqxpssxzxxx.jpg",
    "http://kr.shanghai-jiuxin.com/file/bizhi/20211216/eeq1r2irtib.jpg"

]


async def aiodownload(url):
    name = url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get(url) as resp:
                    with open(name, mode="wb") as f:   # 等价于requests中的resp.content   resp.text()=resp.text resp.json()=resp.json()
                        f.write(await resp.content.read())
                        print("完成")
                        break
            except:
                print("未完成")




async def main():
    tasks = []
    for url in urls:
        tasks.append(aiodownload(url))

    await asyncio.wait(tasks)








if __name__ == '__main__':
    asyncio.run(main())

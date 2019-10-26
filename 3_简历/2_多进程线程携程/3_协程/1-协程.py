import asyncio


async def get_html(url):
    print("start get ", url)
    await asyncio.sleep(2)
    print("end get ", url)


if __name__ == "__main__":
    li = ['url1', 'url2', 'url3']

    loop = asyncio.get_event_loop()  # 事件循环

    tasks = [get_html(url) for url in li]  # 创建任务列表

    loop.run_until_complete(asyncio.wait(tasks))  # 把任务列表放到loop

    loop.close()
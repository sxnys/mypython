import os
import asyncio
import random
import string
import time

async def write(s, n):
    if 'text' not in os.listdir():
        os.mkdir('text')
    asyncio.sleep(2)
    with open('text/{}.txt'.format(n), 'w', encoding='utf8') as f:
        f.write(s)

async def makeFiles(n):
    print('开始创建文件 {}'.format(n+1))
    start = time.perf_counter()
    s = ''.join(string.ascii_letters[random.randint(0, 51)] for _ in range(10000))
    await write(s, n + 1)
    print('文件 {} 创建完成，耗时 {:.3f} 秒\n'.format(
        n + 1, 
        time.perf_counter() - start
        ))


# 协程实现的异步 IO
if __name__ == '__main__':
    print('任务开始')
    start = time.perf_counter()

    tasks = [asyncio.ensure_future(makeFiles(i)) for i in range(100)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    print('任务结束，共耗时 {} 秒'.format(time.perf_counter() - start))



####################################################################################################################
#  同步 IO
####################################################################################################################

# def write1(s, n):
#     if 'text' not in os.listdir():
#         os.mkdir('text')
#     with open('text/{}.txt'.format(n), 'w', encoding='utf8') as f:
#         f.write(s)

# def makeFiles1(n):
#     print('开始创建文件 {}'.format(n+1))
#     start = time.perf_counter()
#     s = ''.join(string.ascii_letters[random.randint(0, 51)] for _ in range(1000000))
#     write1(s, n + 1)
#     print('文件 {} 创建完成，耗时 {:.3f} 秒\n'.format(
#         n + 1, 
#         time.perf_counter() - start
#         ))

# # 顺序执行
# if __name__ == '__main__':
#     print('任务开始')
#     start = time.perf_counter()

#     for i in range(10):
#         makeFiles1(i)

#     print('任务结束，共耗时 {} 秒'.format(time.perf_counter() - start))
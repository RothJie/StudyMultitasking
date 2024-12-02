from concurrent.futures import ThreadPoolExecutor
import blogs_spider
""" 
从线程池中拿数据的方法
# 第一种：pool.map(执行方法名，参数列表)  返回一个结果列表 
with ThreadPoolExecutor() as pool:
    htmls = pool.map(get_data, urls)
    for html in htm ls:  # 结果是有序的
        print(len(html))
"""

"""
从线程池中拿数据的方法
第二种：pool.submit(执行方法名,单个参数) 返回一个结果 可通过列表推导式完成所有操作
01.items()返回结果 直接遍历是有序的 用.result()查看内容
02.as_completed(futures)  处理后，优先把完成的结果返回，因此是无序的

with ThreadPoolExecutor() as pool: 
    futures = [pool.submit(parse_data, html) for html in htmls]

    for future in futures.items():      # 直接遍历有序
        print(future.result())

    for future in as_completed(futures): # as_completed()无序的
        print(future.result())
"""

# get_data
with ThreadPoolExecutor() as pool:
    results = pool.map(blogs_spider.get_data, blogs_spider.url_li)
    htmls = zip(blogs_spider.url_li, results)

    for url, html in htmls: #遍历列表直接查看结果
        print(url, len(html))

#parse_data
with ThreadPoolExecutor() as pool:
    resu_di = {}
    for url, html in htmls:
        future = pool.submit(blogs_spider.parse_data, html)
        resu_di[future] = url

    for future, url in resu_di.items(): # 字典转化为itmes对象是有序的
        print(url,future.result()) # 遍历后，用future.result()查看 结果

    # for future in as_completed(resu_di):  # 无序的
    #     url = resu_di[future]
    #     print(url, future.result()) #遍历后，用future.result()查看 结果
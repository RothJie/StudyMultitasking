import queue
import weatherSpider
import time
import random
import threading
import csv


def do_get_data(url_queue:queue.Queue,html_queue:queue.Queue):
    while True:
        url = url_queue.get()
        print(url)
        html = weatherSpider.dowload(url)
        html_queue.put(html)
        #输出日志
        print("生产者[{}]正在下载{}的网页，当前下载序列中还有{}个未完成".
              format(threading.current_thread().name,url,url_queue.qsize()))
        time.sleep(random.randint(1,3))  #设置时间停顿，保证数据下载

        if url_queue.empty():
            break

def do_paser_data(html_queue:queue.Queue):
    # 定义消费者具体执行方法
    while True:
        html = html_queue.get()
        results = weatherSpider.parse(html)
        writer.writerows(results)

        print("消费者[{}]正在解析数据，该网页中有{}个数据，当前还有{}页的数据待解析".
              format(threading.current_thread().name, len(results), html_queue.qsize()))
        time.sleep(random.randint(1, 3))

        if html_queue.empty():
            f_csv.close()
            break

if __name__ == '__main__':
    headers = ['date', 'week', 'high_temp', 'low_temp', 'weather_condition', 'wind_force']
    f_csv = open('weather3.csv', 'a', newline='\n', encoding='utf-8')
    writer = csv.writer(f_csv)  # 创建一个写入器
    writer.writerow(headers)

    # 创建两个空队列
    url_queue = queue.Queue()  # 暂存所有页的下载网址
    html_queue = queue.Queue()  # 暂存所有下载好的网页内容

    for url in weatherSpider.url_li:
        url_queue.put(url)

    for idx in range(5):
        # 搞出3个生产者线程
        t = threading.Thread(target=do_get_data,args=(url_queue,html_queue),
                             name=f'get_data{idx}') # 注意这里的args
        t.start()

    for idc in range(3):
        t = threading.Thread(target=do_paser_data,args=(html_queue, ),
                             name=f'parse_data{idc}')
        t.start()

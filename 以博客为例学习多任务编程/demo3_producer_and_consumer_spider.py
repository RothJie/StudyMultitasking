import queue
import blogs_spider
import time
import random
import threading

def do_get_data(url_queue:queue.Queue,html_queue:queue.Queue):
    # 定义生产者具体执行方法
    while True :
        url = url_queue.get()
        html = blogs_spider.get_data(url)
        html_queue.put(html)
        #输出日志
        print("生产者[{}]正在下载{}的网页，当前下载序列中还有{}个未完成".
              format(threading.current_thread().name,url,url_queue.qsize()))
        time.sleep(random.randint(1,3))  #设置时间停顿，保证数据下载

        if url_queue.empty():
            break


def do_parse_data(html_queue:queue.Queue,save_file):
    # 定义消费者具体执行方法
    while True:
        html = html_queue.get()
        results = blogs_spider.parse_data(html)
        for result in results:
            save_file.write(str(result)+'\n')

        print("消费者[{}]正在解析数据，该网页中有{}个数据，当前还有{}页的数据待解析".
              format(threading.current_thread().name,len(results),html_queue.qsize()))
        time.sleep(random.randint(1,3))

        if html_queue.empty():
            break


if __name__ == '__main__':
    # 创建两个空队列
    url_queue = queue.Queue() # 暂存所有页的下载网址
    html_queue = queue.Queue() # 暂存所有下载好的网页内容

    for url in blogs_spider.url_li:
        url_queue.put(url)

    for idx in range(3):
        # 搞出3个生产者线程
        t = threading.Thread(target=do_get_data,args=(url_queue,html_queue),
                             name=f'get_data{idx}') # 注意这里的args
        t.start()


    blogs_content = open('blogs_content.txt', 'a')
    for idx in range(2): # 搞出2个消费者线程
        t = threading.Thread(target=do_parse_data,args=(html_queue,blogs_content),
                             name=f'parse_data{idx}')
        t.start()

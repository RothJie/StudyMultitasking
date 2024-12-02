#实现一个单线程和多线程的对比，看看用时
import blogs_spider
import threading
import time

def single_thread():
    print('single_thread start')
    for url in blogs_spider.url_li:
        blogs_spider.get_data(url)
    print('single_thread end')

def multi_thread():
    print('multi_thread start')
    threads = []  # 线程存放列表
    for url in blogs_spider.url_li:
        threads.append(
            # 创建线程threading.Thread(target=目标函数名，args=(n, m, ))
            threading.Thread(target=blogs_spider.get_data, args=(url,))
        )

    for thread in threads:
        thread.start()  #启动线程

    for thread in threads:
        thread.join() # 等待线程执行完毕
    print('multi_thread end')

if __name__ == '__main__':
    start = time.time() # 开始时间
    single_thread()
    end = time.time() # 结束时间
    print('single_thread所需时间{}'.format(end - start))  # 计算时间差
    start = time.time()
    multi_thread()
    end = time.time()
    print('multi_thread所需时间{}'.format(end - start))




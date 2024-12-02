"""多线程
from threading import Thread

t = Thread(target=func,args=(100,))
t.start()
t,join

import Queue
q = queue.Queue()
q.put(item)
item = q.get()

from threading import Lock
lock = Lock()
with lock:
    # do something

from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor() as pool:
    # 方法一
    results = pool.map(func,[1,2,3])
    # 方法二
    future = pool.submit(func,1)
    result = future.result()
"""



"""多进程
from multiprocessing import Process

p = Process(target=func,args=('bob',)) 
p.start()
p.join() 

from multiprocessing import Queue
q = Queue
q.put(item)
item = q.get

from multiprocessing import Lock
lock = Lock()
with lock:
    # do something

from concurrent.futures import ProcessPoolExecutor
with ProcessPoolExecutor() as pool:
    # 方法一
    results = pool.map(func,[1,2,3])
    # 方法二
    future = pool.submit(func,1)
    result = future.result()
    
"""
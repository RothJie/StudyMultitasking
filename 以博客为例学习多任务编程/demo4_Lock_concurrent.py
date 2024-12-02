import threading
import time

lock = threading.Lock()

class Account:
    def __init__(self,balance):
        self.balance = balance

def draw(account,amount):
    with lock:
        if account.balance >= amount:
            time.sleep(0.1)
            print(f'{threading.current_thread().name}取钱成功！')
            # 获取当前线程的名字threading.current_thread().name
            account.balance -= amount
            print('当前余额为：{}'.format(account.balance))
        else:
            print(f'{threading.current_thread().name}取钱失败，余额不足！')

if __name__ == '__main__':
    account_ = Account(1000)
    ta = threading.Thread(name='ta',target=draw, args=(account_,800))
    tb = threading.Thread(name='tb',target=draw, args=(account_,800))
    ta.start()
    tb.start()

"""
用法1:try-finally模式
import threading

lock= threading.Lock()
lock.acquire()
try:
    do somethig
finally:
    lock.release()
    
用法2:_with 模式
import threading
lock = threading.Lock()
with lock:
    do something
"""


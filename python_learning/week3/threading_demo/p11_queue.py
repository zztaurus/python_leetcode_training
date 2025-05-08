import queue
import threading
import random
import time

class Producer(threading.Thread):
    def __init__(self, q, con, name):
        super().__init__()
        self.q = q
        self.con = con
        self.name = name
        self.running = True  # 线程退出标志
        print(f'Producer {self.name} Started')

    def run(self):
        while self.running:
            value = random.randint(0, 10)
            with self.con:
                # 使用 while 防止虚假唤醒
                while self.q.full():
                    print(f'Producer {self.name}: Queue is full, waiting...')
                    self.con.wait()  # 释放锁，等待唤醒
                # 队列未满，放入数据
                self.q.put(f'{self.name}: {value}')
                print(f'Producer {self.name} produced {value}')
                self.con.notify_all()  # 唤醒所有等待的线程
            time.sleep(1)
        print(f'Producer {self.name} exiting')

    def stop(self):
        self.running = False

class Consumer(threading.Thread):
    def __init__(self, q, con, name):
        super().__init__()
        self.q = q
        self.con = con
        self.name = name
        self.running = True
        print(f'Consumer {self.name} Started')

    def run(self):
        while self.running:
            with self.con:
                # 使用 while 防止虚假唤醒
                while self.q.empty():
                    print(f'Consumer {self.name}: Queue is empty, waiting...')
                    self.con.wait()
                # 队列非空，取出数据
                value = self.q.get()
                print(f'Consumer {self.name} consumed {value}')
                self.con.notify_all()
                self.q.task_done()  # 标记任务完成
            time.sleep(1)
        print(f'Consumer {self.name} exiting')

    def stop(self):
        self.running = False

if __name__ == '__main__':
    q = queue.Queue(maxsize=5)  # 设置队列最大容量
    con = threading.Condition()

    p1 = Producer(q, con, 'P1')
    p2 = Producer(q, con, 'P2')
    c1 = Consumer(q, con, 'C1')
    c2 = Consumer(q, con, 'C2')  # 添加更多消费者示例

    p1.start()
    p2.start()
    c1.start()
    c2.start()

    # 运行一段时间后停止线程
    time.sleep(5)
    
    p1.stop()
    p2.stop()
    c1.stop()
    c2.stop()

    p1.join()
    p2.join()
    c1.join()
    c2.join()

    print("All threads exited.")
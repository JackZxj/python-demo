import threading
import time


def print_name():
    while True:
        print("I am xiaoming")
        time.sleep(2)


def print_age():
    while True:
        print('I am 20 years old')
        time.sleep(3)


if __name__ == '__main__':
    try:
        # 使用threading模块，threading.Thread()创建线程，其中target参数值为需要调用的方法，同样将其他多个线程放在一个列表中，遍历这个列表就能同时执行里面的函数了
        threads = [threading.Thread(target=print_name),
                threading.Thread(target=print_age)]
        for t in threads:
            # 受主进程控制的多线程
            t.setDaemon(True)
            # 启动线程
            t.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stop now! Goodbye!")
    except:
        print('Error!')
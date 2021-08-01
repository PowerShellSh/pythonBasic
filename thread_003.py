import threading
import time
import logging

logging.basicConfig(
    level=logging.DEBUG, format='%(threadName)s: %(message)s'
)

def worker1():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')

def worker2():
    logging.debug('start')
    time.sleep(5)
    logging.debug('end')

if __name__ == '__main__':
    t1 = threading.Thread(target=worker1)
    # ５秒待たずにプログラムが終了する
    t1.setDaemon(True)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    print('started')
    # デーモン化したスレッドでもjoinすればちゃんと終了させる
    t1.join()
    # t2はjoinは不要だが、明示的に記載する場合もある
    t2.join()

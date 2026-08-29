import threading
import time
from threading import Thread
import os

def say_hello():
    print("Hello")
    print(f"pid: {os.getpid()}, tid: {threading.get_native_id()}") # thread id
    time.sleep(1)
    print("World")

threads = []

for i in range(10):
    th = Thread(target=say_hello)
    th.start()
    threads.append(th)

for t in threads:
    t.join()

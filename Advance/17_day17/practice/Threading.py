import threading
import time

def say_hello():
    print("Hello")
    print(threading.get_native_id())
    time.sleep(1)
    print("world")

threads = []

for _ in range(4):
    t = threading.Thread(target=say_hello)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
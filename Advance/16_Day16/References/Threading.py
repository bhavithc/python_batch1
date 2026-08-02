import threading
import time
import asyncio

def worker():
    current = threading.current_thread()
    print("Thread ID:", current.ident)
    print("Native OS thread ID:", current.native_id)
    for i in range(0, 10):
        print(f"Thread id {threading.current_thread().ident}, cnt: {i}")
        time.sleep(2)       




def main():
    print("Main Native OS thread ID:", threading.current_thread().native_id)
    # task = asyncio.create_task(worker())
    # print(f"async task id: {task}")
    # await task
    t1 = threading.Thread(target=worker)
    t1.start()
    t1.join()


if __name__ == "__main__":
    # asyncio.run(main())
    main()
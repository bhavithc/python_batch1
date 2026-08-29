import asyncio
import time
import threading
import os


async def say_hello():
    print("Hello")
    print(f"pid: {os.getpid()}, tid: {threading.get_native_id()}") # thread id
    await asyncio.sleep(1)
    print("World")

# asyncio.run(say_hello())

async def main():
    await asyncio.gather(
        say_hello(),
        say_hello(),
        say_hello(),
        say_hello(),
    )

asyncio.run(main())
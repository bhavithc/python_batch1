import asyncio
import threading

async def say_hello():
    print("Hello")
    print(threading.get_native_id())
    await asyncio.sleep(1)
    print("world")


# asyncio.run(say_hello())


async def main():
    results = await asyncio.gather(say_hello(), say_hello(), say_hello(), say_hello())
    print(results)

asyncio.run(main())

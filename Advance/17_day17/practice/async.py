import asyncio
import time

async def say_hello(name, delay):
    print("Hello")
    await asyncio.sleep(delay) 
    # time.sleep(1)
    print("world")
    return f"{name} result"

# h = say_hello()
# print(h)

# asyncio.run(say_hello())

async def main():
    results = await asyncio.gather(say_hello("one", 1), say_hello("two", 2), say_hello("three", 1), say_hello("four", 1))
    print(results)

asyncio.run(main())

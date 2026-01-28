"""Async allows the program to do something else while waiting for an operation to complete.
This is particularly useful for I/O-bound operations, such as network requests or file 
reading/writing, where waiting times can be significant.
In Python, asynchronous programming can be achieved using the `asyncio` library, 
which provides a framework for writing single-threaded concurrent code using the 
`async` and `await` keywords.

"""
import asyncio

import time 
async def greet():
    print("Hello")
    await asyncio.sleep(1)
    print("Goodby!!!")

asyncio.run(greet())




async def fetch_data(id, delay):
    print(f"Fetching data {id}")
    await asyncio.sleep(delay)
    print(f"Finished fetching data {id}")
    return f"Data {id}"

async def main():
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 1))
    task3 = asyncio.create_task(fetch_data(3, 3))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)

asyncio.run(main())

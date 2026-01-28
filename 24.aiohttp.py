"""aiohttp is an asynchronous HTTP client/server framework for Python.
It is built on top of the asyncio library and allows for non-blocking HTTP requests,
making it suitable for high-performance applications that require concurrent network operations.
With aiohttp, you can create both HTTP clients and servers, handle WebSocket connections,
and manage asynchronous tasks efficiently."""

import asyncio
import aiohttp

async def fetch():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.github.com") as response:
            print("Status:",response.status)
            data=await response.json()
            print("Response Data:",data)

asyncio.run(fetch())

    
#Example of aiohttp to fetch multiple posts concurrently

async def fetch_post(session, post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    async with session.get(url) as response:
        data = await response.json()
        print(f"Post {post_id} fetched")
        return data

async def main():
    async with aiohttp.ClientSession() as session:
        task1 = asyncio.create_task(fetch_post(session, 1))
        task2 = asyncio.create_task(fetch_post(session, 2))
        task3 = asyncio.create_task(fetch_post(session, 3))

        result1 = await task1
        result2 = await task2
        result3 = await task3

        print("All posts received")

asyncio.run(main())


#gather example
import asyncio
import aiohttp

async def fetch_post(session, post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    async with session.get(url) as response:
        data = await response.json()
        print(f"Post {post_id} fetched")
        return data

async def main():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            fetch_post(session, 1),
            fetch_post(session, 2),
            fetch_post(session, 3)
        )

        print("All posts received")

asyncio.run(main())

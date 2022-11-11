import asyncio
import datetime
from pprint import pprint
from aiohttp import ClientSession
from more_itertools import chunked

CHUNK_SIZE = 10

async def hello_world():
    while True:
        await asyncio.sleep(0.5)
        print('********************************************hello world')


async def get_person(people_id: int, session: ClientSession):
    print(f'start {people_id}')

    async with session.get(f'https://swapi.dev/api/people/{people_id}') as response:
        json_data = await response.json()

    print(f'end {people_id}')

    return json_data


async def get_people():
    async with ClientSession() as session:
        for chunk in chunked(range(1, 80), CHUNK_SIZE):
            coroutines = [get_person(people_id=i, session=session) for i in chunk]
            results = await asyncio.gather(*coroutines)

            for item in results:
                yield item


async def main():
    task = asyncio.create_task(hello_world())
    async for item in get_people():
        pprint(item)

    await task


start = datetime.datetime.now()
asyncio.run(main())
print(f'Working time: {datetime.datetime.now() - start}')

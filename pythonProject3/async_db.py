import asyncio
import datetime
from pprint import pprint
from aiohttp import ClientSession
from more_itertools import chunked
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import Column, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base

CHUNK_SIZE = 10

PG_DSN = DSN = 'postgresql+asyncpg://app:secret@localhost:5431/app'
engine = create_async_engine(PG_DSN)
Base = declarative_base()


class People(Base):
    id = Column(Integer, primary_key=True)
    json = Column(JSON)


async def get_person(people_id: int, session: ClientSession):
    print(f'start {people_id}')

    async with session.get(f'https://swapi.dev/api/people/{people_id}') as response:
        json_data = await response.json()

    print(f'end {people_id}')

    return json_data


async def get_people():
    async with engine.begin() as connection:
        await connection.urn_sync(Base.metadata.create_all)
        await connection.commit()

    Session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


    async with ClientSession() as session:
        for chunk in chunked(range(1, 80), CHUNK_SIZE):
            coroutines = [get_person(people_id=i, session=session) for i in chunk]
            results = await asyncio.gather(*coroutines)

            for item in results:
                yield item


async def main():
    async for item in get_people():
        pprint(item)


start = datetime.datetime.now()
asyncio.run(main())
print(f'Working time: {datetime.datetime.now() - start}')

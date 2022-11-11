import datetime
import requests
from pprint import pprint


def get_people(people_id):
    return requests.get(f'https://swapi.dev/api/people/{people_id}').json()


def main():
    for i in range(1, 11):
        print(f'id: {i}')
        pprint(get_people(people_id=i))


start = datetime.datetime.now()
main()
print(f'Working time: {datetime.datetime.now() - start}')

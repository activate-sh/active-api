from fastapi import FastAPI, status
from faker import Faker
from faker.providers import internet
from langdetect import detect
from typing import Optional

fake = Faker()
client = FastAPI()


@client.get('/', status_code=status.HTTP_200_OK)
async def main():
    return {
        'status': True,
        'programmer': 'amirali irvany',
        'rubika': '@active_api',
        'github': 'https://github.com/activate-sh',
        'email': 'dev.amirali.irvany@gmail.com'
    }


@client.get('/lang/{__text__}', status_code=status.HTTP_200_OK)
async def main(__text__: str):
    return {
        'status': True,
        'programmer': 'amirali irvany',
        'rubika': '@active_api',
        'result': detect(__text__)
    }


@client.get('/fake/{__type__}/{__range__}', status_code=status.HTTP_200_OK)
async def main(__type__: str, __range__: Optional[int]=10):
    '''Fake information generator'''
    __all__ = ('text', 'name', 'city', 'ip',
               'user-agent', 'emoji', 'email', 'date',
               'color', 'digit', 'address', 'letter', 'password')

    if __type__ == 'text':
        return {
            'status': True,
            'programmer': 'amirali irvany',
            'rubika': '@active_api',
            'type': __type__,
            'range': __range__,
            'results': fake.text(__range__)
        }


    elif __range__ > 999:
        return 'range is very larg'
    else:
        if __type__ == 'name':
            results = []
            for item in range(0, __range__):
                results.append(fake.name())

            return {
                'status': True,
                'programmer': 'amirali irvany',
                'rubika': '@active_api',
                'type': __type__,
                'range': __range__,
                'results': results
            }


        elif __type__ == 'city':
            results = []
            for item in range(0, __range__):
                results.append(fake.city())

            return {
                'status': True,
                'programmer': 'amirali irvany',
                'rubika': '@active_api',
                'type': __type__,
                'range': __range__,
                'results': results
            }


        elif __type__ == 'ip':
            results = []
            fake.add_provider(internet)
            for item in range(0, __range__):
                results.append(fake.ipv4_private())

            return {
                'status': True,
                'programmer': 'amirali irvany',
                'rubika': '@active_api',
                'type': __type__,
                'range': __range__,
                'results': results
            }


        elif __type__ == 'user-agent':
            results = []
            for item in range(0, __range__):
                results.append(fake.user_agent())

            return {
                'status': True,
                'programmer': 'amirali irvany',
                'rubika': '@active_api',
                'type': __type__,
                'range': __range__,
                'results': results
            }


        elif __type__ == 'emoji':
            results = []
            for item in range(0, __range__):
                results.append(fake.emoji())

            return {
                'status': True,
                'programmer': 'amirali irvany',
                'rubika': '@active_api',
                'type': __type__,
                'range': __range__,
                'results': results
            }


        elif __type__ == 'email':
            results = []
            for item in range(0, __range__):
                results.append(fake.ascii_email())

            return {
                'status': True,
                'programmer': 'amirali irvany',
                'rubika': '@active_api',
                'type': __type__,
                'range': __range__,
                'results': results
            }


        elif __type__ == 'date':
            results = []
            for item in range(0, __range__):
                results.append(fake.date())

            return {
                'status': True,
                'programmer': 'amirali irvany',
                'rubika': '@active_api',
                'type': __type__,
                'range': __range__,
                'results': results
            }


        elif __type__ == 'color':
            results = []
            for item in range(0, __range__):
                results.append(fake.color())

            return {
                'status': True,
                'programmer': 'amirali irvany',
                'rubika': '@active_api',
                'type': __type__,
                'range': __range__,
                'results': results
            }


        elif __type__ == 'digit':
            results = []
            for item in range(0, __range__):
                results.append(fake.random_digit())

            return {
                'status': True,
                'programmer': 'amirali irvany',
                'rubika': '@active_api',
                'type': __type__,
                'range': __range__,
                'results': results
            }


        elif __type__ == 'address':
            results = []
            for item in range(0, __range__):
                results.append(fake.address())

            return {
                'status': True,
                'programmer': 'amirali irvany',
                'rubika': '@active_api',
                'type': __type__,
                'range': __range__,
                'results': results
            }


        elif __type__ == 'letters':
            return {
                'status': True,
                'programmer': 'amirali irvany',
                'rubika': '@active_api',
                'type': __type__,
                'range': __range__,
                'results': fake.random_letters(__range__)
            }


        elif __type__ == 'password':
            results = []
            for item in range(0, __range__):
                results.append(fake.password())

            return {
                'status': True,
                'programmer': 'amirali irvany',
                'rubika': '@active_api',
                'type': __type__,
                'range': __range__,
                'results': results
            }

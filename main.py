from fastapi import FastAPI, status
from faker import Faker
from faker.providers import internet
from whois import whois
from typing import Optional

fake = Faker()
client = FastAPI()


@client.get('/', status_code=status.HTTP_200_OK)
async def main():
    return {
        'status': True,
        'dev': 'amirali irvany',
        'rubika': '@active_api',
        'github': 'https://github.com/activate-sh',
        'email': 'dev.amirali.irvany@gmail.com'
    }


parameter = [{'item': 'type'}, {'item': 'range'}]
@client.get('/fake/', status_code=status.HTTP_200_OK)
async def index_fake(type: str, count: Optional[int]=10):
    '''Fake information generator'''
    __all__ = ('text', 'name', 'city', 'ip',
               'user-agent', 'emoji', 'email', 'date',
               'color', 'digit', 'address', 'letter', 'password')

    __type__ = type
    __range__ = count
    if __type__ == 'text':
        return {
            'status': True,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
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
                'dev': 'amirali irvany',
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
                'dev': 'amirali irvany',
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
                'dev': 'amirali irvany',
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
                'dev': 'amirali irvany',
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
                'dev': 'amirali irvany',
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
                'dev': 'amirali irvany',
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
                'dev': 'amirali irvany',
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
                'dev': 'amirali irvany',
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
                'dev': 'amirali irvany',
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
                'dev': 'amirali irvany',
                'rubika': '@active_api',
                'type': __type__,
                'range': __range__,
                'results': results
            }


        elif __type__ == 'letters':
            return {
                'status': True,
                'dev': 'amirali irvany',
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
                'dev': 'amirali irvany',
                'rubika': '@active_api',
                'type': __type__,
                'range': __range__,
                'results': results
            }


        else:
            return {
                'detail': 'The information entered is not correct!',
                'see': __all__
            }


parameter = [{'item': 'domain'}]
@client.get('/domain/', status_code=status.HTTP_200_OK)
async def index_domain(domain: str):
    '''
    Get domain information such as:
        registrar
        updated date
        creation date
        expiration date
        name servers
        and...
    '''
    return whois(domain)

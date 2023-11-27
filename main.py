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


fonts = {
    0: ['𝔞', '𝔟', '𝔠', '𝔡', '𝔢', '𝔣', '𝔤', '𝔥', '𝔦', '𝔧', '𝔨', '𝔩', '𝔪', '𝔫', '𝔬', '𝔭', '𝔮', '𝔯', '𝔰', '𝔱', '𝔲', '𝔳', '𝔴', '𝔵', '𝔶', '𝔷'],
    1: ['𝓪', '𝓫', '𝓬', '𝓭', '𝓮', '𝓯', '𝓰', '𝓱', '𝓲', '𝓳', '𝓴', '𝓵', '𝓶', '𝓷', '𝓸', '𝓹', '𝓺', '𝓻', '𝓼', '𝓽', '𝓾', '𝓿', '𝔀', '𝔁', '𝔂', '𝔃'],
    2: ['𝒶', '𝒷', '𝒸', '𝒹', '𝑒', '𝒻', '𝑔', '𝒽', '𝒾', '𝒿', '𝓀', '𝓁', '𝓂', '𝓃', '𝑜', '𝓅', '𝓆', '𝓇', '𝓈', '𝓉', '𝓊', '𝓋', '𝓌', '𝓍', '𝓎', '𝓏'],
    3: ['𝕒', '𝕓', '𝕔', '𝕕', '𝕖', '𝕗', '𝕘', '𝕙', '𝕚', '𝕛', '𝕜', '𝕝', '𝕞', '𝕟', '𝕠', '𝕡', '𝕢', '𝕣', '𝕤', '𝕥', '𝕦', '𝕧', '𝕨', '𝕩', '𝕪', '𝕫'],
    4: ['ᴀ', 'ʙ', 'ᴄ', 'ᴅ', 'ᴇ', 'ꜰ', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ᴍ', 'ɴ', 'ᴏ', 'ᴘ', 'Q', 'ʀ', 'ꜱ', 'ᴛ', 'ᴜ', 'ᴠ', 'ᴡ', 'x', 'ʏ', 'ᴢ'],
    5: ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ', 'ⓕ', 'ⓖ', 'ⓗ', 'ⓘ', 'ⓙ', 'ⓚ', 'ⓛ', 'ⓜ', 'ⓝ', 'ⓞ', 'ⓟ', 'ⓠ', 'ⓡ', 'ⓢ', 'ⓣ', 'ⓤ', 'ⓥ', 'ⓦ', 'ⓧ', 'ⓨ', 'ⓩ'],
    6: ['𝐚', '𝐛', '𝐜', '𝐝', '𝐞', '𝐟', '𝐠', '𝐡', '𝐢', '𝐣', '𝐤', '𝐥', '𝐦', '𝐧', '𝐨', '𝐩', '𝐪', '𝐫', '𝐬', '𝐭', '𝐮', '𝐯', '𝐰', '𝐱', '𝐲', '𝐳'],
    7: ['𝗮', '𝗯', '𝗰', '𝗱', '𝗲', '𝗳', '𝗴', '𝗵', '𝗶', '𝗷', '𝗸', '𝗹', '𝗺', '𝗻', '𝗼', '𝗽', '𝗾', '𝗿', '𝘀', '𝘁', '𝘂', '𝘃', '𝘄', '𝘅', '𝘆', '𝘇'],
    8: ['𝓪', '𝓫', '𝓬', '𝓭', '𝓮', '𝓯', '𝓰', '𝓱', '𝓲', '𝓳', '𝓴', '𝓵', '𝓶', '𝓷', '𝓸', '𝓹', '𝓺', '𝓻', '𝓼', '𝓽', '𝓾', '𝓿', '𝔀', '𝔁', '𝔂', '𝔃'],
    9: ['𝒶', '𝒷', '𝒸', '𝒹', 'ℯ', '𝒻', '𝑔', '𝒽', '𝒾', '𝒿', '𝓀', '𝓁', '𝓂', '𝓃', 'ℴ', '𝓅', '𝓆', '𝓇', '𝓈', '𝓉', '𝓊', '𝓋', '𝓌', '𝓍', '𝓎', '𝓏'],
    10: ['𝒂', '𝒃', '𝒄', '𝒅', '𝒆', '𝒇', '𝒈', '𝒉', '𝒊', '𝒋', '𝒌', '𝒍', '𝒎', '𝒏', '𝒐', '𝒑', '𝒒', '𝒓', '𝒔', '𝒕', '𝒖', '𝒗', '𝒘', '𝒙', '𝒚', '𝒛'],
}

parameter = [{'item': 'text'}, {'item': 'number'}]
@client.get('/font/')
async def index_font(text: str):
    '''
    Font Generate
    Support Language: English
    Number of available fonts: 11
    '''
    converted_text = ''
    for count in range(0, len(fonts)):
        for char in text:
            if char.isalpha():
                char_index = ord(char.lower()) - 97
                converted_text += fonts[count][char_index]
            else:
                converted_text += char

        converted_text += '\n'
        results = converted_text.split('\n')[0:-1]

    return {
        'status': True,
        'dev': 'amirali irvany',
        'rubika': '@active_api',
        'results': results
    }

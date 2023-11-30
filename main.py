from fastapi import FastAPI, status
from faker import Faker
from faker.providers import internet
from whois import whois
from langdetect import detect
from jalali.Jalalian import jdate
from requests import post

fake = Faker()
client = FastAPI()


@client.get('/', status_code=status.HTTP_200_OK)
async def main():
    '''Information about me'''
    return {
        'status': 200,
        'dev': 'amirali irvany',
        'rubika': '@active_api',
        'github': 'https://github.com/activate-sh',
        'email': 'dev.amirali.irvany@gmail.com'
    }


parameters = [{'item': 'text'}]
@client.get('/lang/')
async def main(text: str):
    '''
    Language recognition service
    Examples of output:
        en
        fa
    '''
    return {
        'status': 200,
        'dev': 'amirali irvany',
        'rubika': '@active_api',
        'results': detect(text)
    }


@client.get('/time')
async def main():
    '''Accurate and complete display of Farsi date and time'''
    return {
        'status': 200,
        'dev': 'amirali irvany',
        'rubika': '@active_api',
        'results': jdate('H:i:s ,Y/n/j')
    }


parameters = [{'item': 'type'}, {'item': 'count'}]
@client.get('/fake/', status_code=status.HTTP_200_OK)
async def main(type: str, count: int):
    '''Fake information generator'''
    __all__ = (
        'name', 'city', 'ipv4', 'ipv6',
        'user-agent', 'emoji', 'email', 'date',
        'color', 'digit', 'address', 'letter', 'password'
    )
    __type__ = type
    __range__ = count

    if __type__ in __all__ and __range__ >= 999:
        return {
            'status': 400,
            'message': 'The information sent is not correct',
            'note': 'The value of \'count\' cannot be greater than 999'
        }


    elif __type__ == 'text' and __range__ <= 5:
        return {
            'status': 400,
            'message': 'The value of \'count\' cannot be less than 5'
        }


    elif __type__ == 'text' and __range__ > 99999:
        return {
            'status': 400,
            'message': 'The information sent is not correct',
            'note': 'The value of \'count\' cannot be greater than 99999'
        }


    elif __type__ == 'text':
        return {
            'status': 200,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
            'results': fake.text(__range__)
        }


    elif __type__ == 'name':
        results = []
        for item in range(0, __range__):
            results.append(fake.name())

        return {
            'status': 200,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
            'results': results
        }


    elif __type__ == 'city':
        results = []
        for item in range(0, __range__):
            results.append(fake.city())

        return {
            'status': 200,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
            'results': results
        }


    elif __type__ == 'ipv4':
        results = []
        fake.add_provider(internet)
        for item in range(0, __range__):
            results.append(fake.ipv4_private())

        return {
            'status': 200,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
            'results': results
        }


    elif __type__ == 'ipv6':
        results = []
        fake.add_provider(internet)
        for item in range(0, __range__):
            results.append(fake.ipv6())

        return {
            'status': 200,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
            'results': results
        }


    elif __type__ == 'user-agent':
        results = []
        for item in range(0, __range__):
            results.append(fake.user_agent())

        return {
            'status': 200,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
            'results': results
        }


    elif __type__ == 'emoji':
        results = []
        for item in range(0, __range__):
            results.append(fake.emoji())

        return {
            'status': 200,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
            'results': results
        }


    elif __type__ == 'email':
        results = []
        for item in range(0, __range__):
            results.append(fake.ascii_email())

        return {
            'status': 200,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
            'results': results
        }


    elif __type__ == 'date':
        results = []
        for item in range(0, __range__):
            results.append(fake.date())

        return {
            'status': 200,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
            'results': results
        }


    elif __type__ == 'color':
        results = []
        for item in range(0, __range__):
            results.append(fake.color())

        return {
            'status': 200,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
            'results': results
        }


    elif __type__ == 'digit':
        results = []
        for item in range(0, __range__):
            results.append(fake.random_digit())

        return {
            'status': 200,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
            'results': results
        }


    elif __type__ == 'address':
        results = []
        for item in range(0, __range__):
            results.append(fake.address())

        return {
            'status': 200,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
            'results': results
        }


    elif __type__ == 'letters':
        return {
            'status': 200,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
            'results': fake.random_letters(__range__)
        }


    elif __type__ == 'password':
        results = []
        for item in range(0, __range__):
            results.append(fake.password())

        return {
            'status': 200,
            'dev': 'amirali irvany',
            'rubika': '@active_api',
            'results': results
        }


    else:
        return {
            'detail': 'The information entered is not correct!',
            'see': __all__
        }



parameters = [{'item': 'url'}]
@client.get('/domain/', status_code=status.HTTP_200_OK)
async def main(url: str):
    '''
    Get domain information such as:
        registrar
        updated date
        creation date
        expiration date
        name servers
        and...
    '''
    return {
        'status': 200,
        'dev': 'amirali irvany',
        'rubika': '@active_api',
        'results': whois(url)
    }


fonts = {
    0: ['𝔞', '𝔟', '𝔠', '𝔡', '𝔢', '𝔣', '𝔤', '𝔥', '𝔦', '𝔧', '𝔨', '𝔩', '𝔪', '𝔫', '𝔬', '𝔭', '𝔮', '𝔯', '𝔰', '𝔱', '𝔲', '𝔳', '𝔴', '𝔵', '𝔶', '𝔷'],
    1: ['𝓪', '𝓫', '𝓬', '𝓭', '𝓮', '𝓯', '𝓰', '𝓱', '𝓲', '𝓳', '𝓴', '𝓵', '𝓶', '𝓷', '𝓸', '𝓹', '𝓺', '𝓻', '𝓼', '𝓽', '𝓾', '𝓿', '𝔀', '𝔁', '𝔂', '𝔃'],
    2: ['𝒶', '𝒷', '𝒸', '𝒹', '𝑒', '𝒻', '𝑔', '𝒽', '𝒾', '𝒿', '𝓀', '𝓁', '𝓂', '𝓃', '𝑜', '𝓅', '𝓆', '𝓇', '𝓈', '𝓉', '𝓊', '𝓋', '𝓌', '𝓍', '𝓎', '𝓏'],
    3: ['𝕒', '𝕓', '𝕔', '𝕕', '𝕖', '𝕗', '𝕘', '𝕙', '𝕚', '𝕛', '𝕜', '𝕝', '𝕞', '𝕟', '𝕠', '𝕡', '𝕢', '𝕣', '𝕤', '𝕥', '𝕦', '𝕧', '𝕨', '𝕩', '𝕪', '𝕫'],
    4: ['ᴀ', 'ʙ', 'ᴄ', 'ᴅ', 'ᴇ', 'ꜰ', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ᴍ', 'ɴ', 'ᴏ', 'ᴘ', 'Q', 'ʀ', 'ꜱ', 'ᴛ', 'ᴜ', 'ᴠ', 'ᴡ', 'x', 'ʏ', 'ᴢ'],
    5: ['ⓐ', 'ⓑ', 'ⓒ', 'ⓓ', 'ⓔ', 'ⓕ', 'ⓖ', 'ⓗ', 'ⓘ', 'ⓙ', 'ⓚ', 'ⓛ', 'ⓜ', 'ⓝ', 'ⓞ', 'ⓟ', 'ⓠ', 'ⓡ', 'ⓢ', 'ⓣ', 'ⓤ', 'ⓥ', 'ⓦ', 'ⓧ', 'ⓨ', 'ⓩ'],
    6: ['𝐚', '𝐛', '𝐜', '𝐝', '𝐞', '𝐟', '𝐠', '𝐡', '𝐢', '𝐣', '𝐤', '𝐥', '𝐦', '𝐧', '𝐨', '𝐩', '𝐪', '𝐫', '𝐬', '𝐭', '𝐮', '𝐯', '𝐰', '𝐱', '𝐲', '𝐳'],
    7: ['𝗮', '𝗯', '𝗰', '𝗱', '𝗲', '𝗳', '𝗴', '𝗵', '𝗶', '𝗷', '𝗸', '𝗹', '𝗺', '𝗻', '𝗼', '𝗽', '𝗾', '𝗿', '𝘀', '𝘁', '𝘂', '𝘃', '𝘄', '𝘅', '𝘆', '𝘇'],
    8: ['𝒂', '𝒃', '𝒄', '𝒅', '𝒆', '𝒇', '𝒈', '𝒉', '𝒊', '𝒋', '𝒌', '𝒍', '𝒎', '𝒏', '𝒐', '𝒑', '𝒒', '𝒓', '𝒔', '𝒕', '𝒖', '𝒗', '𝒘', '𝒙', '𝒚', '𝒛'],
    9: ['α', 'ɓ', '૮', '∂', 'ε', 'ƒ', 'ɠ', 'ɦ', 'เ', 'ʝ', 'ҡ', 'ℓ', 'ɱ', 'ɳ', 'σ', 'ρ', 'φ', '૨', 'ร', 'ƭ', 'µ', 'ѵ', 'ω', 'א', 'ყ', 'ƶ'],
    10: ['【A】', '【B】', '【C】', '【D】', '【E】', '【F】', '【G】', '【H】', '【I】', '【J】', '【K】', '【L】', '【M】', '【N】', '【O】', '【P】', '【Q】', '【R】', '【S】', '【T】', '【U】', '【V】', '【W】', '【X】', '【Y】', '【Z】'],
    11: ['⒜', '⒝', '⒞', '⒟', '⒠', '⒡', '⒢', '⒣', '⒤', '⒥', '⒦', '⒧', '⒨', '⒩', '⒪', '⒫', '⒬', '⒭', '⒮', '⒯', '⒰', '⒱', '⒲', '⒳', '⒴', '⒵'],
    12: ['ᵃ', 'ᵇ', 'ᶜ', 'ᵈ', 'ᵉ', 'ᶠ', 'ᵍ', 'ʰ', 'ᶦ', 'ʲ', 'ᵏ', 'ˡ', 'ᵐ', 'ⁿ', 'ᵒ', 'ᵖ', 'ᑫ', 'ʳ', 'ˢ', 'ᵗ', 'ᵘ', 'ᵛ', 'ʷ', 'ˣ', 'ʸ', 'ᶻ'],
    13: ['Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓘ', 'Ⓙ', 'Ⓚ', 'Ⓛ', 'Ⓜ', 'Ⓝ', 'Ⓞ', 'Ⓟ', 'Ⓠ', 'Ⓡ', 'Ⓢ', 'Ⓣ', 'Ⓤ', 'Ⓥ', 'Ⓦ', 'Ⓧ', 'Ⓨ', 'Ⓩ'],
    14: ['𝐀', '𝐁', '𝐂', '𝐃', '𝐄', '𝐅', '𝐆', '𝐇', '𝐈', '𝐉', '𝐊', '𝐋', '𝐌', '𝐍', '𝐎', '𝐏', '𝐐', '𝐑', '𝐒', '𝐓', '𝐔', '𝐕', '𝐖', '𝐗', '𝐘', '𝐙'],
    15: ['𝕬', '𝕭', '𝕮', '𝕯', '𝕰', '𝕱', '𝕲', '𝕳', '𝕿', '𝕴', '𝕶', '𝕷', '𝕸', '𝕹', '𝕺', '𝕻', '𝕼', '𝕽', '𝕾', '𝕵', '𝖀', '𝖁', '𝖂', '𝖃', '𝚼', '𝖅'],
    16: ['𝘼', '𝘽', '𝘾', '𝘿', '𝙀', '𝙁', '𝙂', '𝙃', '𝙄', '𝙅', '𝙆', '𝙇', '𝙈', '𝙉', '𝙊', '𝙋', '𝙌', '𝙍', '𝙎', '𝙏', '𝙐', '𝙑', '𝙒', '𝙓', '𝙔', '𝙕'],
    17: ['𝓐', '𝓑', '𝓒', '𝓓', '𝓔', '𝓕', '𝓖', '𝓗', '𝓘', '𝓙', '𝓚', '𝓛', '𝓜', '𝓝', '𝓞', '𝓟', '𝓠', '𝓡', '𝓢', '𝓣', '𝓤', '𝓥', '𝓦', '𝓧', '𝓨', '𝓩'],
    18: ['𝒜', 'ℬ', '𝒞', '𝒟', 'ℰ', 'ℱ', '𝒢', 'ℋ', 'ℐ', '𝒥', '𝒦', 'ℒ', 'ℳ', '𝒩', '𝒪', '𝒫', '𝒬', 'ℛ', '𝒮', '𝒯', '𝒰', '𝒱', '𝒲', '𝒳', '𝒴'],
    19: ['𝔸', '𝔹', 'ℂ', '𝔻', '𝔼', '𝔽', '𝔾', 'ℍ', '𝕀', '𝕁', '𝕂', '𝕃', '𝕄', 'ℕ', '𝕆', 'ℙ', 'ℚ', 'ℝ', '𝕊', '𝕋', '𝕌', '𝕍', '𝕎', '𝕏', '𝕐', 'ℤ'],
    20: ['Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｊ', 'Ｋ', 'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ', 'Ｐ', 'Ｑ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ', 'Ｖ', 'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ'],
    21: ['ᴀ', 'ʙ', 'ᴄ', 'ᴅ', 'ᴇ', 'ғ', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ᴍ', 'ɴ', 'ᴏ', 'ᴘ', 'ǫ', 'ʀ', 's', 'ᴛ', 'ᴜ', 'ᴠ', 'ᴡ', 'x', 'ʏ', 'ᴢ'],
    22: ['ᴬ', 'ᴮ', 'ᶜ', 'ᴰ', 'ᴱ', 'ᶠ', 'ᴳ', 'ᴴ', 'ᴵ', 'ᴶ', 'ᴷ', 'ᴸ', 'ᴹ', 'ᴺ', 'ᴼ', 'ᴾ', 'ᵟ', 'ᴿ', 'ˢ', 'ᵀ', 'ᵁ', 'ⱽ', 'ᵂ', 'ˣ', 'ᵞ', 'ᶻ'],
    23: ['卂', '乃', '匚', '刀', '乇', '下', '厶', '卄', '工', '丁', '长', '乚', '从', '𠘨', '口', '尸', '㔿', '尺', '丂', '丅', '凵', 'リ', '山', '乂', '丫', '乙'],
    24: ['『a』', '『b』', '『c』', '『d』', '『e』', '『f』', '『g』', '『h』', '『i』', '『j』', '『k』', '『l』', '『m』', '『n』', '『o』', '『p』', '『q』', '『r』', '『s』', '『t』', '『u』', '『v』', '『w』', '『x』', '『y』', '『z』'],
    25: ['a♥', 'b♥', 'c♥', 'd♥', 'e♥', 'f♥', 'g♥', 'h♥', 'i♥', 'j♥', 'k♥', 'l♥', 'm♥', 'n♥', 'o♥', 'p♥', 'q♥', 'r♥', 's♥', 't♥', 'u♥', 'v♥', 'w♥', 'x♥', 'y♥', 'z♥'],
    26: ['𝕒', 'β', 'ς', 'ᗪ', '𝑒', '𝔣', '𝔾', 'ℍ', 'ᶤ', '𝕁', 'Ҝ', 'ˡ', '𝕞', 'ή', '𝔬', 'Ⓟ', '𝐪', 'Ř', '𝓢', 'ţ', 'Ｕ', 'ᐯ', 'ω', '𝔵', 'ㄚ', 'ｚ'],
    27: ['Δ', '𝒷', 'ς', 'ⓓ', '𝒆', '𝓕', '𝑔', 'ⓗ', '𝐢', 'Ⓙ', '𝕜', 'ℓ', 'Ⓜ', 'Ň', 'Ø', '卩', 'ợ', '𝓇', 'ѕ', 'ｔ', '𝐮', '𝓋', '𝔀', '𝕩', 'у', '𝓩'],
    28: ['𝔸', 'ᵇ', 'ς', '𝔻', '𝒆', 'ƒ', 'ģ', 'ђ', '𝐢', '𝐉', '𝐤', 'ˡ', 'м', 'ℕ', 'ᵒ', 'ק', '𝐪', '𝔯', 'ร', 'ⓣ', 'ⓤ', 'ｖ', 'ᗯ', '𝕩', 'ⓨ', 'z'],
    29: ['α', '𝔟', 'ᑕ', 'đ', 'є', 'ғ', '𝐠', 'Ħ', 'Ｉ', '𝓙', 'к', 'Ĺ', 'м', '𝓝', 'Ｏ', 'ｐ', '𝓠', '𝓡', '𝔰', 'ţ', 'ù', '𝐕', '𝐰', 'χ', 'ｙ', 'ž'],
    30: ['𝒶', '𝒷', '𝔠', 'Ｄ', 'ｅ', 'ⓕ', 'g', 'Ⓗ', 'ί', 'ڶ', 'ⓚ', '𝓵', '𝕄', 'ή', '𝑜', 'Ƥ', '𝓠', '𝓻', '𝐒', 'ⓣ', 'Ｕ', 'ש', 'ｗ', 'ｘ', 'Ⓨ', 'Ž'],
    31: ['Ⓐ', '𝕓', '𝓬', 'Đ', 'ⓔ', '𝒇', 'g', '𝕙', 'เ', 'Ｊ', 'ᛕ', 'ᒪ', '𝓂', 'ⓝ', '𝕆', 'Ƥ', '𝓆', 'г', '𝐒', 'т', 'Ǘ', '𝐯', 'Ŵ', '𝐗', '𝕪', 'Ｚ'],
    32: ['ⓐ', '𝔹', '𝐂', 'Ⓓ', '𝒆', 'ℱ', 'Ⓖ', 'Ｈ', 'ᶤ', '𝐣', 'ｋ', 'Ⓛ', '𝓶', 'Ň', '𝐎', 'ⓟ', 'ⓠ', 'ʳ', 'Ŝ', 'ţ', 'Ữ', 'ｖ', '𝔴', 'Ж', '¥', 'ｚ'],
    33: ['𝒶', '𝔹', 'ｃ', 'ⓓ', '€', '𝔽', '𝐆', 'Ⓗ', 'ι', 'ｊ', 'Ｋ', 'ｌ', '𝕞', 'ℕ', 'Ｏ', '𝐏', 'Ɋ', 'я', '丂', '𝓣', 'υ', 'ᐯ', 'ⓦ', '乂', '𝕪', 'z'],
}


parameters = [{'item': 'text'}]
@client.get('/font/')
async def main(text: str):
    '''
    Font generator
    Support Language: English
    Number of available fonts: 34
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
        'status': 200,
        'dev': 'amirali irvany',
        'rubika': '@active_api',
        'results': results
    }


parameters = [{'item': 'text'}]
@client.post('/gpt/')
async def main(text: str):
    endpoint = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'
    headers = {
        'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
        'Connection': 'keep-alive', 'Accept': '*/*',
        'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/16.3.1 hw/iPhone12_5', 'Accept-Language': 'en',
        'Content-Type': 'application/json; charset=UTF-8'
    }
    data = {
        'message': text,
    }
    response = post(endpoint, json=data, headers=headers)
    return response.json()

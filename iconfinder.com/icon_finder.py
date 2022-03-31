import requests, re

def icon_search(q: str, type: str):
    small, big = list(), list()
    response = requests.get('https://www.iconfinder.com/search', headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
    }, params={
        'q': q,
    }).text

    urls = re.findall(r'https://cdn0\.iconfinder\.com/data/icons/[^"]+', response)
    for url in urls: small.append(url) if '128' in url else big.append(url)
    return {'stats': True, 'results': small} if type.lower() == 's' or type.lower() == 'small' else {'stats': True, 'results': big}



print(icon_search('python', 'small')) # Or print(icon_search('python', 'big'))

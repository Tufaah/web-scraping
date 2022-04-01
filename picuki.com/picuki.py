import requests, re

picuki = lambda user: ({'results': re.findall(r'title="(@[^"]+)', requests.get(f'https://www.picuki.com/search/{user}').text)})
print(picuki('nour'))
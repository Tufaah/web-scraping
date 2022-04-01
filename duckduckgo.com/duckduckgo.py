import requests, re

def duckduckgo(q: str):
        session = requests.session()
        main = session.get(f'https://duckduckgo.com/?q={q}&t=h_&ia=web', headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9', }).text

        vqd = re.search(r"vqd='([^']+)", main).group(1)
        search = session.get(
            f'https://links.duckduckgo.com/d.js?q={q}&l=us-en&s=0&a=h_&dl=en&ct=US&ss_mkt=us&vqd={vqd}&p_ent=&ex=-1&sp=1&biaexp=b&msvrtexp=b&nadse=b&stiaexp=b&uexp=a',
            headers={'referer': 'https://duckduckgo.com/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
                'accept-language': 'en-US,en;q=0.9', }).text

        javascript = re.search(r'DDG.pageLayout.load\(\'d\',([\s\S]*?)\);DDG\.duckbar\.load', search).group(1)
        data = re.findall(r'\{"a":"([^"]+)","ae":([^,]+),"c":"([^"]+)","d":"([^"]+)"', javascript)
        title = re.findall(r'"t":"([^"]+)', javascript)
        return {'stats': 'ok', 'results': [{'Title': title[i], 'Description': data[i][0], 'URL': data[i][2]} for i in range(len(data))]}


print(duckduckgo('python'))

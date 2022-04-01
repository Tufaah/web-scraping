from requests import get
from bs4 import BeautifulSoup


def yahoo(search :str, page :int):
    links, websites, titles, descriptions, data, done = [], [], [], [], [], []
    res = get(f'https://search.yahoo.com/search?p={search}&fr=sfp&fr2=p:s,v:sfp,m:sb-top&b={page if page == 1 else page + 7}',headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}).content

    soup = BeautifulSoup(res, "lxml")
    link = soup.find_all("a", {"class":"d-ib ls-05 fz-20 lh-26 td-hu tc va-bot mxw-100p"})
    for i in range(len(link)):
        links.append(link[i].attrs['href'])
        titles.append(link[i].text)

    website = soup.find_all("span", {"class":"d-ib p-abs t-0 l-0 fz-14 lh-20 fc-obsidian wr-bw ls-n pb-4"})
    for i in range(len(website)): websites.append(str(website[i].text))

    description = soup.find_all("span", {"class":"fc-falcon"})
    for i in range(len(description)): descriptions.append(str(description[i].text))
    for j in range(len(websites)): data.append(str(titles[j]).replace(str(websites[j]),''))

    for i in range(len(links)): done.append({'link':str(links[i]), 'title':str(data[i]), 'website':str(websites[i]).split()[0], 'description':str(descriptions[i]), })
    return {'results':0, 'data':f'Cant find results for: {search}'} if not done else {'results':len(links), 'data':done}


print(yahoo('python', 1))

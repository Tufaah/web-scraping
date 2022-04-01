import requests
from bs4 import BeautifulSoup

def telegram_channel_info(user: str):
    date_list, data_list, data_info_list, mix = [], [], [], {}
    result = requests.get(f"https://t.me/s/{user}/1")
    try:
        soup = BeautifulSoup(result.content, "html.parser")
        date = soup.find_all("span", {"class": "tgme_widget_message_meta"})
        for i in range(len(date)): date_list.append(date[i].find("time").attrs['datetime'])

        data = soup.find_all("span", {"class": "counter_value"})
        for i in range(len(data)): data_list.append(data[i].text)

        data_info = soup.find_all("span", {"class": "counter_type"})
        for i in range(len(data_info)): data_info_list.append(data_info[i].text)

        channel_date = str(date_list[0]).split('T')[0]
        for i in range(len(data_info_list)): mix[f'{data_info_list[i]}'] = f'{data_list[i]}'

        return {'stats': True, 'date': channel_date, 'info': mix}

    except IndexError: return {'stats': False, 'info': 'only channels!'}
    except: return {'stats': False, 'info': 'idk what the fuck is this error'}


print(telegram_channel_info("funny"))
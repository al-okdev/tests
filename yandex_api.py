import requests
import os


API_YANDEX_BASE_URL = "https://cloud-api.yandex.net/"
yandex_token = os.getenv('TOKEN_YA', '')
name_dir = 'MyDir'

def add_dir_disk(name_dir, token, API_YANDEX_BASE_URL):
    headers = {
        'accept': 'application/json',
        'authorization': f'OAuth {token}'
    }



    r = requests.put(API_YANDEX_BASE_URL + "v1/disk/resources",
                      params={'path': name_dir},
                      headers=headers)


    return r.status_code


# print(add_dir_disk(name_dir, yandex_token, API_YANDEX_BASE_URL))
import pytest
import os
import requests

API_YANDEX_BASE_URL = "https://cloud-api.yandex.net/"
yandex_token = os.getenv('TOKEN_YA', '')
name_dir = 'MyDir'


class TestApiYandexDiskPytest():
    def test_add_dir_disk(self):
        headers = {
            'accept': 'application/json',
            'authorization': f'OAuth {yandex_token}'
        }

        r = requests.put(API_YANDEX_BASE_URL + "v1/disk/resources",
                         params={'path': name_dir},
                         headers=headers)

        if r.status_code == 201:
            print("\nПапка успешно добавленна на диск\n")
            assert True
        else:
            assert False
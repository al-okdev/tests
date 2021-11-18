import os
import unittest
from yandex_api import add_dir_disk


API_YANDEX_BASE_URL = "https://cloud-api.yandex.net/"
yandex_token = os.getenv('TOKEN_YA', '')
name_dir = 'MyDir8'

class ApiYandexDiskTest(unittest.TestCase):
    def test_add_dir_disk(self):
        self.assertEqual(add_dir_disk(name_dir, yandex_token, API_YANDEX_BASE_URL), 201)
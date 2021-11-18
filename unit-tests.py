import unittest

from main import add_new_doc, delete_doc, get_doc_owner_name


class MyUnitTest(unittest.TestCase):
    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('181121', 'doc', 'Ivan', '5'), '5')

    def test_delete_doc(self):
        self.assertEqual(delete_doc('10006'), ('10006', True))

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name('11-2'), 'Геннадий Покемонов')
from test import mocks
import unittest
from unittest.mock import MagicMock, Mock, patch
import gnupg
from app.encrypt_file import Encrypted
import os

class TestCase(unittest.TestCase):

    @unittest.mock.patch.object(gnupg, 'GPG')
    def test_encrypt(self, gpg):
        gpg.return_value = mocks.GPG()
        path = os.path.join(os.path.dirname(__file__),'file.csv')
        status = Encrypted(path, path)
        print(status.status.ok)
        self.assertTrue(status.status.ok)
        self.assertEqual(status.status.status, 'Encryption Ok')
        self.assertEqual(status.status.stderr, 'KEY_CONSIDERED')

if __name__ == '__main__':
    unittest.main()
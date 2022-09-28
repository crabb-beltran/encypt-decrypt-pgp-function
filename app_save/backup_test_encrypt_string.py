from test import mocks
import unittest
from unittest.mock import MagicMock, Mock, patch
import gnupg
from app.encrypt_string import Encrypted


class TestCase(unittest.TestCase):

    @unittest.mock.patch.object(gnupg, 'GPG')
    def test_decrypt(self, gpg):
        gpg.return_value = mocks.GPG()
        ciphertext = None
        status = Encrypted(ciphertext)
        print(status.status.ok)
        self.assertTrue(status.status.ok)
        self.assertEqual(status.status.status, 'Encryption Ok')
        self.assertEqual(status.status.stderr, 'KEY_CONSIDERED')

if __name__ == '__main__':
    unittest.main()
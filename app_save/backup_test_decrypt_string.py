from test import mocks
import unittest
from unittest.mock import MagicMock, Mock, patch
import gnupg
from app.decrypt_string import Decrypted


class TestCase(unittest.TestCase):

    @unittest.mock.patch.object(gnupg, 'GPG')
    def test_decrypt(self, gpg):
        gpg.return_value = mocks.GPG()
        ciphertext = None
        passphrase = None
        status = Decrypted(ciphertext, passphrase)
        print(status.status.ok)
        self.assertTrue(status.status.ok)
        self.assertEqual(status.status.status, 'Encryption Ok')
        self.assertEqual(status.status.stderr, 'KEY_CONSIDERED')

if __name__ == '__main__':
    unittest.main()
import os
from test import mocks
import unittest
from unittest.mock import MagicMock, Mock, patch
import gnupg
from app.delete_keys import Deleted
import pytest

class TestCase(unittest.TestCase):

    @unittest.mock.patch.object(gnupg, 'GPG')
    def test_delete_keys(self, gpg):
        gpg.return_value = mocks.GPG()
        os.environ["PASSPHRASE"] = "321"
        self.status = Deleted()
        print(self.status.status)
        self.assertEqual(self.status.status,'Key Deleted')

    @unittest.mock.patch.object(gnupg, 'GPG')
    def test_delete_keys_except(self, gpg):
        gpg.return_value = mocks.GPG()
        os.environ["PASSPHRASE"] = "123"
        with pytest.raises(Exception) as exc_info:
            self.status = Deleted()

if __name__ == '__main__':
    unittest.main()
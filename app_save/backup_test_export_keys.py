import os
from test import mocks
import unittest
from unittest.mock import MagicMock, Mock, patch
import gnupg
from app.export_keys import Export
import pytest

class TestCase(unittest.TestCase):

    @unittest.mock.patch.object(gnupg, 'GPG')
    def test_export_keys(self, gpg):
        gpg.return_value = mocks.GPG()
        os.environ["PASSPHRASE"] = '321'
        self.status = Export()
        print(self.status.status)
        self.assertEqual(self.status.status, 'String Export Key Cotent')

    @unittest.mock.patch.object(gnupg, 'GPG')
    def test_export_keys_exception(self, gpg):
        gpg.return_value = mocks.GPG()
        os.environ["PASSPHRASE"] = '123'
        with pytest.raises(Exception) as exc_info:
            self.status = Export()

if __name__ == '__main__':
    unittest.main()
from test import mocks
import unittest
from unittest.mock import MagicMock, Mock, patch
import gnupg
from app.import_keys import Imported


class TestCase(unittest.TestCase):

    @unittest.mock.patch.object(gnupg, 'GPG')
    def test_import_keys(self, gpg):
        gpg.return_value = mocks.GPG()
        payload = None
        self.status = Imported(payload)
        print(self.status.status)
        self.assertEqual(self.status.status, 'Key Imported')


if __name__ == '__main__':
    unittest.main()
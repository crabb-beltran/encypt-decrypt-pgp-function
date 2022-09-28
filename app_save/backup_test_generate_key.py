from test import mocks
import unittest
from unittest.mock import MagicMock, Mock, patch
import gnupg
from app.generate_key import Generated


class TestCase(unittest.TestCase):

    @unittest.mock.patch.object(gnupg, 'GPG')
    def test_generate_keys(self, gpg):
        gpg.return_value = mocks.GPG()
        self.status = Generated()
        print(self.status.status)
        self.assertEqual(self.status.status, 'Generate Key ok')


if __name__ == '__main__':
    unittest.main()
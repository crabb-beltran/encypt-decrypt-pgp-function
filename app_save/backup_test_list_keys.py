from test import mocks
import unittest
from unittest.mock import MagicMock, Mock, patch
import gnupg
from app.list_keys import Listed


class TestCase(unittest.TestCase):

    @unittest.mock.patch.object(gnupg, 'GPG')
    def test_list_keys(self, gpg):
        gpg.return_value = mocks.GPG()
        self.status = Listed()
        print(self.status.status)
        self.assertEqual(self.status.status, 'List Keys')


if __name__ == '__main__':
    unittest.main()
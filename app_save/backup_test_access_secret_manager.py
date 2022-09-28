from test import mocks
import unittest
from unittest.mock import MagicMock, Mock, patch
from google.cloud import secretmanager
from app.access_secret_manager import AccesSM


class TestCase(unittest.TestCase):

    @unittest.mock.patch.object(secretmanager, 'SecretManagerServiceClient')
    def test_access_secret_version(self, _client):
        _client.return_value = mocks.SecretManagerServiceClient()
        status = AccesSM('type_key')
        print(status)
        self.assertIsNotNone(status)

if __name__ == '__main__':
    unittest.main()
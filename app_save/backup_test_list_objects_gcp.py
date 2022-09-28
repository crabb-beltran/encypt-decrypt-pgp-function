from test import mocks
import unittest
from unittest.mock import MagicMock, Mock, patch
from google.cloud import storage
from app.list_objects_gcp import ListObjects


class TestCase(unittest.TestCase):

    @unittest.mock.patch.object(storage, 'Client')
    def test_list_keys(self, storage_client):
        storage_client.return_value = mocks.StorageClientMock()
        self.bucket = None
        self.status = ListObjects(self.bucket)
        print(self.status.all_blobs)
        self.assertIsNotNone(self.status.all_blobs)


if __name__ == '__main__':
    unittest.main()
from test import mocks
import app.main_cloud_encrypt as m

from concurrent.futures import TimeoutError
from unittest.mock import MagicMock, Mock, patch
from google.cloud import storage, secretmanager
import gnupg
import base64
import unittest
import pytest
import os


class TestCase(unittest.TestCase):

    @unittest.mock.patch.object(storage, 'Client')
    @unittest.mock.patch.object(gnupg, 'GPG')
    @unittest.mock.patch.object(secretmanager, 'SecretManagerServiceClient')
    def test_main_event(self, secretmanager, gpg, storage_client):
        secretmanager.return_value = mocks.SecretManagerServiceClient()
        gpg.return_value = mocks.GPG()
        storage_client.return_value = mocks.StorageClientMock()
        mock_context = Mock()
        mock_context.event_id = '617187464135194'
        mock_context.timestamp = '2019-07-15T22:09:03.761Z'
        mock_context.resource = {
            'name': 'projects/my-project/topics/my-topic',
            'service': 'pubsub.googleapis.com',
            'type': 'type.googleapis.com/google.pubsub.v1.PubsubMessage',
        }
        name = 'test'
        data = {'data': base64.b64encode(name.encode())}
        status = m.main(data, mock_context)
        self.assertTrue(status)
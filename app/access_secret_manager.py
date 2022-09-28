from google.cloud import secretmanager
import os


class AccesSM:

    def __init__(self, type_key):
        self._type_key = type_key
        self._project_id = os.environ.get("ID_PROJECT_SECRET")
        self._version_id = 'latest'
        self.access_secret_version()

    def access_secret_version(self):

        self._client = secretmanager.SecretManagerServiceClient()

        self._name = f"projects/{self._project_id}/secrets/{self._type_key}/versions/{self._version_id}"

        self._response = self._client.access_secret_version(name=self._name)
        self.payload = self._response.payload.data.decode('UTF-8')
        return self.payload
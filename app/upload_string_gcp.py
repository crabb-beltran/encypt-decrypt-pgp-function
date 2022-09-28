from google.cloud import storage


class Transfer:

    def __init__(self, data_string, blob_name, bucket, project):
        self._data_string = str(data_string)
        self._blob_name = blob_name
        self._bucket = bucket
        self._project = project
        self._storage_client = storage.Client(project=self._project)
        self.upload_to_gcp()


    def upload_to_gcp(self):
        self._bucket = self._storage_client.bucket(self._bucket)
        self._blob = self._bucket.blob(self._blob_name)
        self._blob.upload_from_string(self._data_string)
from google.cloud import storage


class DeleteObject:

    def __init__(self, bucket_name, blob_name, project):
        self._bucket_name = bucket_name
        self._blob_name = blob_name
        self._project = project
        self._storage_client = storage.Client(project=self._project)
        self.delete_blob()


    def delete_blob(self):
        self._source_bucket = self._storage_client.bucket(self._bucket_name)
        self._source_bucket.delete_blob(self._blob_name)
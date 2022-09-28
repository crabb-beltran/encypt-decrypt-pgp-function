from google.cloud import storage


class MoveFile:

    def __init__(self, bucket_name, blob_name, destination_bucket_name, destination_blob_name, project):
        self._bucket_name = bucket_name
        self._destination_bucket_name = destination_bucket_name
        self._blob_name = blob_name
        self._destination_blob_name = destination_blob_name
        self._project = project
        self._storage_client = storage.Client(project=self._project)
        self.move_blob()


    def move_blob(self):
        self._source_bucket = self._storage_client.bucket(self._bucket_name)
        self._source_blob = self._source_bucket.blob(self._blob_name)
        self._destination_bucket = self._storage_client.bucket(self._destination_bucket_name)

        self._blob_copy = self._source_bucket.copy_blob(self._source_blob, self._destination_bucket, self._destination_blob_name)
        self._source_bucket.delete_blob(self._blob_name)
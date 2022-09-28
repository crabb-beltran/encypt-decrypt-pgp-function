from google.cloud import storage
import os

class Transfer:

    def __init__(self, path_file):
        self.path_in = path_file
        self.i = path_file.split('\\')
        self.path_out = self.i[-2]+'/'+self.i[-1]
        self._bucket = os.environ.get("BUCKET_NAME")
        self.login()


    def login(self):
        self._storage_client = storage.Client()
        self.upload_to_gcp()


    def upload_to_gcp(self):
        self._bucket = self._storage_client.get_bucket(self._bucket)
        self._blob = self._bucket.blob(self.path_out)
        self._blob.upload_from_filename(self.path_in)

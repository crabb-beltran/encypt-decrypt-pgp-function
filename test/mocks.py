from concurrent.futures import TimeoutError

class JobMock():

    def result(self, timeout=5):
        if timeout == 0:
            raise TimeoutError()
        return {
            'Nombre': 'Soy un mock'
        }

    def cancel(self):
        return True

    def close(self):
        return {
            'Nombre': 'Soy un mock'
        }

class MockEvent():
    data = ""
    def ack(self):
        return JobMock()

class StorageClientMock():

    def __init__(self):
        self.stream = JobMock()

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.stream.close()

    def bucket(self, argumento1):
        return BucketObj(0)

    def get_bucket(self, argumento):
        return JobMock()

    def upload_from_filename(self, argumento1):
        return JobMock()
        
    def list_blobs(self, _bucket):
        return list([BucketObj(0),BucketObj(1)])

class BucketObj():

    def __init__(self, value) -> None:
        self.value = value

    value = 0 
    name = "Test.pgp"

    def download_as_bytes(self):
        return FileObj(value=self.value)

    def delete(self):
        return True

    def blob(self,blob_name):
        return FileObj()

    def copy_blob(self, source_blob, destination_bucket, destination_blob):
        return True

    def delete_blob(self, blob_name):
        return True


class FileObj():

    value = 0
    def __init__(self, value = 0) -> None:
        self.value = value

    def decode(self, decode):
        if (self.value == 1):
            return '{"insertId",{"insertId",{"insertId",{"insertId",{"insertId"'
        else:
            return ''

    def upload_from_string(self, data_string):
        return True


class SecretManagerServiceClient():
    def access_secret_version(self, name):
        return ResponseServiceClient()

    def __init__(self):
        self.stream = JobMock()

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.stream.close()

class ResponseServiceClient():
    payload = None
    def __init__(self):
        self.payload = DataResponse()

class DataResponse():
    data = None
    def __init__(self):
        self.data = Data()

class Data():
    def decode(self, type):
        return ''

class GPG():
    def __init__(self):
        self.stream = JobMock()

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.stream.close()

    def decrypt_file(self, f, passphrase, output):
        return Status()

    def decrypt(self, encrypted_data, passphrase):
        return Status()

    def delete_keys(self, name_file_key, passphrase, secret):
        if (passphrase == '123'):
            raise Exception('Error with passphrase')
        self.status = 'Key Deleted'
        return self.status

    def encrypt_file(self, decrypted_data, recipients, output):
        return Status()

    def encrypt(self, decrypted_data, recipients):
        return Status()

    def export_keys(self, keyid, secret, passphrase):
        if (passphrase == '123'):
            raise Exception('Error with passphrase')
        self.status = 'String Export Key Cotent'
        return self.status

    def gen_key_input(self, name_real, name_comment, name_email, passphrase, key_type, key_length):
        self.input_data = None
        return self.input_data

    def gen_key(self, input_data):
        self.status = 'Generate Key ok'
        return self.status

    def import_keys(self, key_data):
        return Fingerprints()

    def trust_keys(self, fingerprints, trustlevel):
        self.status = 'Key Imported'
        return self.status

    def list_keys(self, type):
        self.status = 'List Keys'
        return self.status

class Fingerprints():
    def __init__(self):
        self.stream = JobMock()
        self.fingerprints = None


class Status():
    def __init__(self):
        self.stream = JobMock()
        self.ok = True
        self.status = 'Encrypt Ok / Decrypt Ok'
        self.stderr = 'KEY_CONSIDERED'
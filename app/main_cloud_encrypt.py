from access_secret_manager import AccesSM
from encrypt_string import Encrypted
from import_keys import Imported
from list_objects_gcp import ListObjects
from move_file_gcp import MoveFile
from upload_string_gcp import Transfer

import os


def main(event, context):

    print('Encryption process started.')
    
    access_m = AccesSM(type_key = os.environ.get("SECRET_ID_PB"))
    Imported(access_m.payload)
    bucket_in = os.environ.get("BUCKET_TO_ENCRYPT_IN")
    list_object = ListObjects(bucket = bucket_in)
    for _blob in list_object.all_blobs:
        print(_blob)
        _ciphertext = _blob.download_as_bytes()
        _ciphertext = _ciphertext.decode('utf-8')

        if not _ciphertext:
            status = False
        else:
            encrypted = Encrypted(ciphertext = _ciphertext)
            Transfer(data_string = encrypted.status, blob_name = _blob.name+'.pgp', bucket = os.environ.get("BUCKET_ENCRYPTED_OUT"), project = os.environ.get("PROJECT_ID_A"))
            MoveFile(bucket_name = bucket_in, blob_name = _blob.name, destination_bucket_name = os.environ.get("BUCKET_TO_ENCRYPT_OLD"), destination_blob_name = _blob.name, project = os.environ.get("PROJECT_ID_B"))
            status = True

    print('Encryption process finished.')
    return status
    
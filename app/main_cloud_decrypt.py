from access_secret_manager import AccesSM
from import_keys import Imported
from list_objects_gcp import ListObjects
from delete_object_gcs import DeleteObject
from decrypt_string import Decrypted
from move_file_gcp import MoveFile
from upload_string_gcp import Transfer

from time import sleep
import os


def main(event, context):

    sleep(10)
    client = os.environ.get("CLIENT")
    access_m = AccesSM(type_key = os.environ.get("SECRET_ID_PV"))
    Imported(access_m.payload)
    access_m = AccesSM(type_key = os.environ.get("SECRET_ID_PSW"))
    _passphrase = access_m.payload
    bucket_in = os.environ.get("BUCKET_TO_DECRYPT_IN")
    list_object = ListObjects(bucket = bucket_in)
    for _blob in list_object.all_blobs:

        if _blob.name.split('/')[0] == client:
            print(f'****{_blob.name}****')
            if _blob.name.split('/')[1] == '.aws-datasync':
                DeleteObject(bucket_name=bucket_in, blob_name=_blob.name, project=os.environ.get("PROJECT_ID_A"))
                print(f'****Carpeta de configuración eliminada. ----> {_blob.name}****')
            else:
                _ciphertext = _blob.download_as_bytes()
                if not _ciphertext:
                    status = False
                else:
                    if _blob.name[-4:] == '.gpg' or _blob.name[-4:] == '.pgp':
                            try:
                                decrypted = Decrypted(ciphertext = _ciphertext, passphrase = _passphrase)
                                if decrypted.status.ok == True:
                                    Transfer(data_string = decrypted.status, blob_name = _blob.name[:-4], bucket = os.environ.get("BUCKET_DECRYPTED_OUT"), project = os.environ.get("PROJECT_ID_B"))
                                    MoveFile(bucket_name = bucket_in, blob_name = _blob.name, destination_bucket_name = os.environ.get("BUCKET_TO_DECRYPT_OLD"), destination_blob_name = _blob.name, project = os.environ.get("PROJECT_ID_A"))
                                    status = True
                                    print(f'****Archivo procesado exitosamente. -----> {_blob.name}****')
                                print(f'****Archivo no procesado. -----> {_blob.name}****')
                            except:
                                print(f'****Archivo no procesado. -----> {_blob.name}****')
                    else:
                        print(f'****Tipo de archivo no permitido para descifrado. \tArchivo eliminado. -----> {_blob.name}****')
                        DeleteObject(bucket_name=bucket_in, blob_name=_blob.name, project=os.environ.get("PROJECT_ID_A"))

    return status
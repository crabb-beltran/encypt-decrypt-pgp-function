from list_files_onprimese import List_Files
from encrypt_file import Encrypted
from upload_file_gcp import Transfer
import os


def main():
    _home = os.getcwd()
    list_files = List_Files()
    for i in list_files._arr_list_file:
        j = i.split('\\')
        j = _home+'encrypted\\'+j[-1]+'.gpg'
        Encrypted(path_in=i, path_out=j)
        Transfer(path_file=j) # Esta función no aplica para el alcance del desarrollo.


if __name__ == "__main__":
    main()
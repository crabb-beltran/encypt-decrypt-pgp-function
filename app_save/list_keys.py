import gnupg
from pprint import pprint


class Listed:

    def __init__(self):
        self.type = True
        self.type_key_data = 'Private'
        self.list_keys()

    def list_keys(self):
        gpg = gnupg.GPG()

        for i in range(0,2):
            if i == 1:
                self.type = False
                self.type_key_data = 'Public'

            self.status = gpg.list_keys(self.type)
            print (self.type_key_data+' key:')
            pprint(self.status)
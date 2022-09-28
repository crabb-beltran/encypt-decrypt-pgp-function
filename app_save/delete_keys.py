from pprint import pprint
import gnupg
import os


class Deleted:

    def __init__(self):
        self._name_email = os.environ.get("NAME_EMAIL")
        self._passphrase = os.environ.get("PASSPHRASE")
        self._secret = True
        self.delete_keys()


    def delete_keys(self):
        gpg = gnupg.GPG()

        try:
            self.status = gpg.delete_keys(self._name_file_key, passphrase=self._passphrase,  secret=True)
            pprint(self.status)
        except:
            raise Exception('Failed to delete key private.')

        try:
            self.status = gpg.delete_keys(self._name_file_key, passphrase=None,  secret=False)
            pprint(self.status)
        except:
            raise Exception ('Failed to delete key public.')
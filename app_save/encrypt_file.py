import os
import gnupg

class Encrypted:

    def __init__(self, path_in, path_out):
        self.path_in = path_in
        self.path_out = path_out
        self._name_email = os.environ.get("NAME_EMAIL")
        self._passphrase = os.environ.get("PASSPHRASE")
        self.encrypt()


    def encrypt(self):
        gpg = gnupg.GPG()

        with open(self.path_in, 'rb') as self._decrypted_data:
            self.status = gpg.encrypt_file(self._decrypted_data, recipients=[self._name_email],output=self.path_out)

        print ('\nok: ', self.status.ok)
        print ('\nstatus: ', self.status.status)
        print ('\nstderr: ', self.status.stderr)
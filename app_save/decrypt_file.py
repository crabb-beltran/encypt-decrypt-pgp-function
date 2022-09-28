import os
import gnupg

class Decrypted:

    def __init__(self, path_in, path_out):
        self.path_in = path_in
        self.path_out = path_out
        self._passphrase = os.environ.get("PASSPHRASE")
        self.decrypt()

    def decrypt(self):
        gpg = gnupg.GPG()

        with open(self.path_in, 'rb') as f:
            self.status = gpg.decrypt_file(f, passphrase=self._passphrase, output=self.path_out)

        print ('\nok: ', self.status.ok)
        print ('\nstatus: ', self.status.status)
        print ('\nstderr: ', self.status.stderr)

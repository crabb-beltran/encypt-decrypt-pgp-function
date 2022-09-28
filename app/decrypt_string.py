import os
import gnupg

class Decrypted:

    def __init__(self, ciphertext, passphrase):
        self._encrypted_data = ciphertext
        self._passphrase = passphrase
        self._name_email = os.environ.get("NAME_EMAIL")
        self.decrypt()

    def decrypt(self):
        gpg = gnupg.GPG()

        self.status = gpg.decrypt(self._encrypted_data, passphrase = self._passphrase)

        print ('\nok: ', self.status.ok)
        print ('\nstatus: ', self.status.status)
        print ('\nstderr: ', self.status.stderr)
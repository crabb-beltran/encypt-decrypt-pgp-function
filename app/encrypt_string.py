import os
import gnupg

class Encrypted:

    def __init__(self, ciphertext):
        self._decrypted_data = ciphertext
        self._name_email = os.environ.get("NAME_EMAIL")
        self.encrypt()

    def encrypt(self):
        gpg = gnupg.GPG()

        self.status = gpg.encrypt(self._decrypted_data, recipients=self._name_email)

        print ('\nok: ', self.status.ok)
        print ('\nstatus: ', self.status.status)
        print ('\nstderr: ', self.status.stderr)
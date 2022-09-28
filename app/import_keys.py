import gnupg
import os


class Imported:

    def __init__(self, payload):
        self._key_data = payload
        self._name_email = os.environ.get("NAME_EMAIL")
        self.import_keys()


    def import_keys(self):
        gpg = gnupg.GPG()

        self.key = gpg.import_keys(self._key_data)
        self.status = gpg.trust_keys(self.key.fingerprints, trustlevel='TRUST_ULTIMATE')
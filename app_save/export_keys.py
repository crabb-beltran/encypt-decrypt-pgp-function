import gnupg
import os


class Export:

    def __init__(self):
        self.keyid = os.environ.get("KEY_ID")
        self.passphrase = os.environ.get("PASSPHRASE")
        self.path = os.path.join(os.path.dirname(__file__),'key_file_')
        self.file = 'private.asc'
        self.secret = True
        self.export_keys()

    def export_keys(self):
        gpg = gnupg.GPG()

        try:
            self.status = gpg.export_keys(self.keyid, secret = False, passphrase = None)
            with open(self.path+'pub.asc', 'w') as f:
                f.write(self.status)
        except:
            raise Exception('Failed to export key public.')

        try:
            self.status = gpg.export_keys(self.keyid, secret = True, passphrase = self.passphrase)
            with open(self.path+'priv.asc', 'w') as f:
                f.write(self.status)
        except:
            raise Exception('Failed to export key private.')

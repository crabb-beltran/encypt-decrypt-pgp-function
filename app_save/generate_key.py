import os
import gnupg


class Generated:

    def __init__(self):
        self.keyid = os.environ.get("KEY_ID")
        self.passphrase = os.environ.get("PASSPHRASE")
        self.name_email = os.environ.get("NAME_EMAIL")
        self.name_real = os.environ.get("NAME_REAL")
        self.name_comment = os.environ.get("NAME_COMMENT")
        self.key_type = "RSA"
        self.key_length = 4096
        self.generate_keys()

    def generate_keys(self):
        gpg = gnupg.GPG()

        self.input_data = gpg.gen_key_input(
            name_real = self.name_real,
            name_comment = self.name_comment,
            name_email = self.name_email,
            passphrase = self.passphrase,
            key_type = self.key_type,
            key_length = self.key_length)

        self.status = gpg.gen_key(self.input_data)
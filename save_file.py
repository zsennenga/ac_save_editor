import os

from crypto.checksum_wrapper import ChecksumWrapper
from crypto.constant.revisions import Revisions
from crypto.crypto_wrapper import CryptoWrapper
from file_name import FileName


class SaveFile:
    def __init__(
            self,
            file_name: FileName,
            raw_data: bytes,
            header_file_name: FileName,
            raw_header: bytes
    ):
        self.file_name = file_name
        self.header_file_name = header_file_name

        self.raw_data = raw_data
        self.raw_header = raw_header

        self.decrypted_raw = CryptoWrapper.decrypt(
            header=self.raw_header,
            file_bytes=self.raw_data,
        )

        self.file_info = Revisions.get_file_info(
            file_name=self.file_name,
            decrypted_data=self.decrypted_raw,
        )

        ChecksumWrapper.verify_hashes(
            file_info=self.file_info,
            data=self.decrypted_raw,
        )

    @classmethod
    def read_file_bytes(cls, root_path, filename):
        with open(os.path.join(root_path, filename), "rb") as f:
            return f.read()

    @classmethod
    def read(cls, path: str, file_name: FileName, header_file_name: FileName):
        return SaveFile(
            file_name=file_name,
            raw_data=cls.read_file_bytes(path, file_name.value),
            header_file_name=header_file_name,
            raw_header=cls.read_file_bytes(path, header_file_name.value)
        )

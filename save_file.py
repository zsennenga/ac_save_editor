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
    def read_file_bytes(cls, root_path: str, filename: FileName) -> bytes:
        with open(os.path.join(root_path, filename.value), "rb") as f:
            return f.read()

    @classmethod
    def write_file_bytes(cls, root_path: str, filename: FileName, data: bytes) -> None:
        if not os.path.exists(root_path):
            os.mkdir(root_path)
        with open(os.path.join(root_path, filename.value), "wb") as f:
            f.write(data)

    @classmethod
    def read(cls, path: str, file_name: FileName, header_file_name: FileName) -> 'SaveFile':
        return SaveFile(
            file_name=file_name,
            raw_data=cls.read_file_bytes(path, file_name),
            header_file_name=header_file_name,
            raw_header=cls.read_file_bytes(path, header_file_name),
        )

    def save(self, path) -> None:
        decrypted_with_checksums = ChecksumWrapper.update_hashes(self.file_info, self.decrypted_raw)
        (header_data, enc_data) = CryptoWrapper.encrypt(decrypted_with_checksums)
        self.write_file_bytes(path, self.header_file_name, header_data)
        self.write_file_bytes(path, self.file_name, enc_data)

    def save_decrypted(self, path):
        decrypted_with_checksums = ChecksumWrapper.update_hashes(self.file_info, self.decrypted_raw)

        self.write_file_bytes(path, self.file_name, decrypted_with_checksums)

import mmh3

import numpy as np

from crypto.constant.file_info import FileInfo


class ChecksumWrapper:
    @classmethod
    def get_hash_bytes(cls, data_to_hash):
        new_hash = np.uint32(mmh3.hash(data_to_hash)).tobytes()
        return np.frombuffer(new_hash, np.int8)

    @classmethod
    def update_hashes(cls, file_info: FileInfo, data: bytes):
        data_mutable = bytearray(data)
        for hash_region in file_info.hash_regions:
            data_to_hash = data[hash_region.begin_offset: hash_region.end_offset]
            new_hash = cls.get_hash_bytes(data_to_hash)
            for i in range(len(new_hash)):
                data_mutable[hash_region.hash_offset + i] = new_hash[i]

        return bytes(data_mutable)

    @classmethod
    def verify_hashes(cls, file_info: FileInfo, data: bytes):
        for hash_region in file_info.hash_regions:
            read_hash = np.frombuffer(data[hash_region.hash_offset: hash_region.hash_end_offset], np.int32)[0]
            data_to_hash = data[hash_region.begin_offset: hash_region.end_offset]

            if read_hash != mmh3.hash(data_to_hash):
                raise Exception("Hash does not match!")

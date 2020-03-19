from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

import numpy as np

from crypto.constant.file_info import FileInfo
from crypto.constant.hash_info import HashSets
from file_name import FileName


@dataclass
class Revision:
    magic_number: List
    file_info: Dict[FileName, FileInfo]


class Revisions(Enum):
    v1_0_0 = Revision(
        magic_number=[
            np.uint32(0x67),
            np.uint32(0x6F),
            np.uint32(0x02),
            np.uint32(0x02),
        ],
        file_info={
            FileName.MAIN: FileInfo(
                name=FileName.MAIN,
                header_file=FileName.MAIN_HEADER,
                size=0xAC0938,
                hash_regions=HashSets.v1_0_0.value[FileName.MAIN]
            ),
            FileName.PERSONAL: FileInfo(
                name=FileName.PERSONAL,
                header_file=FileName.PERSONAL_HEADER,
                size=0x6BC50,
                hash_regions=HashSets.v1_0_0.value[FileName.PERSONAL]
            ),
            FileName.POSTBOX: FileInfo(
                name=FileName.POSTBOX,
                header_file=FileName.POSTBOX_HEADER,
                size=0xB44580,
                hash_regions=HashSets.v1_0_0.value[FileName.POSTBOX]
            ),
            FileName.PHOTO_STUDIO: FileInfo(
                name=FileName.PHOTO_STUDIO,
                header_file=FileName.PHOTO_STUDIO_HEADER,
                size=0x263B4,
                hash_regions=HashSets.v1_0_0.value[FileName.PHOTO_STUDIO]
            ),
            FileName.PROFILE: FileInfo(
                name=FileName.PROFILE,
                header_file=FileName.PROFILE_HEADER,
                size=0x69508,
                hash_regions=HashSets.v1_0_0.value[FileName.PROFILE]
            )
        }
    )

    v1_1_0 = Revision(
        magic_number=[
            np.uint32(0x6D),
            np.uint32(0x78),
            np.uint32(0x02),
            np.uint32(0x00010002),
        ],
        file_info={
            FileName.MAIN: FileInfo(
                name=FileName.MAIN,
                header_file=FileName.MAIN_HEADER,
                size=0xAC2AA0,
                hash_regions=HashSets.v1_1_0.value[FileName.MAIN]
            ),
            FileName.PERSONAL: FileInfo(
                name=FileName.PERSONAL,
                header_file=FileName.PERSONAL_HEADER,
                size=0x6BED0,
                hash_regions=HashSets.v1_1_0.value[FileName.PERSONAL]
            ),
            FileName.POSTBOX: FileInfo(
                name=FileName.POSTBOX,
                header_file=FileName.POSTBOX_HEADER,
                size=0xB44590,
                hash_regions=HashSets.v1_1_0.value[FileName.POSTBOX]
            ),
            FileName.PHOTO_STUDIO: FileInfo(
                name=FileName.PHOTO_STUDIO,
                header_file=FileName.POSTBOX_HEADER,
                size=0x263C0,
                hash_regions=HashSets.v1_1_0.value[FileName.PHOTO_STUDIO]
            ),
            FileName.PROFILE: FileInfo(
                name=FileName.PROFILE,
                header_file=FileName.PROFILE_HEADER,
                size=0x69560,
                hash_regions=HashSets.v1_1_0.value[FileName.PROFILE]
            )
        }
    )

    @classmethod
    def get_file_info(cls, file_name: FileName, decrypted_data: bytes) -> FileInfo:
        magic_bytes = decrypted_data[:32]

        for enum_key in cls:
            as_np_array = np.frombuffer(magic_bytes, np.uint32)[:4]
            if np.array_equal(enum_key.value.magic_number, as_np_array):
                return enum_key.value.file_info[file_name]

        raise Exception("Unable to identify file constants")

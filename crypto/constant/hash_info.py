from dataclasses import dataclass
from enum import Enum

from file_name import FileName


@dataclass
class HashRegion:
    hash_offset: int
    begin_offset: int
    size: int

    @property
    def end_offset(self) -> int:
        return self.begin_offset + self.size

    @property
    def hash_end_offset(self) -> int:
        return self.begin_offset + 8


class HashSets(Enum):
    v1_0_0 = {
        FileName.MAIN: [
            HashRegion(0x000108, 0x00010C, 0x1D6D4C),
            HashRegion(0x1D6E58, 0x1D6E5C, 0x323384),
            HashRegion(0x4FA2E8, 0x4FA2EC, 0x035AC4),
            HashRegion(0x52FDB0, 0x52FDB4, 0x03607C),
            HashRegion(0x565F38, 0x565F3C, 0x035AC4),
            HashRegion(0x59BA00, 0x59BA04, 0x03607C),
            HashRegion(0x5D1B88, 0x5D1B8C, 0x035AC4),
            HashRegion(0x607650, 0x607654, 0x03607C),
            HashRegion(0x63D7D8, 0x63D7DC, 0x035AC4),
            HashRegion(0x6732A0, 0x6732A4, 0x03607C),
            HashRegion(0x6A9428, 0x6A942C, 0x035AC4),
            HashRegion(0x6DEEF0, 0x6DEEF4, 0x03607C),
            HashRegion(0x715078, 0x71507C, 0x035AC4),
            HashRegion(0x74AB40, 0x74AB44, 0x03607C),
            HashRegion(0x780CC8, 0x780CCC, 0x035AC4),
            HashRegion(0x7B6790, 0x7B6794, 0x03607C),
            HashRegion(0x7EC918, 0x7EC91C, 0x035AC4),
            HashRegion(0x8223E0, 0x8223E4, 0x03607C),
            HashRegion(0x858460, 0x858464, 0x2684D4),
        ],
        FileName.PERSONAL: [
            HashRegion(0x00108, 0x0010C, 0x35AC4),
            HashRegion(0x35BD0, 0x35BD4, 0x3607C),
        ],
        FileName.POSTBOX: [
            HashRegion(0x000100, 0x00104, 0xB4447C),
        ],
        FileName.PHOTO_STUDIO: [
            HashRegion(0x000100, 0x00104, 0x262B0),
        ],
        FileName.PROFILE: [
            HashRegion(0x000100, 0x00104, 0x69404),
        ]
    }
    v1_1_0 = {
        FileName.MAIN: [
            HashRegion(0x000110, 0x000114, 0x1D6D5C),
            HashRegion(0x1D6E70, 0x1D6E74, 0x323C0C),
            HashRegion(0x4FAB90, 0x4FAB94, 0x035AFC),
            HashRegion(0x530690, 0x530694, 0x0362BC),
            HashRegion(0x566A60, 0x566A64, 0x035AFC),
            HashRegion(0x59C560, 0x59C564, 0x0362BC),
            HashRegion(0x5D2930, 0x5D2934, 0x035AFC),
            HashRegion(0x608430, 0x608434, 0x0362BC),
            HashRegion(0x63E800, 0x63E804, 0x035AFC),
            HashRegion(0x674300, 0x674304, 0x0362BC),
            HashRegion(0x6AA6D0, 0x6AA6D4, 0x035AFC),
            HashRegion(0x6E01D0, 0x6E01D4, 0x0362BC),
            HashRegion(0x7165A0, 0x7165A4, 0x035AFC),
            HashRegion(0x74C0A0, 0x74C0A4, 0x0362BC),
            HashRegion(0x782470, 0x782474, 0x035AFC),
            HashRegion(0x7B7F70, 0x7B7F74, 0x0362BC),
            HashRegion(0x7EE340, 0x7EE344, 0x035AFC),
            HashRegion(0x823E40, 0x823E44, 0x0362BC),
            HashRegion(0x85A100, 0x85A104, 0x26899C),
        ],
        FileName.PERSONAL: [
            HashRegion(0x00110, 0x00114, 0x35AFC),
            HashRegion(0x35C10, 0x35C14, 0x362BC),
        ],
        FileName.POSTBOX: [
            HashRegion(0x000100, 0x00104, 0xB4448C),
        ],
        FileName.PHOTO_STUDIO: [
            HashRegion(0x000100, 0x00104, 0x262BC),
        ],
        FileName.PROFILE: [
            HashRegion(0x000100, 0x00104, 0x6945C),
        ]
    }

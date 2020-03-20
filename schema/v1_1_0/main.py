from construct import *

Struct(
    "header" / Array(0x110, Byte),
    "checksum0" / Int32ul,
    "segment0" / Array(0x1d6d5c, Byte),
    "checksum1" / Int32ul,
    "segment1" / Array(0x323c0c, Byte),
    "checksum2" / Int32ul,
    "segment2" / Array(0x35afc, Byte),
    "checksum3" / Int32ul,
    "segment3" / Array(0x362bc, Byte),
    "checksum4" / Int32ul,
    "segment4" / Array(0x35afc, Byte),
    "checksum5" / Int32ul,
    "segment5" / Array(0x362bc, Byte),
    "checksum6" / Int32ul,
    "segment6" / Array(0x35afc, Byte),
    "checksum7" / Int32ul,
    "segment7" / Array(0x362bc, Byte),
    "checksum8" / Int32ul,
    "segment8" / Array(0x35afc, Byte),
    "checksum9" / Int32ul,
    "segment9" / Array(0x362bc, Byte),
    "checksum10" / Int32ul,
    "segment10" / Array(0x35afc, Byte),
    "checksum11" / Int32ul,
    "segment11" / Array(0x362bc, Byte),
    "checksum12" / Int32ul,
    "segment12" / Array(0x35afc, Byte),
    "checksum13" / Int32ul,
    "segment13" / Array(0x362bc, Byte),
    "checksum14" / Int32ul,
    "segment14" / Array(0x35afc, Byte),
    "checksum15" / Int32ul,
    "segment15" / Array(0x362bc, Byte),
    "checksum16" / Int32ul,
    "segment16" / Array(0x35afc, Byte),
    "checksum17" / Int32ul,
    "segment17" / Array(0x362bc, Byte),
    "checksum18" / Int32ul,
    "segment18" / Array(0x26899c, Byte),
)

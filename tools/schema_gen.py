from crypto.constant.hash_info import HashSets

for (file_name, hash_regions) in HashSets.v1_1_0.value.items():
    print(file_name)

    print("Struct(")
    print(
        f'"header" / Array({hex(hash_regions[0].hash_offset)}, Byte),'
    )
    for (i, hash_region) in enumerate(hash_regions):
        print(f'"checksum{i}" / Int32ul,')
        print(f'"segment{i}" / Array({hex(hash_region.size)}, Byte),')

    print(")")

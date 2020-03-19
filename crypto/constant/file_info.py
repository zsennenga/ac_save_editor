from dataclasses import dataclass
from typing import List

from crypto.constant.hash_info import HashRegion
from file_name import FileName


@dataclass
class FileInfo:
    name: FileName
    header_file: FileName
    size: int
    hash_regions: List[HashRegion]

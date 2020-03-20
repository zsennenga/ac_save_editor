import os
from typing import List

from file_name import FileName
from save_file import SaveFile
from villager_save import VillagerSave


class ACSave:
    def __init__(
            self,
            root_path: str,
            main: SaveFile,
            villagers: List[VillagerSave]
    ):
        self.root_path = root_path
        self.main = main
        self.villagers = villagers

    @classmethod
    def build(cls, path):
        villager_paths = [
            obj for obj in os.listdir(path)
            if os.path.isdir(os.path.join(path, obj)) and obj.startswith("villager")
        ]

        villager_ids = []
        for villager in villager_paths:
            parsed = villager.replace("villager", "")
            if 0 > int(parsed) > 8:
                raise Exception("Bad villager path")

            villager_ids.append(parsed)

        return ACSave(
            root_path=path,
            main=SaveFile.read(
                file_name=FileName.MAIN,
                header_file_name=FileName.MAIN_HEADER,
                path=path,
            ),
            villagers=[
                VillagerSave.build(path, villager_id)
                for villager_id in villager_ids
            ]
        )


    def save(self, path: str):
        self.main.save(path)
        for villager in self.villagers:
            villager.save(path)

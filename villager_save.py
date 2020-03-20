import os

from file_name import FileName
from save_file import SaveFile


class VillagerSave:
    def __init__(
            self,
            path: str,
            villager_id: str,
            personal: SaveFile,
            postbox: SaveFile,
            photo_studio: SaveFile,
            profile: SaveFile
    ):
        self.path = path
        self.villager_id = villager_id
        self.personal = personal
        self.postbox = postbox
        self.photo_studio = photo_studio
        self.profile = profile

    @classmethod
    def get_villager_path(cls, path: str, villager_id: str) -> str:
        return os.path.join(path, "villager" + villager_id)

    @classmethod
    def build(cls, path: str, villager_id: str) -> 'VillagerSave':
        villager_path = cls.get_villager_path(path, villager_id)
        return VillagerSave(
            path=villager_path,
            villager_id=villager_id,
            personal=SaveFile.read(
                file_name=FileName.PERSONAL,
                header_file_name=FileName.PERSONAL_HEADER,
                path=villager_path,
            ),
            postbox=SaveFile.read(
                file_name=FileName.POSTBOX,
                header_file_name=FileName.POSTBOX_HEADER,
                path=villager_path,
            ),
            photo_studio=SaveFile.read(
                file_name=FileName.PHOTO_STUDIO,
                header_file_name=FileName.PHOTO_STUDIO_HEADER,
                path=villager_path,
            ),
            profile=SaveFile.read(
                file_name=FileName.PROFILE,
                header_file_name=FileName.PROFILE_HEADER,
                path=villager_path,
            ),
        )

    def save(self, path: str):
        villager_path = self.get_villager_path(path, self.villager_id)
        self.personal.save(villager_path)
        self.postbox.save(villager_path)
        self.photo_studio.save(villager_path)
        self.profile.save(villager_path)

    def save_decrypted(self, path):
        villager_path = self.get_villager_path(path, self.villager_id)
        self.personal.save_decrypted(villager_path)
        self.postbox.save_decrypted(villager_path)
        self.photo_studio.save_decrypted(villager_path)
        self.profile.save_decrypted(villager_path)

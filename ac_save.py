from file_name import FileName
from save_file import SaveFile


class ACSave:
    def __init__(
            self,
            root_path: str,
            main: SaveFile,
            personal: SaveFile,
            postbox: SaveFile,
            photo_studio: SaveFile,
            profile: SaveFile
    ):
        self.root_path = root_path
        self.main = main
        self.personal = personal
        self.postbox = postbox
        self.photo_studio = photo_studio
        self.profile = profile

    @classmethod
    def build(cls, path):
        return ACSave(
            root_path=path,
            main=SaveFile.read(
                file_name=FileName.MAIN,
                header_file_name=FileName.MAIN_HEADER,
                path=path
            ),
            personal=SaveFile.read(
                file_name=FileName.PERSONAL,
                header_file_name=FileName.PERSONAL_HEADER,
                path=path
            ),
            postbox=SaveFile.read(
                file_name=FileName.POSTBOX,
                header_file_name=FileName.POSTBOX_HEADER,
                path=path
            ),
            photo_studio=SaveFile.read(
                file_name=FileName.PHOTO_STUDIO,
                header_file_name=FileName.PHOTO_STUDIO_HEADER,
                path=path
            ),
            profile=SaveFile.read(
                file_name=FileName.PROFILE,
                header_file_name=FileName.PROFILE_HEADER,
                path=path
            ),
        )

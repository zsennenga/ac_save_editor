import os

from ac_save import ACSave


def get_path(version, file_type):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", version, file_type)


def test_v1_0_0():
    ac_save = ACSave.build(get_path("v1_0_0", "encrypted"))

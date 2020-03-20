import os

from ac_save import ACSave


def get_path(version, file_type):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", version, file_type)


def get_file_path(version, file_type, file_name):
    return os.path.join(get_path(version, file_type), file_name)


def get_bytes(path):
    with open(path, "rb") as f:
        return f.read()


def do_test(version):
    ac_save = ACSave.build(get_path(version, "encrypted"))
    import pdb; pdb.set_trace()

    assert ac_save.main.decrypted_raw == get_bytes(get_file_path(version, "decrypted", "main.dat"))
    assert ac_save.personal.decrypted_raw == get_bytes(get_file_path(version, "decrypted", "personal.dat"))
    assert ac_save.photo_studio.decrypted_raw == get_bytes(
        get_file_path(version, "decrypted", "photo_studio_island.dat"))
    assert ac_save.postbox.decrypted_raw == get_bytes(get_file_path(version, "decrypted", "postbox.dat"))
    assert ac_save.profile.decrypted_raw == get_bytes(get_file_path(version, "decrypted", "profile.dat"))


def test_v1_0_0():
    do_test("v1_0_0")


def test_v1_1_0():
    do_test("v1_1_0")

import os
import tempfile

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

    assert ac_save.main.decrypted_raw == get_bytes(get_file_path(version, "decrypted", "main.dat"))
    assert ac_save.villagers[0].personal.decrypted_raw == get_bytes(
        get_file_path(version, "decrypted/villager0", "personal.dat")
    )
    assert ac_save.villagers[0].photo_studio.decrypted_raw == get_bytes(
        get_file_path(version, "decrypted/villager0", "photo_studio_island.dat"))
    assert ac_save.villagers[0].postbox.decrypted_raw == get_bytes(
        get_file_path(version, "decrypted/villager0", "postbox.dat")
    )
    assert ac_save.villagers[0].profile.decrypted_raw == get_bytes(
        get_file_path(version, "decrypted/villager0", "profile.dat")
    )

    with tempfile.TemporaryDirectory() as tmp:
        ac_save.save(tmp)

        ac_save2 = ACSave.build(tmp)

        assert ac_save.main.decrypted_raw == ac_save2.main.decrypted_raw
        assert ac_save.villagers[0].personal.decrypted_raw == ac_save2.villagers[0].personal.decrypted_raw
        assert ac_save.villagers[0].photo_studio.decrypted_raw == ac_save2.villagers[0].photo_studio.decrypted_raw
        assert ac_save.villagers[0].postbox.decrypted_raw == ac_save2.villagers[0].postbox.decrypted_raw
        assert ac_save.villagers[0].profile.decrypted_raw == ac_save2.villagers[0].profile.decrypted_raw


def test_v1_0_0():
    do_test("v1_0_0")


def test_v1_1_0():
    do_test("v1_1_0")

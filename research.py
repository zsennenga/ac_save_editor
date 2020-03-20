import os

from ac_save import ACSave

research_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "research")
folders = os.listdir(research_path)

saves = []

for folder in folders:
    save_dir = os.path.join(research_path, folder)
    if not os.path.isdir(save_dir):
        continue

    save_input = os.path.join(save_dir, "encrypted")
    save_output = os.path.join(save_dir, "decrypted")

    new_save = ACSave.build(save_input)
    saves.append(new_save)

    new_save.save(save_output)

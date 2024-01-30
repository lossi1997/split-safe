
import os

import configure
from filehandling import Filehandler


def init(args):
    conf = configure.ConfigHandler()
    conf.create_file()


def add(args):
    conf = configure.ConfigHandler()
    print(conf.settings)
    paths: list[str] = []
    while True:
        path: str = input("Insert path, enter to continue adding. Empty input breaks: ")
        if path == "":
            break
        else:
            path = path.replace("\\", "/")
            if os.path.exists(path):
                paths.append(path)
            else:
                print("Invalid path!")

    conf.add_paths(paths)


def save(args):
    conf = configure.ConfigHandler()

    active_drives: list[str] = []
    filepaths: list[str] = []
    for drive, active in conf.settings["ACTIVE_DRIVES"].items():
        if active:
            active_drives.append(drive.upper() + ":")
    for path in conf.settings["PATHS"].items():
        filepaths.append(path[1])

    fh = Filehandler(active_drives, filepaths)

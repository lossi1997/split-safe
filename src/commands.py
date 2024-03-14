
import os

from configure import ConfigHandler
from filehandling import Filehandler
from metadata_parsing import JsonParser
from fileclass import File


def init(args):
    ch = ConfigHandler()
    ch.create_file()
    jp = JsonParser()
    jp.create_file()


def add(args):
    fileobjs: list[File] = []
    while True:
        path: str = input("Insert path, enter to continue adding. Empty input breaks: ")
        if path == "":
            break
        else:
            path = path.replace("\\", "/")
            if os.path.exists(path):
                fileobjs.append(File(path, new=True))
            else:
                print("Invalid path!")
    jp = JsonParser()
    jp.dump_new_files(fileobjs)


def save(args):
    jp = JsonParser()
    fileobjs: list[File] = []
    for name, values in jp.filedata.items():
        fileobjs.append(File(values["orig_path"], name, values["dest_path"], values["modify_date"]))
    jp.update_file_modify_dates(fileobjs)
    fh = Filehandler(fileobjs)
    fh.backup()
    jp.update_file_save_dates(fileobjs)


import os

from configure import ConfigHandler
from filehandling import Filehandler
from metadata_parsing import JsonParser
from fileclass import File


def init(args):
    ConfigHandler()
    JsonParser()


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
    json_parser = JsonParser()
    json_parser.dump_new_files(fileobjs)


def save(args):
    json_parser = JsonParser()
    fileobjs: list[File] = []
    for name, values in json_parser.filedata.items():
        fileobjs.append(File(values["orig_path"], name, values["dest_path"], values["modify_date"]))
    json_parser.update_file_modify_dates(fileobjs)
    fh = Filehandler(fileobjs)
    fh.backup()

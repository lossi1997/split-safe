
import os

from configure import ConfigHandler
from filehandling import Filehandler
from metadata_parsing import JsonParser
from file import File

def init(args):
    ConfigHandler()
    JsonParser()


def add(args):
    json_parser = JsonParser()
    fileobjs: list[File] = []
    while True:
        path: str = input("Insert path, enter to continue adding. Empty input breaks: ")
        if path == "":
            break
        else:
            path = path.replace("\\", "/")
            if os.path.exists(path):
                fileobjs.append(File(path))
            else:
                print("Invalid path!")
    json_parser.dump_new_files(fileobjs)


def save(args):
    json_parser = JsonParser()
    fileobjs = json_parser.get_filedata()
    fh = Filehandler(fileobjs)
    fh.backup()

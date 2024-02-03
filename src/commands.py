
import os

from configure import ConfigHandler
from filehandling import Filehandler
from metadata_parsing import JsonParser


def init(args):
    ConfigHandler()
    JsonParser()


def add(args):
    conf = ConfigHandler()
    print(conf.active_drives)
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

    json_parser = JsonParser()
    for path in paths:
        dest_path = json_parser.set_dest_filepath(path, conf.active_drives)
        json_parser.add_path_data(path, dest_path)


def save(args):
    json_parser = JsonParser()
    fh = Filehandler(json_parser.data)

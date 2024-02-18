
import shutil
import os

from file_dataclass import File

# FIXME error when split-safe folder does not exist


class Filehandler:
    fileobjs: list[File]

    def __init__(self, fileobjs: list[File]):
        self.fileobjs = fileobjs

    def backup(self):
        for file in self.fileobjs:
            if not os.path.exists(file.dest_path):
                os.mkdir(file.dest_path)
                os.system("attrib +h " + file.dest_path)
            shutil.copy(file.orig_path, file.dest_path)

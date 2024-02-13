
import shutil

from file_dataclass import File


class Filehandler:
    fileobjs: list[File]

    def __init__(self, fileobjs: list[File]):
        self.fileobjs = fileobjs

    def backup(self):
        for file in self.fileobjs:
            shutil.copy(file.orig_path, file.dest_path)



class Filehandler:
    _drives: list[str]
    _orig_filepaths: list[str]
    _dest_filepaths: list[str]

    def __init__(self, drives: list[str], orig_filepaths: list[str]):
        self._drives = drives
        self._orig_filepaths = orig_filepaths
        #self._dest_filepaths = self._set_dest_filepaths()



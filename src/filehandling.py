

class Filehandler:
    drives: list[str]
    filepaths: list[str]

    def __init__(self, drives: list[str], filepaths: list[str]):
        self.drives = drives
        self.filepaths = filepaths

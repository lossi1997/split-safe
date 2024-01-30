

class Filehandler:
    _drives: list[str]
    _orig_filepaths: list[str]
    _dest_filepaths: list[str]

    def __init__(self, drives: list[str], orig_filepaths: list[str]):
        self._drives = drives
        self._orig_filepaths = orig_filepaths
        self._dest_filepaths = self._set_dest_filepaths()

    def _set_dest_filepaths(self) -> list[str]:
        new_dests: list[str] = []
        for path in self._orig_filepaths:
            drive = path.split("/")[0]
            path = path.split("/")[1:]
            new_drive = self._drives[(self._drives.index(drive) + 1) % len(self._drives)]
            new_dests.append(new_drive + "/" + "/".join(path))
        return new_dests

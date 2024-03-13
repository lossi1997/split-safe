
import time
import os

from configure import ConfigHandler


class File:
    orig_path: str
    name: str
    dest_path: str
    modify_date: str

    def __init__(self,
                 orig_path: str,
                 name: str | None = None,
                 dest_path: str | None = None,
                 modify_date: str | None = None,
                 new: bool = False
                 ):
        self.orig_path = orig_path
        if new:
            self._create_new()
        else:
            self.name = name
            self.dest_path = dest_path
            self.modify_date = modify_date

    def _create_new(self):
        self.name = self.orig_path.split("/")[-1]
        self.dest_path = self._get_dest_path()
        self.modify_date = self.get_modify_date()

    def _get_dest_path(self) -> str:
        ch = ConfigHandler()
        active_drives = ch.active_drives
        new_dest: str
        drive = self.orig_path.split("/")[0]
        new_drive = active_drives[(active_drives.index(drive) + 1) % len(active_drives)]
        new_dest = new_drive + "/split-safe"
        return new_dest

    def get_modify_date(self) -> str:
        unix_m_date = os.path.getmtime(self.orig_path)
        formatted_m_date = time.strftime("%d.%m.%Y", time.localtime(unix_m_date))
        formatted_m_date = str(formatted_m_date)
        return formatted_m_date

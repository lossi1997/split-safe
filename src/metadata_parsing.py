
import json
import os
import time

from file_dataclass import File

# json file structure:
# {
#   "<filename>": {
#     "orig_path": "<path>",
#     "dest_path": "<path>"
#   }
# }


class JsonParser:
    filepath: str = "./file_metadata.json"
    split_dest_path: str = "/split-safe/"

    def __init__(self):
        if os.path.exists(self.filepath):
            self.data = self.__get_data()
        else:
            self.__create_file()

    def __get_data(self) -> dict:
        with open(self.filepath) as f:
            json_data = json.load(f)
        return json_data

    def __create_file(self) -> None:
        with open(self.filepath, "w") as f:
            default = json.dumps({})
            f.write(default)
        return None

    def add_path_data(self, orig_path: str, dest_path: str) -> None:
        filename = self._get_path_filename(orig_path)
        exists = self._check_existance(orig_path)
        modify_date = self._get_modify_date(orig_path)
        if not exists:
            new_data = {filename: {"orig_path": orig_path, "dest_path": dest_path, "modify_date": modify_date}}
            self.data.update(new_data)
            with open(self.filepath, "w") as outfile:
                json.dump(self.data, outfile, indent=2)
        return None

    @staticmethod
    def _get_path_filename(path: str) -> str:
        filename = path.split("/")[-1]
        return filename

    def _check_existance(self, new_path) -> bool:
        exists: bool = False  # FIXME error when file does not exist
        for fn in self.data.values():
            for path in fn.keys():
                if path == new_path:
                    exists = True
        return exists

    @staticmethod
    def _get_modify_date(path) -> str:
        unix_m_date = os.path.getmtime(path)
        formatted_m_date = time.strftime("%d.%m.%Y", time.localtime(unix_m_date))
        formatted_m_date = str(formatted_m_date)
        return formatted_m_date

    def set_dest_filepath(self, orig_path, active_drives) -> str:
        new_dest: str
        drive = orig_path.split("/")[0]
        new_drive = active_drives[(active_drives.index(drive) + 1) % len(active_drives)]
        new_dest = new_drive + self.split_dest_path
        return new_dest

    def get_filedata(self) -> list[File]:
        fileobjs: list[File] = []
        data = self.__get_data()
        for item in data.items():
            filename = item[0]
            orig_path = item[1]["orig_path"]
            dest_path = item[1]["dest_path"]
            unix_m_date = os.path.getmtime(item[1]["orig_path"])
            formatted_m_date = time.strftime("%d.%m.%Y", time.localtime(unix_m_date))
            file_obj = File(filename, orig_path, dest_path, formatted_m_date)
            fileobjs.append(file_obj)
        return fileobjs

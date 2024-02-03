
import json
import os


# json file structure:
# {
#   "<filename>": {
#     "orig_path": "<path>",
#     "dest_path": "<path>"
#   }
# }


class JsonParser:
    filepath: str = "./file_metadata.json"

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
        if not exists:
            new_data = {filename: {"orig_path": orig_path, "dest_path": dest_path}}
            self.data.update(new_data)
            with open(self.filepath, "w") as outfile:
                json.dump(self.data, outfile, indent=2)
        return None

    def _get_path_filename(self, path: str) -> str:
        filename = path.split("/")[-1]
        return filename

    def _check_existance(self, new_path) -> bool:
        exists: bool = False
        for fn in self.data.values():
            for path in fn.keys():
                if path == new_path:
                    exists = True
        return exists

    def set_dest_filepath(self, orig_path, active_drives) -> str:
        new_dest: str
        drive = orig_path.split("/")[0]
        path = orig_path.split("/")[1:]
        new_drive = active_drives[(active_drives.index(drive) + 1) % len(active_drives)]
        new_dest = new_drive + "/" + "/".join(path)
        return new_dest

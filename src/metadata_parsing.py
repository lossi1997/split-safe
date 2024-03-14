
import json
import os
import time

from fileclass import File

# json file structure:
# {
#   "<filename>": {
#     "orig_path": "<path>",
#     "dest_path": "<path>",
#     "modify_date": "<dd.mm.yyyy>",
#     "save_date": "<dd.mm.yyyy>"
#   }
# }


class JsonParser:
    filepath: str = "./file_metadata.json"
    split_dest_path: str = "/split-safe"
    filedata = dict

    def __init__(self):
        if os.path.exists(self.filepath):
            self.filedata = self.__get__data()

    def __get__data(self) -> dict:
        with open(self.filepath) as f:
            json_data = json.load(f)
        return json_data

    def create_file(self) -> bool:
        file_exists = os.path.exists(self.filepath)
        if not file_exists:
            with open(self.filepath, "w") as f:
                default = json.dumps({})
                f.write(default)
        return file_exists

    def dump_new_files(self, fileobjs) -> None:
        for file in fileobjs:
            if self._check_existance(file) is True:
                print(f"File: '{file.name}' already saved.")
            else:
                new_data = {
                    file.name: {
                        "orig_path": file.orig_path,
                        "dest_path": file.dest_path,
                        "modify_date": file.modify_date,
                        "save_date": ""
                    }
                }
                self.filedata.update(new_data)
                data = self.filedata
                with open(self.filepath, "w") as f:
                    json.dump(data, f, indent=2)
                print(f"File: '{file.name}' successfully saved.")
        return None

    def _check_existance(self, file) -> bool:
        exists: bool = False
        for fn in self.filedata.values():
            for path in fn.keys():
                if path == file.orig_path:
                    exists = True
        return exists

    def update_file_modify_dates(self, files: list[File]) -> None:
        changes = False
        for file in files:
            modify_date = file.get_modify_date()
            if modify_date != self.filedata[file.name]["modify_date"]:
                self.filedata[file.name]["modify_date"] = modify_date
                file.modify_date = modify_date
                changes = True
        if changes:
            with open(self.filepath, "w") as f:
                json.dump(self.filedata, f, indent=2)
        return None

    def update_file_save_dates(self, files: list[File]) -> None:
        for file in files:
            formatted_m_date = time.strftime("%d.%m.%Y", time.localtime())
            self.filedata[file.name]["save_date"] = formatted_m_date
            file.save_date = formatted_m_date
        with open(self.filepath, "w") as f:
            json.dump(self.filedata, f, indent=2)
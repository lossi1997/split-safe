
import json
import os
import time

from fileclass import File

# json file structure:
# {
#   "<filename>": {
#     "orig_path": "<path>",
#     "dest_path": "<path>",
#     "modify_date": "<dd.mm.yyyy>"
#   }
# }


class JsonParser:
    filepath: str = "./file_metadata.json"
    split_dest_path: str = "/split-safe"
    filedata = dict

    def __init__(self):
        self.filedata = self.__init__data()

    def __init__data(self) -> dict:
        if os.path.exists(self.filepath):
            with open(self.filepath) as f:
                json_data = json.load(f)
        else:
            with open(self.filepath, "w") as f:
                default = json.dumps({})
                f.write(default)
                json_data = default
        return json_data

    def dump_new_files(self, fileobjs) -> None:
        for file in fileobjs:
            if self._check_existance(file) is True:
                print(f"File: '{file.name}' already saved.")
            else:
                new_data = {
                    file.name: {
                        "orig_path": file.orig_path,
                        "dest_path": file.dest_path,
                        "modify_date": file.modify_date
                    }
                }
                self.filedata.update(new_data)
                data = self.filedata
                with open(self.filepath, "w") as outfile:
                    json.dump(data, outfile, indent=2)
                print(f"File: '{file.name}' successfully saved.")

    def _check_existance(self, file) -> bool:
        exists: bool = False
        for fn in self.filedata.values():
            for path in fn.keys():
                if path == file.orig_path:
                    exists = True
        return exists

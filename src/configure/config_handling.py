
import configparser
import os


class ConfigHandler(configparser.ConfigParser):
    filepath: str = "./config.ini"
    file_exists: bool = False
    settings: dict = {
        "GENERAL": {
            "autosave": False
        },
        "ACTIVE_DRIVES": {
        },
        "PATHS": {
        }
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if os.path.exists(self.filepath):
            self.file_exists = True
            self.get_data()

    def get_data(self) -> None:
        self.read(self.filepath)
        for section in self.sections():
            for item in self.items(section):
                try:
                    self.settings[section][item[0]] = self.getboolean(section, item[0])
                except ValueError:
                    self.settings[section][item[0]] = item[1]
        return None

    def __get_drives(self) -> None:
        for i in range(65, 91):
            if os.path.exists(chr(i) + ":"):
                self.settings["ACTIVE_DRIVES"][chr(i)] = True
        return None

    def create_file(self) -> None:
        if not self.file_exists:
            self.__get_drives()
            for section, value in self.settings.items():
                self[section] = value
            with open(self.filepath, "w") as configfile:
                self.write(configfile)
        return None

    def add_paths(self, paths) -> None:
        for path in paths:
            # drive: str = path.split(":")[0]
            filename: str = path.split(r"/")[-1]
            self["PATHS"][filename] = path
            with open(self.filepath, "w") as configfile:
                self.write(configfile)
        return None

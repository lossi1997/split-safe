
import configparser
import os


class ConfigHandler(configparser.ConfigParser):
    filepath: str = "../config.ini"
    active_drives: list[str]
    settings: dict = {
        "GENERAL": {
            "autosave": False
        },
        "ACTIVE_DRIVES": {
        },
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if os.path.exists(self.filepath):
            self.settings = self.__get_data()
        else:
            self.__create_file()
        self.active_drives = self.__get_active_drives()

    def __get_data(self) -> dict:
        self.read(self.filepath)
        settings: dict = self.settings
        for section in self.sections():
            for item in self.items(section):
                try:
                    settings[section][item[0]] = self.getboolean(section, item[0])
                except ValueError:
                    settings[section][item[0]] = item[1]
        return settings

    def __get_existing_drives(self) -> None:
        for i in range(65, 91):
            if os.path.exists(chr(i) + ":"):
                self.settings["ACTIVE_DRIVES"][chr(i)] = True
        return None

    def __create_file(self) -> None:
        self.__get_existing_drives()
        for section, value in self.settings.items():
            self[section] = value
        with open(self.filepath, "w") as configfile:
            self.write(configfile)
        return None

    def __get_active_drives(self) -> list[str]:
        active_drives: list[str] = []
        for drive, active in self.settings["ACTIVE_DRIVES"].items():
            if active:
                active_drives.append(drive.upper() + ":")
        return active_drives

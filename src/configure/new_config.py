
import configparser
import os

from .constants import DEFAULT_CONFIG as DC


class Config(configparser.ConfigParser):
    filepath: str = "./config.ini"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__check_file()

    def __check_file(self) -> None:
        file_exists: bool = os.path.isfile(self.filepath)
        if file_exists:
            self.__read_file()
        else:
            self.__create_file()
        return None

    def __read_file(self) -> None:
        self.read(self.filepath)
        return None

    def __create_file(self) -> None:
        for section, value in DC.items():
            self[section] = value
        with open(self.filepath, "w") as configfile:
            self.write(configfile)
        return None

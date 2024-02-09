
from dataclasses import dataclass


@dataclass
class File:
    name: str
    orig_path: str
    dest_path: str
    modify_date: str

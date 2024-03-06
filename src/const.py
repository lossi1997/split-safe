
from commands import *

SUBCOMMANDS = {
    "init": {
        "func": init,
        "kwargs": {
            "help": "help init test",
            "description": "help desc test"
        }
    },
    "add": {
        "func": add,
        "kwargs": {
            "help": "help commit test",
            "description": "help add test"
        }
    },
    "save": {
        "func": save,
        "kwargs": {
            "help": "help save test",
            "description": "help save test"
        }
    }
}

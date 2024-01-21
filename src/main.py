
import argparse
from argparse import Namespace

import command_handler as cmdh


class Main:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.description = "not implemented yet......"
        self.subparsers = self.parser.add_subparsers(dest="command", help="Available commands")
        self.__conf_parsers()
        self.args = self.parser.parse_args()
        self.args.func(self.args)

    def __conf_parsers(self):
        for cmd, config in cmdh.SUBCOMMANDS.items():
            subparser = self.subparsers.add_parser(cmd, help=config["help"])
            subparser.set_defaults(func=config["func"])
            if "args" in config or "kwargs" in config:
                subparser.add_argument(*config["args"], **config["kwargs"])


if __name__ == "__main__":
    Main()

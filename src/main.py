
import argparse
from argparse import Namespace, ArgumentParser

import const


class Main:
    parser: ArgumentParser
    subparsers: '_SubParsersAction[_ArgumentParserT]'
    args: Namespace

    def __init__(self):
        self.parser = argparse.ArgumentParser(prog="splits", description="not implemented yet......")
        self.subparsers = self.parser.add_subparsers(dest="command", help="Available commands")
        self.__conf_parsers()
        self.args = self.parser.parse_args()
        if self.args.command is not None:
            self.args.func(self.args)
        else:
            self.parser.print_help()

    def __conf_parsers(self) -> None:
        for cmd, config in const.SUBCOMMANDS.items():
            subparser = self.subparsers.add_parser(cmd, **config["kwargs"])
            subparser.set_defaults(func=config["func"])
        return None


if __name__ == "__main__":
    Main()

import argparse
import sys
from operator import add

from src.toolkit.converter import _converter
from src.toolkit.calculator import evaluate
from src.toolkit.errors import ToolkitError


def main() -> None:
    parser = argparse.ArgumentParser(description="Калькулятор, конвертер")
    command = parser.add_subparsers(dest="command", required=True)

    calc_parser = command.add_parser("calc")
    calc_parser.add_argument("EXPRESSION")

    converter_parser = command.add_parser("convert")
    converter_parser.add_argument("VALUE")
    converter_parser.add_argument("--from",dest="FROM", required=True)
    converter_parser.add_argument("--to",dest="TO", required=True)

    args = parser.parse_args()

    try:
        if args.command == "calc":
            result = evaluate(args.EXPRESSION)

        else:
            result = _converter(args.VALUE, args.FROM, args.TO)
        print(result)

    except ToolkitError as e:
        print(e, file=sys.stderr)
        sys.exit(2)
if __name__ == "__main__":
    main()

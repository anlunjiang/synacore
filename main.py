import argparse
from typing import Optional, Sequence

from utils.decorators import log_with_time
from vm.vm import run_program

OptionalArgs = Optional[Sequence[str]]


def parse_args(args_list: OptionalArgs = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bin_file", required=True)
    args = parser.parse_args(args_list)

    return args


@log_with_time()
def main():
    args = parse_args()
    run_program(args.bin_file)


if __name__ == "__main__":
    main()

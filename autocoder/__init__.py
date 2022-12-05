import pathlib
import os
import argparse
import sys


HPP = """namespace automod {
    void say_hi();
}
"""

CPP = r"""#include <iostream>
#include "automod.hpp"

void automod::say_hi() {
    std::cout << "hi\n";
};
"""


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("out_dir", default=None)
    parser.add_argument("-n", "--dry-run", action="store_true")

    args = parser.parse_args()

    out_dir = pathlib.Path(args.out_dir) or pathlib.Path(__file__).parent.parent / "autosrc"

    if args.dry_run:
        print(";".join((str(out_dir / "automod.hpp"), str(out_dir / "automod.cpp"))),
                end="")
        return

    print(f"generating autocode in {out_dir}")


    if not out_dir.exists():
        print(f"{out_dir} doesnt exist; creating it for you")
        os.mkdir(out_dir)

    with open(out_dir / "automod.hpp", "w") as hpp:
        hpp.write(HPP)

    with open(out_dir / "automod.cpp", "w") as cpp:
        cpp.write(CPP)

if __name__ == "__main__":
    main()


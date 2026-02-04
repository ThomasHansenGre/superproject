import sys

sys.path.append("..")
from func import my_super_function
from superproject.func import *  # type: ignore


def main():
    print("Hello from superproject!")
    my_super_function()


if __name__ == "__main__":
    main()

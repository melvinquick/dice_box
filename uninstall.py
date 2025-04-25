from os import path, makedirs, remove
from sys import stdout
from shutil import rmtree


def print_green(skk):
    print("\033[92m {}\033[00m".format(skk))


def get_venv_path():
    home_dir = path.expanduser("~")
    venv_dir = path.join(home_dir, ".venvs")
    if not path.exists(venv_dir):
        makedirs(venv_dir)
    return path.join(venv_dir, "prime_number_finder_venv")


def get_desktop_file_path():
    return path.expanduser("~/.local/share/applications/prime_number_finder.desktop")


# * UNINSTALL SECTION


def uninstall():
    venv_path = get_venv_path()
    desktop_file_path = get_desktop_file_path()

    print_green("\nUNINSTALL")
    print("-" * 9)

    if path.exists(venv_path) is False and path.exists(desktop_file_path) is False:
        print_green("\nApplication not installed.\n")

    else:
        if path.exists(venv_path):
            print("Removing the virtual environment...", end="")
            stdout.flush()
            rmtree(venv_path)
            print_green("󰄬")

        else:
            print("No virtual environment found...", end="")
            stdout.flush()
            print_green("󰄬")

        if path.exists(desktop_file_path):
            print("Removing the .desktop entry...", end="")
            stdout.flush()
            remove(desktop_file_path)
            print_green("󰄬")

        else:
            print("No .desktop entry found...", end="")
            stdout.flush()
            print_green("󰄬")

        print_green("\nApplication uninstalled successfully.")


def main():
    uninstall()


if __name__ == "__main__":
    main()

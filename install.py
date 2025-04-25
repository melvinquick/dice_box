from os import path, listdir, makedirs, remove
from sys import stdout
from subprocess import run, DEVNULL
from shutil import rmtree
from textwrap import dedent


def print_green(skk):
    print("\033[92m {}\033[00m".format(skk))


def get_venv_path():
    home_dir = path.expanduser("~")
    venv_dir = path.join(home_dir, ".venvs")
    if not path.exists(venv_dir):
        makedirs(venv_dir)
    return path.join(venv_dir, "dice_box_venv")


def get_site_package_path(venv_path):
    site_packages = path.join(venv_path, "lib")
    for folder in listdir(site_packages):
        if folder.startswith("python"):
            return path.join(site_packages, folder, "site-packages")


def get_desktop_file_path():
    return path.expanduser("~/.local/share/applications/dice_box.desktop")


# * UNINSTALL SECTION


def uninstall():
    venv_path = get_venv_path()
    desktop_file_path = get_desktop_file_path()

    print_green("\nUNINSTALL")
    print("-" * 9)

    if path.exists(venv_path) is False and path.exists(desktop_file_path) is False:
        print_green("\nApplication not installed... Moving on to installation.\n")

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

        print_green(
            "\nApplication uninstalled successfully... Moving on to installation."
        )


# * INSTALL SECTION


def create_venv(venv_path):
    print("Creating the virtual environment...", end="")
    stdout.flush()
    run(
        ["python3", "-m", "venv", venv_path],
        check=True,
        stdout=DEVNULL,
        stderr=DEVNULL,
    )
    print_green("󰄬")

    print("Ensuring pip is up to date...", end="")
    stdout.flush()
    pip_path = path.join(venv_path, "bin", "pip")
    run(
        [pip_path, "install", "--upgrade", "pip"],
        check=True,
        stdout=DEVNULL,
        stderr=DEVNULL,
    )
    print_green("󰄬")


def install_app(venv_path):
    print("Installing Dice Box into the virtual environment...", end="")
    stdout.flush()
    pip_path = path.join(venv_path, "bin", "pip")
    run(
        [pip_path, "install", "dice_box"],
        check=True,
        stdout=DEVNULL,
        stderr=DEVNULL,
    )
    print_green("󰄬")


def get_icon(site_packages):
    icon_relative_path = "dice_box/resources/images/dice_box-128.png"
    full_icon_path = path.join(site_packages, icon_relative_path)
    return full_icon_path


def get_python_path(venv_path):
    return path.join(venv_path, "bin", "python3")


def get_app_path(venv_path):
    return path.join(venv_path, "bin", "dice-box")


def create_desktop_file(icon, version, python, app):
    print("Creating the .desktop entry...", end="")
    stdout.flush()
    desktop_content = dedent(f"""
    [Desktop Entry]
    Version={version}
    Type=Application
    Name=Dice Box
    Comment=Dice roller for board games, card games, bets, etc.
    Exec={python} {app}
    Icon={icon}
    Terminal=false
    Categories=Utility;
    """)
    desktop_content = desktop_content.lstrip()
    with open(
        path.expanduser("~/.local/share/applications/dice_box.desktop"), "w"
    ) as f:
        f.write(desktop_content)
    print_green("󰄬")


def install():
    print_green("\nINSTALL")
    print("-" * 7)

    venv_path = get_venv_path()
    create_venv(venv_path)
    install_app(venv_path)
    site_package_path = get_site_package_path(venv_path)
    version = "1.0.0"
    icon = get_icon(site_package_path)
    python = get_python_path(venv_path)
    app = get_app_path(venv_path)
    create_desktop_file(icon, version, python, app)

    print_green("\nApplication has been installed successfully.")


def main():
    uninstall()
    install()


if __name__ == "__main__":
    main()

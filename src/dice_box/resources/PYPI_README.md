## Table of Contents

[Donations](#donations)  
[Stars](#stars)  
[Purpose](#purpose)  
[Install on Linux](#linux)  
[Build Source Code](#build-source-code)  
[Other Useful Information](#useful-information)  
[Star History](#star-history)

## Donations

[Buy Me A Coffee](https://buymeacoffee.com/KingKairos)  
[GitHub Sponsors](https://github.com/sponsors/melvinquick)

## Stars

If you like this project, please consider giving it a star on [Codeberg](https://codeberg.org/melvinquick/dice_box) or [GitHub](https://github.com/melvinquick/dice_box)!

## Purpose

This is just a simple app for getting "Dice" Rolls. What that really means is you can have anything from 1 "Dice" with 2 "Sides" (which would really just be a 50/50 coin flip), all the way up to 10 "Dice" with 100 "Sides" each! I picture people using this for coin flips, DnD, and anything else you may need "Dice" for.

## Install/Uninstall

**Note**: Your system needs to have Python 3.9 or higher installed to run this!

### Linux

Install: `curl -s https://codeberg.org/melvinquick/dice_box/raw/branch/main/install.py | python3 -`  
Uninstall: `curl -s https://codeberg.org/melvinquick/dice_box/raw/branch/main/uninstall.py | python3 -`

### Build Source Code

If you're not on Linux, or if you want to build this from source, you'll need to do the following.

1. Make sure Python 3.9 or higher is installed.
2. Make sure [UV](https://docs.astral.sh/uv/) is installed.
3. Within a terminal:
   1. `cd` into whatever directory you'd like.
   2. Run the command `git clone https://codeberg.org/melvinquick/dice_box.git`.
   3. `cd` into `dice_box`
4. Run the command `uv sync`
5. Run the command `uv run dice-box`

## Useful Information

[Project Goals](https://codeberg.org/melvinquick/dice_box/projects/16094)  
[Latest Releases](https://pypi.org/project/dice_box/)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=melvinquick/dice_box&type=Date)](https://www.star-history.com/#melvinquick/dice_box&Date)

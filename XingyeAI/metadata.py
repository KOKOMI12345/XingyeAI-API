from .utils import datetime

PURPLE_ASNI = "\033[95m"
CYAN_ASNI = "\033[96m"
BOLD_ASNI = "\033[1m"
END_ASNI = "\033[0m"

LOGO = r"""
                  __  ___                           _    ___ 
                  \ \/ (_)_ __   __ _ _   _  ___   / \  |_ _|
                   \  /| | '_ \ / _` | | | |/ _ \ / _ \  | |
                   /  \| | | | | (_| | |_| |  __// ___ \ | |
                  /_/\_\_|_| |_|\__, |\__, |\___/_/   \_\___|
                                |___/ |___/

      """
AUTHOR = "符玄(KOKOMI12345)"
VERSION = "0.1.0-alpha"
GITHUB = "https://github.com/KOKOMI12345/XingyeAI-API"
DATETIME_NOW = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

INFO_STRING = f"{CYAN_ASNI}{BOLD_ASNI}@Author: {AUTHOR}\n@Version: {VERSION}\n@Github: {GITHUB}\n@Datetime: {DATETIME_NOW}\n{END_ASNI}"


def print_info():
    print(f"{PURPLE_ASNI}{LOGO}{END_ASNI}")
    print(INFO_STRING)

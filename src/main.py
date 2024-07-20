import sys
import readline

from librarian import Librarian
from colors import red, sky
import config

# Точка входа в приложение


def main():
    print(config.HELP_MESSAGE)

    librarian = Librarian()
    prompt = librarian.library.name + ": "

    while True:
        arg = input(sky(prompt)).strip()
        if arg in config.ALLOWED_COMMANDS:
            method = getattr(librarian, arg)
            method()
        elif arg == "help":
            print(config.HELP_MESSAGE)
        elif arg == "":
            continue
        else:
            print(red(config.UNKNOWN_COMMAND), "\n")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\b\b\nДо свидания")

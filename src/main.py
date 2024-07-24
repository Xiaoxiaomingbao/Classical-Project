import pyperclip
from src.Latin import Latin
from src.Greek import Greek


def main():
    configured = False  # configured or not
    la_parser = Latin()
    gr_parser = Greek()

    while 1:
        typed = input(">>>")
        if typed.startswith('@'):
            pass
            # typing process terminated
            if typed.startswith("@model "):
                pass
            elif typed == "@help":
                pass
            elif typed == "@start":
                pass
            elif typed == "@exit":
                exit(0)
            else:
                print("Unknown command")
        else:
            pass


if __name__ == '__main__':
    main()

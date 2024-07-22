import pyperclip


def main():
    while 1:
        typed = input(">>>")
        if typed.startswith('@'):  # typing process terminated
            if typed == "@help":
                pass
            elif typed.startswith("@model "):
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

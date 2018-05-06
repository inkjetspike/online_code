
def banner(message, boarder="-"):
    line = boarder * len(message)
    print(line)
    print(message)
    print(line)


def main():
    banner("Megaman & Bass")

if __name__ == "__main__":
    main()

def foo():
    try:
        f = open('myfile.txt')
    except OSError as err:
        print("OS error:", err)
        raise
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


def main():
    try:
        foo()
    except Exception as err:
        print(f"Exception {err=}, {type(err)=}")
        exit(1)


if __name__ == "__main__":
    main()

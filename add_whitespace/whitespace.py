import sys
import re


class Text:
    ch_flag = False
    en_flag = False
    back_quote_flag = False
    i = 0
    text = None


def add_space(before=True):
    if before:
        Text.text = Text.text[:Text.i] + ' ' + Text.text[Text.i:]
    else:
        Text.text = Text.text[:Text.i + 1] + ' ' + Text.text[Text.i + 1:]
    Text.en_flag = False
    Text.ch_flag = False
    Text.i += 1


def formatting():
    while Text.i < len(Text.text) - 1:
        # Chinese Characters
        if '\u4e00' <= Text.text[Text.i] <= '\u9fa5':
            if Text.en_flag:
                add_space()
            else:
                Text.ch_flag = True
        # A~z, 0~9
        elif Text.text[Text.i].isalpha() or Text.text[Text.i].isnumeric():
            if Text.ch_flag:
                add_space()
            else:
                Text.en_flag = True
            if '\u4e00' <= Text.text[Text.i + 1] <= '\u9fa5':
                add_space(False)
        # back_quote: '`'
        elif Text.text[Text.i] == '`' and Text.text[Text.i + 1] != '`':
            if Text.back_quote_flag:
                add_space(False)
                Text.back_quote_flag = False
            else:
                add_space()
                Text.back_quote_flag = True
        # add space after ',', '.'
        # elif Text.text[Text.i] == ',' or Text.text[Text.i] == '.' or Text.text[Text.i] == ',':
        elif re.match('[,.?:]', Text.text[Text.i]):
            if Text.text[Text.i + 1] != ' ':
                add_space(False)
        else:
            Text.ch_flag = False
            Text.en_flag = False
        Text.i += 1


def main():
    if len(sys.argv) != 2:
        print("Error: Incorrect number of arguments.")
        print("Usage: python file_path.py path/to/file.txt")
        exit(1)

    file_path = sys.argv[1]
    try:
        with open(file_path, encoding="utf-8") as f:
            Text.text = f.read()
            if Text.text is None:
                print("Contents of Text cannot be None!")
                sys.exit()
            else:
                formatting()
    except OSError as e:
        print(f"{type(e)}: {e}")

    print(Text.text)


if __name__ == "__main__":
    main()

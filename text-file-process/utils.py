import hashlib
import os
from string import punctuation, whitespace, digits
from collections import Counter


def count_words(word_list, n):
    """
    Returns three values:
    1.the top n most frequent words in a list
    2.the number of different words
    3.total number of words
    :param n: the top n most frequent words.
    :param word_list:
    :return: three values
    """
    most_common_words = Counter(word_list).most_common(n)
    word_count = {}
    total_words = 0
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        total_words += 1
    return most_common_words, len(word_count), total_words


def read_text_file(file_path):
    """
    Reads from a given file and returns a list of words
    :param file_path:
    :return: a list contains words
    """
    try:
        with open(file_path, encoding="utf-8") as f:
            text = f.read()
            # split(): splits a string into a word list
            # default separator is any whitespace
            return strip_text(text)
    except OSError as e:
        print(f"{type(e)}: {e}")


def strip_text(text):
    """
    Accepts a plain text and return word list,
    removes all separators such as whitespace, newline, digits, just keep word.
    :param text: a plain text
    :return: a list
    """
    res = []
    words = text.split()
    for word in words:
        # strip() removes both the leading and the trailing characters
        # string is immutable which means strip() and lower() always make a copy
        word = word.strip(punctuation + digits + whitespace)
        word = word.lower()
        # if a word is a digit, it will be striped into an empty string
        if word == '': continue
        res.append(word)
    return res


def search_files_with_suffix(directory, suffix):
    """
    Returns a list contains the full path of the files satisfy the given suffix
    :param directory: directory in which you want search
    :param suffix: 'mp3', 'md' for example
    :return: a list
    """
    file_paths = []
    # try to print path, dirs and files to check what they are
    for path, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(suffix):
                file_path = os.path.join(path, file)
                file_paths.append(file_path)
    return file_paths


def calculate_checksum(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
        # MD5 can be used as a checksum to verify data integrity against unintentional corruption.
        # https://en.wikipedia.org/wiki/MD5
        checksum = hashlib.md5(content).hexdigest()
    return checksum


def find_duplicates(directory, suffix):
    """
    Finds all duplicate files in a given directory.
    :param directory:
    :param suffix:
    :return: A dict whose key type is string, and the value type is a list
    """
    file_paths = search_files_with_suffix(directory, suffix)
    checksums = {}
    duplicates = {}
    for file_path in file_paths:
        checksum = calculate_checksum(file_path)
        if checksum in checksums:
            if checksum in duplicates:
                duplicates[checksum].append(file_path)
            else:
                duplicates[checksum] = [file_path, checksums[checksum]]
        else:
            checksums[checksum] = file_path
    return duplicates


if __name__ == "__main__":
    pass

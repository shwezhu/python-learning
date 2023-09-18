import subprocess

import utils


def find_missing_words(file_path, target_words):
    set1 = set(target_words)
    set2 = set(utils.read_text_file(file_path))
    mis_words = set1 - set2
    return mis_words


words = ['he', 'has', 'excited']
missing_words = find_missing_words('novel.txt', words)
print("missing words:", missing_words)  # {'excited', 'has'}


def double_check_duplicates(_duplicates):
    """
    :param _duplicates: A dict whose key type is string,
     and the value type is a list
    :return:
    """
    for file_list in _duplicates.values():
        for i in range(1, len(file_list)):
            diff_output = subprocess.run(['diff', file_list[0], file_list[i]], capture_output=True, text=True)
            if diff_output.stdout:
                print(f"Potential difference found between {file_list[0]} and {file_list[i]}:\n{diff_output.stdout}")
            else:
                print(f"{file_list[0]} and {file_list[i]} are duplicates.")


duplicates = utils.find_duplicates('/Users/David/Downloads/test', 'md')
double_check_duplicates(duplicates)

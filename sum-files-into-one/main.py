import os
import glob
import argparse


def copy_md_contents_to_file(folder_path, output_file):
    # 获取输出文件的目录名
    output_dir = os.path.dirname(output_file)

    # 如果输出目录名非空，则确保目录存在
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # 遍历所有的 .md 文件
    # f"{folder_path}/**/*.md": ** 匹配任意数量的目录和子目录, *.md 匹配所有以 .md 结尾的文件
    for md_file in glob.glob(f"{folder_path}/**/*.md", recursive=True):
        with open(md_file, 'r', encoding='utf-8') as file:
            contents = file.read()

        # 将内容追加到输出文件中
        with open(output_file, 'a', encoding='utf-8') as output:
            output.write(contents + "\n")


def main():
    parser = argparse.ArgumentParser(description="Copy contents of all markdown files in a folder to a single file.")
    parser.add_argument("-i", "--input", required=True, help="Path to the folder containing markdown files.")
    parser.add_argument("-o", "--output", required=True, help="Path to the output file.")

    args = parser.parse_args()
    copy_md_contents_to_file(args.input, args.output)


if __name__ == "__main__":
    main()


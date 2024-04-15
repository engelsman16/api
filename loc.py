import os
import sys

def count_lines_of_code(directory):
    total_lines = 0
    cs_files_count = 0
    test_files_count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.cs'):
                file_path = os.path.join(root, file)
                if "test" not in file.lower():
                    lines, success = count_lines_in_file(file_path)
                    if success:
                        total_lines += lines
                        cs_files_count += 1
                else:
                    test_files_count += 1
    return total_lines, cs_files_count, test_files_count

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            non_empty_lines = [line for line in lines if line.strip()]
            return len(non_empty_lines), True
    except UnicodeDecodeError:
        print(f"UnicodeDecodeError: Unable to decode file '{file_path}'")
        return 0, False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python loc.py <directory_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    loc_count, cs_files_count, test_files_count = count_lines_of_code(folder_path)
    print(f"Total lines of code (excluding empty lines) in {folder_path}: {loc_count}")
    print(f"Total number of .cs files in {folder_path}: {cs_files_count}")
    print(f"Total number of files containing 'test' in {folder_path}: {test_files_count}")
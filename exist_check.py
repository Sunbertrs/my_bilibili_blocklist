import os
import random
import sys

LOCAL_PATH = os.path.abspath(os.path.dirname(__file__))
INPUT_FILE = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else None
COMPARISON_FILE = os.path.join(LOCAL_PATH, "blocklist.csv")

def load_compare_file():
    if not INPUT_FILE:
        raise ValueError("Can't find the csv file to compare. Please specify the file in the argument.")
    elif not INPUT_FILE.endswith(".csv"):
        raise ValueError("The file needs to be converted to csv first then it can be loaded.")
    
    with open(INPUT_FILE, encoding="utf-8") as f:
        return f.readlines()

def convert_format(file_content: list[str]):
    return [line.split(",")[0] for line in file_content[1:]]

def load_comparison_file():
    if not os.path.exists(COMPARISON_FILE):
        raise ValueError("Blocklist file is missing.")
    
    with open(COMPARISON_FILE, encoding="utf-8") as f:
        return [l.split(",")[0] for l in f.readlines()[1:]]
    
def pattern_in_list_match(pattern, list):
    for i, l in enumerate(list):
        length = len(l)
        random_start = random.randint(0, int(length*0.5))
        if pattern in l :
            return True, i
    return False, None

def compare(blocklist_b):
    blocklist_a = load_comparison_file()
    count = 0
    for i, l in enumerate(blocklist_b):
        result = pattern_in_list_match(l, blocklist_a)
        if result[0] and count == 0:
            print(f"{'Inputted file':<40} | {'Main blocklist'}")
        if result[0]:
            print(f"Line {i+2:<3} | {l+"\t"*random.randint(1, 2):\t<6} | Line {result[1]+2:<3} | {blocklist_a[result[1]]}")
            count += 1
    print(f"{count} patterns is already existed in the main blocklist." if count else f"No pattern is the same in main blocklist.")

if __name__ == "__main__":
    file = load_compare_file()
    compare(convert_format(file))
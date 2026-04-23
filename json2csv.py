import json
import csv
import sys
import os

LOCAL_PATH = os.path.abspath(os.path.dirname(__file__))
INPUT_FILE = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else None
OUTPUT_FILE = sys.argv[2] if len(sys.argv) > 2 else os.path.join(LOCAL_PATH, 'output.csv')
COLUMN = ["关键词/表达式", "类型"]

def process_input_file():
    if not INPUT_FILE:
        raise ValueError("Input file is missing.")
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    processed_data = []
    for block_type in (0,1):
        for item in data:
            if item["type"] == block_type:
                processed_data.append(item)
    return processed_data

def write_csv(data, file):
    with open(file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(COLUMN)
        for item in data:
            writer.writerow([item["filter"], item["type"]])

if __name__ == "__main__":
    data = process_input_file()
    write_csv(data, OUTPUT_FILE)


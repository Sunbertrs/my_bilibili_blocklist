import sys
import os
import csv
import xml.etree.ElementTree as et

LOCAL_PATH = os.path.abspath(os.path.dirname(__file__))
INPUT_FILE = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(LOCAL_PATH, "blocklist.csv")
OUTPUT_FILE = sys.argv[2] if len(sys.argv) == 2 else os.path.join(LOCAL_PATH, 'output.xml')

def convert_blocklist():
    root = et.Element("filter")
    with open(INPUT_FILE, encoding='utf-8', newline='') as f:
        csv_data = csv.reader(f)
        for line in csv_data:
            if line[1] == "0":
                section = et.SubElement(root, "item")
                section.attrib["enabled"] = "true"
                section.text = f"t={line[0]}"
            elif line[1] == "1":
                section = et.SubElement(root, "item")
                section.attrib["enabled"] = "true"
                section.text = f"r={line[0]}"
    return et.ElementTree(root)

def write_output_file(xml_data: et.ElementTree): 
    et.indent(xml_data)
    xml_data.write(OUTPUT_FILE, encoding="utf-8")

if __name__ == '__main__':
    data = convert_blocklist()
    write_output_file(data)
# 20.Desirable: Write a program to process JSON and XML data. 

import json
import xml.etree.ElementTree as ET

# Process JSON data
def process_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        print("JSON Data:")
        for usr in data.get("users", []):
            print(f"Name: {usr['name']}, Age: {usr['age']}, City: {usr['city']}")

# Process XML data
def process_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    print("\nXML Data:")
    for usr in root.findall('user'):
        name = usr.find('name').text
        age = usr.find('age').text
        city = usr.find('city').text
        print(f"Name: {name}, Age: {age}, City: {city}")


process_json('user.json')
process_xml('user.xml')

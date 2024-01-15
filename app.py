import os
import json

def directory_to_json(path):
    result = {}
    if os.path.isdir(path):
        result['name'] = os.path.basename(path)
        result['type'] = 'directory'
        result['contents'] = []
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                result['contents'].append(directory_to_json(item_path))
            else:
                result['contents'].append({
                    'name': item,
                    'type': 'file'
                })
    return result

directory_path = "/your/directory/path"
json_data = directory_to_json(directory_path)

with open("directory_structure.json", "w") as json_file:
    json.dump(json_data, json_file, indent=4)

print("Directory structure has been converted to JSON.")

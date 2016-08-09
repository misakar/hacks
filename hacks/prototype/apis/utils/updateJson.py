# coding: utf-8

import os
import json


def updateJson(field_name, field_type, config_json_path):
    with open(config_json_path, 'r') as f:
        data = json.load(f)

    data["configs"]["columns"][field_name] = [field_type]
    data["configs"]["views"].append(field_name)
    data["configs"]["fromjson"].append(field_name)

    with open(config_json_path, 'w+') as f:
        json.dump(data, f, indent=4)

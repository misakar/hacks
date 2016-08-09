# coding: utf-8

import os
from flask import url_for


except_list = ['configs', 'decorators', 'utils', 'hacks']
dir_list = []
apis_list = []
resources_list = []


def findResources(apis_path):
    for _, _dir, _ in os.walk(apis_path):
        dir_list.append(_dir)
    apis_list = dir_list[0]
    for _dirname in apis_list:
        if _dirname not in except_list:
            resources_list.append(_dirname)
    return resources_list

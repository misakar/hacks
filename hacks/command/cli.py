# coding: utf-8

import os
import shutil
import click
import logging
import subprocess

from logging import StreamHandler, DEBUG
from functions import _mkdir

logger = logging.getLogger(__name__)
logger.setLevel(DEBUG)
logger.addHandler(StreamHandler())

prototype_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


@click.group()
def cli():
    pass


@click.command()
@click.argument('project_name')
def new(project_name):
    prototype = os.path.join(prototype_path, 'prototype')
    destination = os.path.join(os.getcwd(), project_name)

    if os.path.isdir(destination):
        logger.warning(
            '\033[31m{warning}\033[0m destination'.format(warning="(╥﹏╥) => ")\
            + ' \033[33m{path}\033[0m already exists.'.format(path=destination)
        )
        return -1

    logger.info('\033[32m(ง •_•)ง =>\033[0m start a hacks project.')

    _mkdir(destination)

    for _dir, _dirs, _files in os.walk(prototype):
        relative = _dir.split(prototype)[1].lstrip(os.path.sep)
        destination_dir = os.path.join(destination, relative)

        _mkdir(destination_dir)

        for _file in _files:
            prototype_file = os.path.join(_dir, _file)
            destination_file = os.path.join(destination_dir, _file)
            shutil.copy(prototype_file, destination_file)

    os.chdir(destination)
    logger.info('\033[32m(ง •_•)ง =>\033[0m initial api virtual environment.')

    subprocess.check_call('virtualenv apivenv', shell=True)
    pip = os.path.join(destination, 'apivenv/bin/pip')
    requirements = os.path.join(destination, 'requirements.txt')
    subprocess.Popen([pip, 'install', '-r', requirements]).wait()

    logger.info('\033[32m(ง •_•)ง =>\033[0m done!')


cli.add_command(new)

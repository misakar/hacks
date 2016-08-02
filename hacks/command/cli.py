# coding: utf-8

import os
import shutil
import click
import logging
import subprocess

from logging import StreamHandler, DEBUG
from functions import _mkdir

from templates import bp_register_template
from templates import configs_append_template
from templates import configs_import_template

logger = logging.getLogger(__name__)
logger.setLevel(DEBUG)
logger.addHandler(StreamHandler())

hacks_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


@click.group()
def cli():
    pass


@click.command()
@click.argument('project_name')
def new(project_name):
    prototype = os.path.join(hacks_path, 'prototype')
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
    python = os.path.join(destination, 'apivenv/bin/python')
    requirements = os.path.join(destination, 'requirements.txt')
    manage_py = os.path.join(destination, 'manage.py')
    subprocess.Popen([pip, 'install', '-r', requirements]).wait()

    logger.info('\033[32m(ง •_•)ง =>\033[0m setup basic config.')

    hacksConfig_init = os.path.join(hacks_path, 'configs/__init__.py')
    hacksConfig_path = os.path.join(hacks_path, 'configs/hacksConfig.py')

    destinationConfig = os.path.join(destination, 'apis/configs')
    destinationConfig_path = os.path.join(destinationConfig, 'hacksConfig.py')
    destinationConfig_init = os.path.join(destinationConfig, '__init__.py')

    _mkdir(destinationConfig)
    shutil.copy(hacksConfig_path, destinationConfig_path)
    shutil.copy(hacksConfig_init, destinationConfig_init)

    logger.info('\033[32m(ง •_•)ง =>\033[0m setup database migration.')
    subprocess.Popen([python, manage_py, 'db', 'init']).wait()
    subprocess.Popen([python, manage_py, 'db', 'migrate']).wait()
    subprocess.Popen([python, manage_py, 'db', 'upgrade']).wait()

    logger.info('\033[32m(ง •_•)ง =>\033[0m done!')


@click.command()
def boot():
    os.popen('python manage.py runserver --port 5486')


@click.command()
@click.option('-api', nargs=1)
def generate(api):
    resources = os.path.join(hacks_path, 'resources')
    destination = os.path.join(os.getcwd(), 'apis/%s' % api)

    if os.path.isdir(destination):
        logger.warning(
            '\033[31m{warning}\033[0m api'.format(warning="(╥﹏╥) => ")\
            + ' \033[33m{path}\033[0m already exists.'.format(path=api)
        )
        return -1

    _mkdir(destination)

    # logger.info('\033[32m(ง •_•)ง =>\033[0m start a hacks api.')

    for _dir, _dirs, _files in os.walk(resources):
        relative = _dir.split(resources)[1].lstrip(os.path.sep)
        destination_dir = os.path.join(destination, relative)

        _mkdir(destination_dir)

        for _file in _files:
            resources_file = os.path.join(_dir, _file)
            destination_file = os.path.join(destination_dir, _file)
            with open(resources_file, 'r') as api_init_file:
                with open(destination_file, 'w+') as dstapi_init_file:
                    for line in api_init_file:
                        new_line = line \
                            .replace('#{=> resources|model <=}',
                                     'class {ModelName}(db.Model):' \
                                .format(ModelName=api[:-1].capitalize())) \
                            .replace('#{=> initial|blueprint <=}',
                                     '{bp} = Blueprint("{bp}", __name__)' \
                                .format(bp=api)) \
                            .replace('#{=> resources|blueprint|import <=}',
                                     'from .. import {bp}' \
                                .format(bp=api)) \
                            .replace('#{=> resources|model|import_as <=}',
                                     'from ..models import {ModelName} as Resources' \
                                .format(ModelName=api[:-1].capitalize())) \
                            .replace('#{=> resources_post|route <=}',
                                     "@{bp}.route('/', methods=['POST'])" \
                                .format(bp=api)) \
                            .replace('#{=> new_resource|function <=}}',
                                     "def new_{bp}():" \
                                .format(bp=api)) \
                            .replace('#{=> resources_delete|route <=}',
                                     "@{bp}.route('/<int:id>/', methods=['DELETE'])" \
                                .format(bp=api)) \
                            .replace('#{=> delete_resource|function <=}',
                                     "def delete_{bp}(id):" \
                                .format(bp=api)) \
                            .replace('#{=> resources_get|route <=}',
                                     "@{bp}.route('/', methods=['GET'])" \
                                .format(bp=api)) \
                            .replace('#{=> get_resources|function <=}',
                                     "def get_{bp}():" \
                                .format(bp=api)) \
                            .replace('#{=> resource_get|route <==}',
                                     "@{bp}.route('/<int:id>/', methods=['GET'])" \
                                .format(bp=api)) \
                            .replace('#{=> get_id_resources|function <=}',
                                     "def get_id_{bp}(id):" \
                                .format(bp=api)) \
                            .replace('#{=> resources_search|route <=}',
                                     "@{bp}.route('/search/')" \
                                .format(bp=api)) \
                            .replace('#{=> search_resources|function <=}',
                                     "def search_{bp}():" \
                                .format(bp=api)) \
                            .replace('#{=> resources_patch|route <=}',
                                     "@{bp}.route('/<int:id>/', methods=['PATCH'])" \
                                .format(bp=api)) \
                            .replace('#{=> update_resource|function <=}',
                                     "def update_{bp}(id):" \
                                .format(bp=api)) \
                            .replace('#{=> resources|name <=}', "%s" % api)

                        dstapi_init_file.write(new_line)

    data = {'bp': api}
    # logger.info('\033[32m(ง •_•)ง =>\033[0m setup api config.')
    resourcesConfig = os.path.join(hacks_path, 'configs/resourcesConfig.py')
    dstConfig = os.path.join(os.getcwd(), 'apis/configs/%sConfig.py' % api)
    with open(resourcesConfig, 'r') as rescs_cfg_file:
        with open(dstConfig, 'w+') as dst_cfg_file:
            for line in rescs_cfg_file:
                new_line = line.replace('#{=> resources|config <=}',
                        "class %(bp)sConfig(object):" % data)
                dst_cfg_file.write(new_line)

    # logger.info('\033[32m(ง •_•)ง =>\033[0m register api blueprint.')
    hacks_init_file = os.path.join(os.getcwd(), 'apis/__init__.py')
    hacks_init_temp_file = os.path.join(os.getcwd(), 'apis/init_temp.py')
    with open(hacks_init_file, 'r') as init_file:
        with open(hacks_init_temp_file, 'w') as init_temp_file:
            for line in init_file:
                new_line = line \
                    .replace('#{=> configs|import <=}',
                             configs_import_template % data) \
                    .replace('#{=> register|blueprint <=}',
                             bp_register_template % data) \
                    .replace('#{=> configs|append <=}',
                             configs_append_template % data)
                init_temp_file.write(new_line)
    shutil.copy(hacks_init_temp_file, hacks_init_file)
    os.remove(hacks_init_temp_file)

    # logger.info('\033[32m(ง •_•)ง =>\033[0m done!')


@click.command()
def migrate():
    os.popen('python manage.py db migrate')
    os.popen('python manage.py db upgrade')


cli.add_command(new)
cli.add_command(boot)
cli.add_command(generate)
cli.add_command(migrate)

# coding: utf-8

"""
	hacks~bin
	``````````

	hacks command-line tools

		- hack new
		- hack generate -api
		- hack boot
		- hack task
		- hack migration
"""


import click


@click.group()
def cli():
	pass


from .hack_boot import boot
from .hack_generate import generate
from .hack_migrate import migrate
from .hack_task import task
from .hack_new import new


cli.add_command(boot)
cli.add_command(generate)
cli.add_command(migrate)
cli.add_command(task)
cli.add_command(new)


"""
click的文档需要好好看
关于
	`. 安装虚拟环境的子进程
	`. wrap gunicorn server
	`. 目录的遍历
	`. 环境变量的配置
有没有更好的做法
new, generate的时候一定要快(网络正常)
migrate先做一个简单的
"""
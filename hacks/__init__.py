# coding: utf-8

"""
	hacks
	`````

	hacks is a realtime mvc web framework
		~ for morden web development of your dream.z

	hacks built on top of flask, with several hooks, signals and useful decorators.
"""


__version__ = '0.10.1.dev0'

# hacks 不是最佳实践、不仅仅是个脚手架, 而是一个框架, flask只是作为hacks的wsgi层和工具层
# hacks的灵活和配置是通过一系列配置完成的.

# 装饰器固然是好东西, 但是, 装饰器是分散到每一个函数的, 如果能通过配置文件的形式, 集中式的管理资源API,
# 这将是一个非常好的做法

# 这样就需要在API访问之上，设置一个配置层, 也就是钩子注入. 或者说一系列的middleware.
# 这个想法是绝对可行的, 而且比应用代码装饰器好...
# 问题是如何配置开关... 所以中间件部署需要在服务器前部署就可以了, 每次服务器启动前读取中间件配置, 决定是否部署这个
# 中间件, 明天具体看一下 WSGI 中间件开发!

# 然后还要做好 API 和 html 的错误处理... json异常以及错误处理的默认界面

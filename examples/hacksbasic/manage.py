# coding: utf-8
"""
    hacks~manage.py
    ```````````````

    hacks project management file:

        - $ python manage.py runserver
            - alias ```hack boot```
        - $ python manage.py celery
"""

import sys
import subprocess
from blueprints import app, socketio
from configs import connection
from flask_script import Manager, Command, Server as _Server, Option
import eventlet
eventlet.monkey_patch()


manager = Manager(app)


class Server(_Server):
    help = description = 'Run the Socket.IO web server'

    def get_options(self):
        options = (
            Option('-h', '--host',
                   dest='host',
                   default=self.host),

            Option('-p', '--port',
                   dest='port',
                   type=int,
                   default=self.port),

            Option('-d', '--debug',
                   action='store_true',
                   dest='use_debugger',
                   help=('enable the Werkzeug debugger (DO NOT use in '
                         'production code)'),
                   default=self.use_debugger),
            Option('-D', '--no-debug',
                   action='store_false',
                   dest='use_debugger',
                   help='disable the werkzeug debugger',
                   default=self.use_debugger),

            Option('-r', '--reload',
                   action='store_true',
                   dest='use_reloader',
                   help=('monitor Python files for changes (not 100%% safe '
                         'for production use)'),
                   default=self.use_reloader),
            Option('-R', '--no-reload',
                   action='store_false',
                   dest='use_reloader',
                   help='do not monitor Python files for changes',
                   default=self.use_reloader),
        )
        return options

    def __call__(self, app, host, port, use_debugger, use_reloader):
        if use_debugger is None:
            use_debugger = app.debug
            if use_debugger is None:
                use_debugger = True
        if use_reloader is None:
            use_reloader = use_debugger
        socketio.run(app, host=host, port=port, debug=use_debugger,
                     use_reloader=use_reloader, **self.server_options)

manager.add_command('runserver', Server())


class CeleryWorker(Command):
    name = 'celery'
    capture_all_args = True

    def run(self, argv):
        boot = subprocess.call(
            ['celery', 'worker', '-A', 'blueprints.celery'] + argv)
        sys.exit(boot)

manager.add_command('celery', CeleryWorker())


if __name__ == '__main__':
    manager.run()

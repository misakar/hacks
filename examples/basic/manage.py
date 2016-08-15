# coding: utf-8
"""
    hacks~manage.py
    ```````````````

    hacks project management file:

        - $ python manage.py runserver
            - python manage.py runserver -p 5486
              # alias ```hack boot```
"""

from blueprints import app
from configs import connection
from flask_script import Manager


manager = Manager(app)


if __name__ == '__main__':
    app.debug = True
    manager.run()

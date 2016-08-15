# coding: utf-8
"""
    blueprints~main.py
    ``````````````````

    hacks app blueprint

        - define app blueprint
        - add app index rule
"""

from flask import Blueprint, render_template


main = Blueprint(
        'main', __name__,
        template_folder='templates',
        static_folder='static'
)


@main.route('/')
def index():
    return render_template('index.html')


from .controllers.main import views

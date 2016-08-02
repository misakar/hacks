# coding: utf-8


bp_register_template = '''from .%(bp)s import %(bp)s
    api.register_blueprint(%(bp)s, url_prefix='/api/%(bp)s')

    #{=> register|blueprint <=}'''

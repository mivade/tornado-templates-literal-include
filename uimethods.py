from os import path


def vue_template(handler, filename):
    base_path = path.abspath(path.dirname(__file__))
    with open(path.join(base_path, filename)) as f:
        return f.read()

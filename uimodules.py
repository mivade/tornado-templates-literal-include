from os import path
from tornado.web import UIModule

_basepath = path.join(path.abspath(path.dirname(__file__)), "templates")


class VueTemplate(UIModule):
    def render(self, filename):
        fname = path.join(_basepath, filename)
        with open(fname) as f:
            contents = f.read()
        return self.render_string("vue-template.html",
                                  id="test-template", contents=contents)

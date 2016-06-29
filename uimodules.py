from os import path
from tornado.web import UIModule
from tornado.escape import xhtml_unescape

_basepath = path.join(path.abspath(path.dirname(__file__)), "templates")


class VueTemplate(UIModule):
    def render(self, filename):
        fname = path.join(_basepath, filename)
        with open(fname) as f:
            contents = xhtml_unescape(f.read())
        return self.render_string("vue-template.html",
                                  id="test-template", contents=contents)

from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
import uimethods


class RootHandler(RequestHandler):
    def get(self):
        self.render('index.html')


app = Application(
    [(r'/', RootHandler)],
    static_path='static',
    template_path='templates',
    ui_methods=uimethods,
    debug=True
)
app.listen(8989)
IOLoop.current().start()

import logging
from tornado import log
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
import uimodules

logger = logging.getLogger(__name__)


class RootHandler(RequestHandler):
    def get(self):
        self.render('index.html')


log.enable_pretty_logging()
app = Application(
    [(r'/', RootHandler)],
    static_path='static',
    template_path='templates',
    ui_modules=uimodules,
    debug=True
)
app.listen(8989)
logger.info("Listening on :8989")
IOLoop.current().start()

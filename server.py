import tornado.ioloop
import tornado.web
import tornado.template
import tornado.options
import tornado.httpserver
import os

from List import *
from tornado.options import define
define("port", default=8888, help="Run on given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        dutyMap = getDutyMap()
        items = dutyMap
        self.render('template.html', title='Who cleans the house this week', items=items)
    
class NextSuckerHandler(tornado.web.RequestHandler):
    def get(self, duty):
        dutyMap = getDutyMap()
        result = nextSucker(duty, dutyMap)
        self.write(json.dumps(getSucker(duty,dutyMap)))

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),    
            (r"/nextSucker/([a-z]+)", NextSuckerHandler),
        ]
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
        }
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()

import tornado.ioloop
import tornado.web
import tornado.template
import tornado.options
import os

from List import *

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

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}
application = tornado.web.Application([
    (r"/", MainHandler),    
    (r"/nextSucker/([a-z]+)", NextSuckerHandler),
], **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

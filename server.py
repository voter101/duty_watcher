import tornado.ioloop
import tornado.web
import tornado.template
import tornado.options

from List import *

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        dutyMap = getDutyMap()
        items = dutyMap
        self.render('template.html', title='Który frajer sprząta w tym tygodniu?', items=items)

    
class NextSuckerHandler(tornado.web.RequestHandler):
    def get(self, duty):
        dutyMap = getDutyMap()
        result = nextSucker(duty, dutyMap)
        self.write(json.dumps(getSucker(duty,dutyMap)))


application = tornado.web.Application([
    (r"/", MainHandler),    
    (r"/nextSucker/([a-z]+)", NextSuckerHandler),
])

if __name__ == "__main__":
    tornado.options.parse_command_line()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

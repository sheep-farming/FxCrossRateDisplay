import datetime
from WindPy import *
from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib

def today():
    today = datetime.datetime.today()
    return xmlrpclib.DateTime(today)

server = SimpleXMLRPCServer(("0.0.0.0", 8080))
print "Listening on port 8080..."
server.register_function(today, "today")
server.register_function(w.start, 'start')
server.register_function(w.wsq, 'wsq')
server.register_function(w.cancelRequest, 'cancel')

server.serve_forever()

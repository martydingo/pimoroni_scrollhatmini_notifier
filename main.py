from flask import Flask, request
from flask_restful import Resource, Api
import time
import scrollphathdcustom
import scrollphathd

# Let's not blind anyone here, unless it's intentionally done using the below line of code. 
scrollphathd.set_brightness(0.2)

app = Flask(__name__)
api = Api(app)

class Notify(Resource):
  def post(self, apiNotifyMsg):
      scrollphathdcustom.scrollMsg(apiNotifyMsg)
      scrollphathdcustom.scrollMsg(" ")
class Clear(Resource):
  def post(self):
      scrollphathd.clear()


api.add_resource(Notify, '/notify/notify/<apiNotifyMsg>')
api.add_resource(Clear, '/notify/clear')

if __name__ == '__main__':
     app.run(port='5002')
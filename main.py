from flask import Flask, request
from flask_restful import Resource, Api
import scrollphathdcustom
import scrollphathd

# Let's not blind anyone here, unless it's intentionally done using the below line of code. 
scrollphathd.set_brightness(0.2)

app = Flask(__name__)
api = Api(app)

class Notifiy(Resource):
  def post(Resource):
      scrollphathdcustom.scrollMsg(apiNotifyMsg)

api.add_resource(Notify, '/notify/<apiNotifyMsg>')

if __name__ == '__main__':
     app.run(port='5002')
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
  def post(self):
      apiNotifyMsg = request.args['message']
      scrollphathdcustom.scrollMsg(apiNotifyMsg)
      scrollphathdcustom.scrollMsg(" ")

api.add_resource(Notify, '/notify')

if __name__ == '__main__':
     app.run(host='0.0.0.0',port='80')
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from ezw_restful_controller import EZWRController
import os

application = Flask(__name__)
api = Api(application)
CORS(application)
REF_WHITE_LIST = os.environ['REF_WHITE_LIST']
ref_white_list_arr = [x.strip() for x in REF_WHITE_LIST.split(",")]

class Ezw_API(Resource):

    def post(self):
        json_data = request.get_json()
        latitude = json_data['latitude']
        longitude = json_data['longitude']
        start_date = json_data['start_date']
        end_date = json_data['end_date']
        #print(json_data)

        #remote_add = request.remote_addr
        referrer = request.headers.get("Referer")
        #print("Referrer: [{}]".format(referrer))
        if (referrer in ref_white_list_arr):
            ezw = EZWRController()     
            ezw_reports = ezw.getWeatherReports(start_date, end_date, latitude, 
                                            longitude)
            return {'reports': ezw_reports}
        else: 
            return {'message': 'Service is blocked'}

api.add_resource(Ezw_API, '/ezw_api')

if __name__ == '__main__':
    application.run(debug=False)
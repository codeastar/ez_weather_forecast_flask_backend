from ezw_model import WeatherReport
from datetime import datetime,timedelta
import requests, os, json

DARK_SKY_API_KEY = os.environ['DARK_SKY_KEY']
option_list = "exclude=currently,minutely,hourly,alerts&units=si"

class EZWRController:
 
    def getWeatherReports(self, date_from, date_to, 
                        latitude, longitude):
        d_from_date = datetime.strptime(date_from , '%Y-%m-%d')
        d_to_date = datetime.strptime(date_to , '%Y-%m-%d')
        delta = d_to_date - d_from_date

        latitude = str(latitude)
        longitude = str(longitude)

        weather_reports = []

        for i in range(delta.days+1):
            new_date = (d_from_date + timedelta(days=i)).strftime('%Y-%m-%d')
            search_date = new_date+"T00:00:00"
            response = requests.get("https://api.darksky.net/forecast/"+DARK_SKY_API_KEY+"/"+latitude+","+longitude+","+search_date+"?"+option_list)
            json_res = response.json()
            report_date = (d_from_date + timedelta(days=i)).strftime('%Y-%m-%d %A')
            unit_type = '°F' if json_res['flags']['units'] == 'us' else '°C'
            min_temperature = str(json_res['daily']['data'][0]['apparentTemperatureMin'])+unit_type
            max_temperature = str(json_res['daily']['data'][0]['apparentTemperatureMax'])+unit_type
            summary = json_res['daily']['data'][0]['summary']
            icon = json_res['daily']['data'][0]['icon']
            precip_type = None
            precip_prob = None
            raining_chance = None
            if'precipProbability' in json_res['daily']['data'][0] and 'precipType' in json_res['daily']['data'][0]:
                precip_type = json_res['daily']['data'][0]['precipType']
                precip_prob = json_res['daily']['data'][0]['precipProbability']
            if (precip_type == 'rain' and precip_prob != None):
                precip_prob *= 100
                raining_chance = "%.2f%%" % (precip_prob)

            ezw_wr = WeatherReport(report_date, max_temperature,min_temperature, 
            summary, raining_chance, icon)        

            weather_reports.append(ezw_wr)
            #object list to JSON list
            json_reports = json.dumps([weather_report.__dict__ for weather_report in weather_reports])

        return json_reports
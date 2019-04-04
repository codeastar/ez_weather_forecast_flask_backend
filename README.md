# ez_weather_forecast_flask_backend
Easy Weather Forecast RESTful API server with Flask-RESTful

Full document: 
http://www.codeastar.com/flask-backend-react-frontend-weather-1

## Quick start
$cd ezw_restful

$pipenv --three

$pip install -r requirements.txt 
(download/install required libraries to your current system)

$pipenv shell

$export DARK_SKY_KEY={your Dark Sky API Key}    
//SET DARK_SKY_KEY={your Dark Sky API Key}    for Windows users

$export REF_WHITE_LIST='{white listed refernence domains}'

//e.g. export REF_WHITE_LIST='elasticbeanstalk.com, abc.com'

//use SET REF_WHITE_LIST={....}    for Windows users

$python application.py  

## Live Demo

https://www.codeastar.com/ez-weather-forecast/

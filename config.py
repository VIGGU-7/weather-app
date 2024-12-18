import os 
baseurl="https://api.openweathermap.org/"
basekey="data/"
version="2.5/"
weather="weather/"
def call():
  return baseurl+basekey+version+weather
def apikey():
  return os.getenv('api_key')
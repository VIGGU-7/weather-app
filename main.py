import requests
import config
url=config.call()
queries={
"q":input("Input City : "),
"appid":config.apikey()
}
try:
  r=requests.get(url,params=queries)
  print("Country : "+str(r.json()['sys']['country']))
  print("Longitude : "+str(r.json()['coord']['lon']))
  print("Latitude : "+str(r.json()['coord']['lat']))
  print("Temperature : "+str(r.json()['main']['temp']-273))
except:
  print("internalerror,please tryagain later")
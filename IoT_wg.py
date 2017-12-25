from urllib.request import urlopen
import tkinter as tk
import json
import time



while(1):
    print("Please key in the reigon")
    str1 = input("Your reigon:")
    str="http://api.wunderground.com/api/f4d4d2cde7f948ec/geolookup/conditions/q/TW/"+str1+".json"
    str2="http://api.wunderground.com/api/f4d4d2cde7f948ec/hourly/q/TW/"+str1+".json"
    
    f1 = urlopen(str)
    json_string1 = f1.read().decode('utf-8')
    parsed_json1 = json.loads(json_string1)
    location_TP = parsed_json1['location']['city']
    temp_TP = parsed_json1['current_observation']['temp_c']
    rain_TP = parsed_json1['current_observation']['precip_1hr_in']
    
    f2 = urlopen(str2)
    json_string2 = f2.read().decode('utf-8')
    parsed_json2 = json.loads(json_string2)
    temp_HR = parsed_json2['hourly_forecast'][1]['temp']['metric']
    rain_HR = parsed_json2['hourly_forecast'][1]['pop']
    
    temp_TP=float(temp_TP)
    rain_TP=float(rain_TP)
    temp_HR = float(temp_HR)
    rain_HR = float(rain_HR)
    
    if rain_TP<0:
        rain_TP=0
    
    print ("Current temperature in %s is: %f" % (location_TP, temp_TP))
    print ("Current precipitation in %s is: %f" % (location_TP, rain_TP))
    print ("%s"%(temp_HR))

    if (temp_TP>30 or temp_TP<18 or rain_TP>5):
        print ("I suggest that you should skip the class")
        print("")

    else:
        print ("I suggest that you should attend the class")
        print("")




    f1.close()
    f2.close()


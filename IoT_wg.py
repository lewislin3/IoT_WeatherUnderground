from urllib.request import urlopen
import json
import time


print("Welcome to I want to skip the class app")

while(1):
    print("Please key in the reigon")
    str = input("Your reigon:")
    str="http://api.wunderground.com/api/f4d4d2cde7f948ec/geolookup/conditions/q/TW/"+str+".json"
    
    f1 = urlopen(str)
    json_string1 = f1.read().decode('utf-8')
    parsed_json1 = json.loads(json_string1)
    location_TP = parsed_json1['location']['city']
    temp_TP = parsed_json1['current_observation']['temp_c']
    rain_TP = parsed_json1['current_observation']['precip_1hr_in']
    
    temp_TP=float(temp_TP)
    rain_TP=float(rain_TP)
    
    if rain_TP<0:
        rain_TP=0
    
    print ("Current temperature in %s is: %f" % (location_TP, temp_TP))
    print ("Current precipitation in %s is: %f" % (location_TP, rain_TP))

    if (temp_TP>30 or temp_TP<15 or rain_TP>5):
        print ("I suggest that you should skip the class")
        print("")

    else:
        print ("I suggest that you should attend the class")
        print("")
    



    
    


    f1.close()

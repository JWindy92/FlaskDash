import json

f = open('.env', 'w')
f.write('''
FLASK_APP="dashb"
MQTT_BROKER=""
''')
f.close()

device_dict = {
    "yeelight": {

    }
}

with open("dashb/devices.json", "w") as outfile:
    json.dump(device_dict, outfile)
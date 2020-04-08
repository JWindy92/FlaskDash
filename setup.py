import json

f = open('.env', 'w')
f.write('''
FLASK_APP="dashb"
''')
f.close()

device_dict = {
    "yeelight": {

    }
}

with open("dashb/devices.json", "w") as outfile:
    json.dump(device_dict, outfile)
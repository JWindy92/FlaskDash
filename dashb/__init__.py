from flask import Flask, render_template, url_for, request
from flask_cors import CORS
import paho.mqtt.client as mqtt
import dashb.yeelight_helpers as ylight
import json

app = Flask(__name__)
CORS(app)
client = mqtt.Client("SmartHome")
client.connect("10.0.0.91")

devices = {
    'desk' : 'desk-light',
    'table' : 'table-lamp',
    'bed' : 'bed-light',
    'leds' : 'desk-leds'
}

@app.route('/')
def dash():
    return render_template('dashboard.html', title="Dashboard")

@app.route('/lights/<device_name>', methods=['GET', 'POST'])
def desk_light(device_name):
    device = device_name
    if request.method == 'POST':
        if 'payload' in request.json:
            client.publish(request.json['topic'], json.dumps(request.json['payload']))
            return "Success"

        if request.json['service'] == 'yeelight':
            if request.json['command'] == 'ON':
                ylight.turn_on(ylight.bulb) # bulb still hard coded, needs work
            elif request.json['command'] == 'movie':
                print('working')
                ylight.movie_mode(ylight.bulb)
            else:
                ylight.turn_off(ylight.bulb)
            return "Success"

        command = request.json['command']
        print("Powering", command)
        client.publish(f'cmnd/lights/{device}/POWER', command)
        return "Success"
    else: # Not sure what to do with GET, maybe for state checks?
        pass

@app.route('/post-test', methods=['GET', 'POST'])
def post_test():
    if request.method == 'POST':
        print("Got a post")
        return {"Success" : 200}
    else:
        pass
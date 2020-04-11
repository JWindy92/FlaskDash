from flask import Flask, render_template, url_for, request
from flask_cors import CORS
from flask_mqtt import Mqtt
# import paho.mqtt.client as mqtt
import dashb.yeelight_helpers as ylight
import json
import os


app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = os.environ.get('MQTT_BROKER')
app.config['MQTT_BROKER_PORT'] = 1883
# app.config['MQTT_USERNAME'] = 'user'
# app.config['MQTT_PASSWORD'] = 'secret'
app.config['MQTT_REFRESH_TIME'] = 1.0
mqtt = Mqtt(app)
CORS(app)
test_var = 0

# client = mqtt.Client("SmartHome")
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('test/')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print(data['payload'])

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
            mqtt.publish(request.json['topic'], json.dumps(request.json['payload']))
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
        mqtt.publish(f'cmnd/lights/{device}/POWER', command)
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
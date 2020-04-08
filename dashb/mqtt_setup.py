import paho.mqtt.client as mqtt
import json
# 83 leds
client = mqtt.Client("SmartHome")
client.connect("10.0.0.91")

message = {
	"brightness": 255,
	"effect": "solid",
	"color": {"r": 132, "g": 3, "b": 252},
	"state": "ON"
}

json_data = json.dumps(message)

client.publish('johnw/desk_strip/set', json_data)
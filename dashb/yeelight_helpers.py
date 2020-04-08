from yeelight import Bulb, RGBTransition, Flow
import json

f = open('dashb/devices.json')
yeelight_data = json.load(f)

bulb = Bulb(yeelight_data["yeelight"]["bed-lamp"])

def turn_off(bulb):
    print('turning off')
    bulb.turn_off()

def turn_on(bulb):
    print('turning on')
    bulb.turn_on()
    bulb.set_brightness(100)
    bulb.set_color_temp(4700)

def movie_mode(bulb):
    if bulb.get_properties()['power'] == 'off':
        bulb.set_brightness(50)
        bulb.turn_on()
    transitions = [
        RGBTransition(0,0,255, duration=20000, brightness=10)
    ]

    flow = Flow(
        count=1,
        transitions=transitions,
        action=Flow.actions.stay
    )
    bulb.start_flow(flow)

if __name__ == "__main__":
    # movie_mode(bulb)
    turn_on(bulb)
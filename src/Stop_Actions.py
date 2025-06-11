import json
from pynput import keyboard

actions = []

class Cut:
    def on_release(key):
        global Recording 
        if key == keyboard.Key.esc:
            Recording = False
            with open("C:\\Automator_System\\ActionFile\\Recorded_Actions.json" , "w") as d:
                json.dump(actions , d , indent=2)

        return False        
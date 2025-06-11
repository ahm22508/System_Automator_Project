import json
import time
import pyautogui

actions = []

class Replaying:
    def replay_actions():
        global actions
        with open("C:\\Automator_System\\ActionFile\\Recorded_Actions.json" , "r") as d:
            actions = json.load(d)
        start = time.time()
        for action in actions:
            delay = action['time'] - (time.time() - start)
            if delay > 0:
                time.sleep(delay)

            if action['type'] == 'mouse click' and action['pressed']:
                pyautogui.click(action['x']  , action['y'] , button=action['button'].split('.')[-1])
            elif action['type'] == 'key_press':
                pyautogui.typewrite(action['key'])    
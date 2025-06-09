import json
import time
import pyautogui

actions = []

class Replaying:
    def replay_actions():
         with open("actions.json", "r") as f:
             actions = json.load(f)

    print("▶️ Replaying...")
    start = time.time()
    for action in actions:
        delay = action['time'] - (time.time() - start)
        if delay > 0:
            time.sleep(delay)

        if action['type'] == 'mouse_click' and action['pressed']:
            pyautogui.click(action['x'], action['y'], button=action['button'].split('.')[-1])
        elif action['type'] == 'key_press':
            pyautogui.typewrite(action['key'])

    print("✅ Replay complete.")

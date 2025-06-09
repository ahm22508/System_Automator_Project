import json
from pynput import keyboard

actions = []

class Cut:
    def on_release(key):
        global recording
        if key == keyboard.Key.esc:
            recording = False
            print("🛑 Recording stopped.")
            with open("actions.json", "w") as f:
                json.dump(actions, f, indent=2)
        return False

import time
import pyautogui
from Base import AutomationComponent

class Replaying(AutomationComponent):
    def __init__(self):
        super().__init__()

    def replay_actions(self):
        actions = self.file_manager.load()  # Load recorded actions
        start = time.time()  # Start timing

        for action in actions:
            delay = action['time'] - (time.time() - start)
            if delay > 0:
                time.sleep(delay)  # Synchronize replay timing

            if action['type'] == 'mouse_click' and action['pressed']:
                # Simulate mouse click
                pyautogui.click(action['x'], action['y'], button=action['button'].split('.')[-1])
            elif action['type'] == 'key_press':
                # Simulate key press
                pyautogui.typewrite(action['key'])
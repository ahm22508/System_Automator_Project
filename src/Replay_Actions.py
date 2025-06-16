import time
import pyautogui
from ActionFileManagement import FileManaging

class Replaying:
   

    def replay_actions(self):
        file = FileManaging()
        actions = file.load() 
        start = time.time() 

        for action in actions:
            delay = action['time'] - (time.time() - start)
            if delay > 0:
                time.sleep(delay) 

            if action['type'] == 'mouse_click' and action['pressed']:

                pyautogui.click(action['x'], action['y'], button=action['button'].split('.')[-1])
            elif action['type'] == 'key_press':

                pyautogui.typewrite(action['key'])
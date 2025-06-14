from ActionFileManagement import FileManaging
import time
import pyautogui


class Replaying:

    def __init__(self):
        self.fileManager = FileManaging([])

    def replay_actions(self):
        start = time.time()
        
        File = self.fileManager.load_Action_File()
        for action in File:
            delay = action['time'] - (time.time() - start)
            if delay > 0:
                time.sleep(delay)
            if action['type'] == 'Mouse_Click' and action['Pressed']:
                pyautogui.click(action['x']  , action['y'] , button=action['button'].split('.')[-1])
            elif action['type'] == 'Key_Press':
                pyautogui.typewrite(action['key'])    
from pynput import keyboard
from ActionFileManagement import FileManaging
class Cut:
    def __init__(self, actions):
        self.actions = actions
        
    def on_release(self, key):
        if key == keyboard.Key.esc:
           file = FileManaging()
           actions = self.actions
           file.save(actions)
           return False 
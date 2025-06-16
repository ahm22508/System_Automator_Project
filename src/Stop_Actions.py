from pynput import keyboard

class Cut:
    def __init__(self, actions, file_manager):
        self.actions = actions
        self.file_manager = file_manager 

    def on_release(self, key):
        if key == keyboard.Key.esc:
            self.file_manager.save(self.actions) 
            return False 
import time
from pynput import mouse, keyboard
from Stop_Actions import Cut

class Action:
    def __init__(self):
        self.actions = []
        self.time_start = None
        self.recording = False

    def on_press(self, key):
        if self.recording:
            try:
                key_str = key.char  
            except AttributeError:
                key_str = str(key)  
            self.actions.append({
                'type': 'key_press',
                'key': key_str,
                'time': time.time() - self.time_start
            })  

    def on_click(self, x, y, button, pressed):
        if self.recording:
            self.actions.append({
                'type': 'mouse_click',
                'x': x,
                'y': y,
                'button': str(button),
                'pressed': pressed,
                'time': time.time() - self.time_start
            })  

    def start_recording(self):
        self.actions = []
        self.time_start = time.time()
        self.recording = True

        cut_handler = Cut(self.actions)  
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.keyboard_listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=cut_handler.on_release
        )

        self.mouse_listener.start()
        self.keyboard_listener.start()
        self.keyboard_listener.join()
import time
from pynput import mouse, keyboard
from Stop_Actions import Cut


class Action:
    def on_press(key):
        if recording:
             try:
                  key_str = key.char
             except AttributeError:
                 key_str = str(key)
                 actions.append({
                'type': 'key_press',
                'key': key_str,
                'time': time.time() - start_time
            })

    def on_click(x, y, button, pressed):
        if recording:
            actions.append({
            'type': 'mouse_click',
            'x': x,
            'y': y,
            'button': str(button),
            'pressed': pressed,
            'time': time.time() - start_time
        })

# Record keyboard events
    
    def start_recording():
        global recording, start_time, actions
        print("🔴 Recording started... Press ESC to stop.")
        actions = []
        start_time = time.time()
        recording = True

        mouse_listener = mouse.Listener(on_click=Action.on_click)
        keyboard_listener = keyboard.Listener(on_press=Action.on_press, on_release=Cut.on_release)

        mouse_listener.start()
        keyboard_listener.start()

        keyboard_listener.join()  # Wait until ESC is pressed

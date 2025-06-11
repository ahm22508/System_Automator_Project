import time
from pynput import mouse, keyboard
from Stop_Actions import Cut


actions = []
time_start = None
Recording = False

class Action:
    def on_press(key):
        if Recording:
            try:
                Key_Str = key.char
            except AttributeError:
                Key_Str = str(key)
                actions.append({
                    'type' : 'Key Press',
                    'key'  : Key_Str,
                    'time' : time.time() - time_start
                })

    def on_click(x , y , button , Pressed):
     if Recording:
         actions.append({
             'type' : 'Mouse_Click',
             'x' : x,
             'y' : y ,
             'button' : str(button) ,
             'Pressed' : Pressed,
             'time': time.time() - time_start

         })

    def Start_Recording():
        global actions, time_start , Recording
        actions = []
        time_start = time.time()
        Recording = True

        Mouse_Listener = mouse.Listener(on_click= Action.on_click)
        Keyboard_Listener = keyboard.Listener(on_press= Action.on_press , on_release=Cut.on_release) 

        Mouse_Listener.start()
        Keyboard_Listener.start()
        Keyboard_Listener.join()    
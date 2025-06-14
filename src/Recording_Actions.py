import time
from pynput import mouse, keyboard
from Stop_Actions import Cut
from ActionFileManagement import FileManaging

class Action(FileManaging):

    def __init__(self):
        self.actions = []
        self.time_start = None
        self.Recording = False



    def on_press(self ,key):
        if self.Recording:
            try:
                Key_Str = key.char
            except AttributeError:
                Key_Str = str(key)
            self.actions.append({
              'type' : 'Key_Press',
               'key'  : Key_Str,
               'time' : time.time() - self.time_start
                })

    def on_click(self,x , y , button , Pressed):
     if self.Recording:
         self.actions.append({
             'type' : 'Mouse_Click',
             'x' : x,
             'y' : y ,
             'button' : str(button) ,
             'Pressed' : Pressed,
             'time': time.time() - self.time_start

         })

    def Start_Recording(self):
            self.actions = []
            self.time_start = time.time()
            self.Recording = True
            FileManaging.actions = self.actions
            CutHandler = Cut(self.actions)    
            self.Mouse_Listener = mouse.Listener(on_click= self.on_click)
            self.Keyboard_Listener = keyboard.Listener(on_press= self.on_press , on_release=CutHandler.on_release) 

            self.Mouse_Listener.start()
            self.Keyboard_Listener.start()
            self.Keyboard_Listener.join()


import json
import os

class FileManaging:
    def __init__(self, actions):
        self.actions = actions
        self.filePath = os.getcwd()

    def update_Action_file(self):
        with open(self.filePath + "\Recorded_Actions.json" , "w") as file:
            json.dump(self.actions , file , indent=2)


    def load_Action_File(self):
       with open(self.filePath + "\Recorded_Actions.json" , "r") as file:
          self.actions = json.load(file)         
          return self.actions
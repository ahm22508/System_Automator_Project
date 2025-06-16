import json
import os

class FileManaging:


    def save(self , actions):
        with open(os.getcwd() + "\Recorded_Actions.json", "w") as file:
            json.dump(actions, file, indent=2) 

    def load(self):
        with open(os.getcwd() + "\Recorded_Actions.json", "r") as file:
            return json.load(file) 
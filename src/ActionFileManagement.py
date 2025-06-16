import json
import os

class FileManaging:
    def __init__(self):
        self.filepath = os.getcwd() + "\Recorded_Actions.json"

    def save(self, actions):
        with open(self.filepath, "w") as file:
            json.dump(actions, file, indent=2) 

    def load(self):
        with open(self.filepath, "r") as file:
            return json.load(file) 
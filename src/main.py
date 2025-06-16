from Recording_Actions import Action
from Replay_Actions import Replaying

class AutomationController:
    def __init__(self):
        self.action_recorder = Action()
        self.replayer = Replaying()
        self.running = True # Main loop control

    def display_menu(self):
        print("\n1. Start recording")
        print("2. Replay actions")
        print("3. Quit")

    def handle_choice(self, choice):
        if choice == "1":
            self.action_recorder.start_recording()
        elif choice == "2":
            self.replayer.replay_actions()
        elif choice == "3":
            self.running = False
        else:
            print("Invalid input.")

    def run(self):
        while self.running:
            self.display_menu()
            choice = input("Select: ").strip() # User input
            self.handle_choice(choice)

if __name__ == "__main__":
    controller = AutomationController()
    controller.run()
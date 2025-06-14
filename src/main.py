from Recording_Actions import Action
from Replay_Actions import Replaying


while True:
    print("\n1. Start recording\n2. Replay actions\n3. Quit")
    choice = input("Select: ").strip()

    if choice == "1":
        action = Action()
        action.Start_Recording()
    elif choice == "2":
       RedoActions = Replaying()
       RedoActions.replay_actions()

    elif choice == "3":
        break
    else:
        print("Invalid input.")
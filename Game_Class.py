from random import randint
class Game:
    def computer(self):
        return randint(0,2)
    def display(self,user_selection,computer_selection):
        print(f"Your Choice:\n{user_selection}")
        print(f"Computer Choice:\n{computer_selection}")

    def compare_user_computer(self,user_selection,computer_selection):
        print([user_selection,computer_selection])
        if user_selection == computer_selection:
            print("It is a Draw")
        elif (user_selection == 0 and computer_selection == 2) or (user_selection == 2 and computer_selection == 1) or (user_selection == 1 and computer_selection == 0):
            print("You Won")
        else:
            print("You Lost")







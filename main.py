from Game_Class import Game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_list=[rock,paper,scissors]
a=Game()
play=True
while play:
    print(f"'0' for Rock\n'1' for Paper\n'2' for Scissors")
    user_choice=int(input("Enter Your Choice:"))
    computer_choice=a.computer()
    a.display(game_list[user_choice],game_list[computer_choice])
    a.compare_user_computer(user_choice,computer_choice)
    continue_playing=input("Do you want to continue playing('y' for YES/'n' for NO):")
    if continue_playing=='n':
        play=False
    print("\n"*30)

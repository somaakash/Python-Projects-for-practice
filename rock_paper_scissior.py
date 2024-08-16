#importing random 
import random

user_choice=int(input("Enter your choice:Type 0 for rock ,Type 1 for paper , Type 2 for scissors"))
if (user_choice>=3 or user_choice <0):
    print("you have entered invalid number")
else:   
#using random function
    computer_choice=random.randint(0,2)
    print("computer chose:")
    print(computer_choice)

#implementing conditions

#for draw
    if (computer_choice==user_choice):
        print("It is a draw")

#0 means ROCK....2 means SECISSOR.
    elif (computer_choice == 0 and user_choice == 2):
          print("You Lose")

    elif (user_choice == 0 and computer_choice == 2):
          print("You Win")


#for lose
    elif(computer_choice > user_choice):
        print("You Lose.")

#for win
    elif(user_choice>computer_choice):
        print("You Win")
    

    


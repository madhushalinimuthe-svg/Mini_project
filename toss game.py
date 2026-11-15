""" TOSS GAME
user_input=heads_or_tails
computer_choice=heads_or_tails
computer choice equal to your choice then you win 
computer choice is not equal to your choice then you loss
"""
import random
item_list = ["heads","tails"]
user_input = input("choose heads or tails : ")
comp_choice = random.choice(item_list)
print(f"user choice = {user_input} ,  computer = {comp_choice}")
if comp_choice==user_input:
    print("your choice equal to computer choice : YOU WIN")
else:
    print("your choice is not equal to computer choice : YOU LOSS")

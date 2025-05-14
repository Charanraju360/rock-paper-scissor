import random

items=["rock", "paper", "scissor" ]

user_item = input("Enter the item (rock or paper or scissor):")
user_item = user_item.lower()

py_item = random.choice(items)
print(f"Python has selected {py_item} as item")

if user_item not in items:
    print('''Enter a valid item
          BYE BYE.........''')
    exit()
elif py_item == user_item:
    print("It's a tie")
elif py_item == "rock" and user_item == "scissor" or \
    py_item == "paper" and user_item == "rock" or \
    py_item == "scissors" and user_item == "paper":
    print("Python WON")
else:
    print("You WON")
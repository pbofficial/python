x = 15
price  = 9.99
discount = 0.2
result = price * (1 - discount)
print(result)

name = "Pritam"
print(name)

# -- While loop --

number = 7
play = input("Would you like to play (y/n): ")

while play != "n":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by 1")
    else:
        print("Sorry, its wrong!")

    play = input("Would you like to play (y/n): ")
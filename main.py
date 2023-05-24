#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_char = [letters, numbers, symbols]
new_pass = []
for char in range(nr_letters):
    if nr_letters > 0:
        random_letter = random.randint(0, 25)
        new_pass += letters[random_letter]
        nr_letters -= 1

for number in range(nr_numbers):
    if nr_numbers > 0:
        random_number = random.randint(0, 10)
        new_pass += numbers[random_number]
        nr_numbers -= 1
for symbol in range(nr_symbols):
    if nr_symbols > 0:
        random_symbol = random.randint(0, 8)
        new_pass += symbols[random_symbol]
        nr_symbols -= 1
print(new_pass)
random.shuffle(new_pass)
pass_string = ''
for new_char in new_pass:
    pass_string += new_char
print(pass_string)
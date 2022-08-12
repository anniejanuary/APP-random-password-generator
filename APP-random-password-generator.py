import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#    Order not randomised:

random_letters = random.choices(letters, k = nr_letters)
random_symbols = random.choices(symbols, k = nr_symbols)
random_numbers = random.choices(numbers, k = nr_numbers)

password_in_order_list = random_letters + random_symbols + random_numbers
password_in_order_str = ''.join(password_in_order_list)
print("Your password is:", password_in_order_str)


#     Order of characters randomised:

password_length = nr_letters + nr_symbols + nr_numbers
password_shuffled_list = random.sample(password_in_order_str, password_length)
password_shuffled_str = ''.join(password_shuffled_list)
print("Your shuffled password is:", password_shuffled_str)

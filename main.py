# This function will print the menu
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit ")
    print()
def password_encoder(password):
    encoded = ""
    pass_as_char = str(password)
    for number in pass_as_char:
        appendage = int(number) + 3
        encoded += str(appendage)
    encoded = int(encoded)
    return encoded


# This is the main function
if __name__ == "__main__":
    running = True
    while running:
        print_menu()
        user_input = int(input("Please enter an option: "))
        if user_input == 1:
            original_password = int(input("Please enter your password to encode: "))
            encoded_password = password_encoder(original_password)
            print("Your password has been encoded and stored!")
            print(encoded_password)
        elif user_input == 2:
            pass
        else:
            pass

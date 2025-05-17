import string
import random
import time
from termcolor import colored

def generate_password(length=8, type='alpha', number_of_passwords=1, save=False):
    if type == 'alpha':
        characters = string.ascii_letters
    elif type == 'alphanumeric':
        characters = string.ascii_letters + string.digits
    elif type == 'full':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print(colored("Invalid password type. Use 'alpha', 'alphanumeric', or 'full'.", 'red'))
        return []

    password_list = [''.join(random.choice(characters) for _ in range(length)) for _ in range(number_of_passwords)]

    if save:
        with open('wordlist.txt', 'w') as f:
            for pw in password_list:
                f.write(pw + '\n')
        print(colored("Passwords have been saved to 'wordlist.txt'.", 'green'))

    return password_list

number_of_characters = int(input(colored("How many characters should the passwords have? ", 'green')))
number_of_passwords = int(input(colored("How many passwords do you want to generate? ", 'green')))
password_type = input(colored("Do you want 'alpha', 'alphanumeric', or 'full' (with symbols)? ", 'green')).lower()
save_to_file = input(colored("Do you want to save the passwords in a wordlist.txt file? (yes/no) ", 'green')).strip().lower() == 'yes'

passwords = generate_password(number_of_characters, password_type, number_of_passwords, save_to_file)

print(colored("\n--- Start Password Generation ---", 'yellow'))
for i, pw in enumerate(passwords, 1):
    print(colored(f"\nPassword {i}: ", 'cyan') + colored(pw, 'green'))
    print(colored("---", 'magenta'))
    time.sleep(0.5)

print(colored("\n--- End Password Generation ---", 'yellow'))

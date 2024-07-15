import random
import string

def main(password_length):
    characters = string.ascii_letters + string.punctuation + string.digits
    password = ''.join(random.choice(characters) for i in range(password_length))
    return password

try:
    password_length = int(input('Please input the length of the Password: '))

    if password_length <= 0:
        print('Password Length should be Positive')
    elif password_length > 0:
        generated_password = main(password_length)
        print('Generated Password: ', generated_password)
except ValueError:
    print("Invalid Input! Password Length should be Integer")





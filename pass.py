import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    try:
        length = int(input("Enter the length for the password: "))
        
        if length < 1:
            print("enter a positive number for the password length.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("enter a valid number for the password length.")
if __name__ == "__main__":
    main()

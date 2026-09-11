# Password Generator Python Program
import sys
import random

def main():
    fpath = f"C:\\users\\andre.lemos\\downloads\\password.txt"

    with open(fpath, "w") as file:

        def generate_password(username, length):
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
            password = "".join(random.choice(characters) for _ in range(length))
            print(f'{username}: {password}', file=file)

        generate_password(username, length)

if __name__ == "__main__":
    username = sys.argv[1]
    length = int(sys.argv[2])
    main()
import bcrypt
import sys
import os

def read_hashes():
    with open('hash.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]

def read_passwords():
    with open('pass1.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]

def write_success(hashed, password):
    with open('success.txt', 'a') as f:
        f.write(f"{hashed} : {password}\n")

def remove_line(filename, line_to_remove):
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            if line.strip() != line_to_remove:
                f.write(line)

def brute(passwords, hashed):
    print(f"Processing hash: {hashed}")
    c = 0
    for passwdstr in passwords:
        c += 1
        passwd = passwdstr.encode('UTF-8')
        hashed_bytes = hashed.encode('UTF-8')
        if bcrypt.checkpw(passwd, hashed_bytes):
            write_success(hashed, passwdstr)
            remove_line('hash.txt', hashed)
            return
        sys.stdout.write(f"{passwdstr} does not match this hash.{c} passwords tried so far. \033[0m\033[0K\r")
        sys.stdout.flush()

def main():
    passwords = read_passwords()
    hashes = read_hashes()

    for hashed in hashes[:]:  # Using a copy of the list to allow modifications
        brute(passwords, hashed)

if __name__ == "__main__":
    main()


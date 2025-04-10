from banking_pkg import account



def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")
# User Input and Name Length Verification
print("          === Automated Teller Machine ===          ")

while True:
    name = input("Enter name to register: ")
    if 1 <= len(name) <= 10:
        break
    else:
        print("Input must be between 1 and 10 characters long. Please try again.")
while True:
    pin = input("Enter PIN to register: ")
    if len(pin) > 4:
        print("PIN may only be 4 characters. Try again.")
    else:
        break
balance = 0
print(f"{name} has been registered with a starting balance of ${balance}")
# Name Length Validation


print("Login to Account")
print("--------------------------------------")
while True:
    user_name = input("Enter Name: ")
    user_pin = input("Enter PIN: ")
    if user_name == name and user_pin == pin:
        print("Login Successful!")
        break
    else:
        print("Invalid credentials! Please try again.")
        
# ATM Menu
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        print(account.show_balance(balance))
    elif option == "2":
        balance = account.deposit(balance)
    elif option == "3":
        balance = account.withdraw(balance)
    elif option == "4":
        account.logout(name)
    break


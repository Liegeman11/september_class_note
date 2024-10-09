#  Build an ATM machine using function

# # solution

# # balance = 500,000,000,000

# # user=input("""welcome to USSD Banking. N6.98 network Charge will apply to your account \nfor banking service on this channel. press 1 to accept or 2 to reject >>>
# #                                         1.Accept
# #                                         2.Reject

def login():
    pin ='1234'
    attempt =3
    while attempt > 0:
        input_pin=input('Enter your pin: ')
        if input_pin == pin:
            print('login Succesful')
            return True
        else:
            attempt -= 1
            if attempt > 0:
                print(f'Incorrect Pin. you have {attempt} attempt left')
            else:
                print('Too many attempt. existing')
            return False
        


def check_balance(balance):
    print(f'Your current balance is: #{balance}.')

def transfer(balance):
    if balance <= 0:
        print('Insufficient balance for transfer')
        return balance
    account_number=input("Enter the recipient's 10-digit account number: ")
    if len(account_number) != 10 or not account_number.isdigit():
        print('Invalid account number. Must be 10 digit')
        return balance
    amount =input('Enter the amount: ')
    if amount <=0:
        print('Transfer must be greater than zero')
    elif amount > balance:
        print('Insufficient funds for this Transfer')
    else:
        balance -= amount
        print(f'Successfully transfer #{amount} to account {account_number}')
        check_balance(balance)
        return balance
def withdraw(balance):
    amount = int(input("Enter amount to withdraw: "))
    if 0 < amount <= balance:
        balance -= amount
        print(f"#{amount} has been withdrawn.")
    elif amount > balance:
        print("Insufficient funds.")
    else:
        print("Invalid amount. Please enter a positive number.")
    return balance
def main():
    balance= 5000
    
    if login():
        while True:
            print("""\n=== ATM Main Menu ===
                        1. Check Balance
                        2. Transfer Money
                        3. Withdraw Money
                        4. Exit
""")
            choice=input('Choose an option (1-4): ')
            
            # print("\n=== ATM Main Menu ===")
            # print("1. Check Balance")
            
            # print("2. Transfer Money")
            # print("3. Withdraw Money")
            # print("4. Exit")

            if choice == '1':
                check_balance(balance)
            elif choice == '2':
                balance = transfer(balance)
            elif choice == '3':
                balance = withdraw(balance)
            elif choice == '4':
                exit()
                print('Log out successfully. Thanks for using the ATM machine.')
            else:
                print('Invalid choice. Please select a valid option.')
# main()


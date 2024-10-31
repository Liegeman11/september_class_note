                            #          Bank USSD Code         #


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
def display_menu():
    print('Welcome to Bank USSD Service')
    print('1. Check balance')
    print('2. Buy Airtime')
    print('3. Transfer')
    print('4. Exit')
def Check_balance(balance):
    print(f'Your current balance is #{balance}')
def buy_airtime(balance):
        phone_number = input("Enter the recipient's phone number: ")
        if len(phone_number) != 11 or not phone_number.isdigit():
            print('Invalid phone number. Must be 11 digits.')
            return
        airtime_amount = float(input('Enter the amount: '))
        if airtime_amount <= 0:
            print('Transfer amount must be greater than zero.')
        elif airtime_amount > balance:
            print('Insufficient funds for this transfer.')
        else:
            balance -= airtime_amount
            print(f'Successfully transferred #{airtime_amount} to this phone number:{phone_number}.')
            # self.check_balance()
            print(f"Remaining balance: #{balance}")
def transfer(balance):
    if balance <= 0:
        print('Insufficient balance for transfer')
        return balance
    account_number = input("Enter the recipient's 10-digit account number: ")
    if len(account_number) != 10 or not account_number.isdigit():
        print('Invalid account number. Must be 10 digits.')
        return balance
    amount = input('Enter the amount: ')
    if not amount.isdigit():
        print('Invalid amount. Please enter a number.')
        return balance
    amount = int(amount)
    if amount <= 0:
        print('Transfer amount must be greater than zero.')
    elif amount > balance:
        print('Insufficient funds for this transfer.')
    else:
        balance -= amount
        print(f'Successfully transferred #{amount} to account {account_number}.')
        Check_balance(balance)
    return balance
def main():
    service_code='*435#'
    user_code=input("Enter USSD code to access bank service: ")
    if user_code != service_code:
        print("Invalid code. Access denied.")
        return
    balance = 300000
    if login():
        while True:
            display_menu()
            choice = input('Enter your choice: ')
            if choice == '1':
                Check_balance(balance)
            elif choice == '2':
                balance = buy_airtime(balance)
            elif choice == '3':
                balance = transfer(balance)
            elif choice == '4':
                print('Thanks for using our service!')
                break
            else:
                print('Invalid choice. Please try again.')
main()

    
    








































#     if user == '1':
#             print('Welcome to Bank USSD Service')
#             return True
#     else:
#             print('USSD Terminated')
#             return False
# def reg(self):
#     self.pin= '1234'
#     self.service_code='*435#'
    
    
# def display_menu():
#     print('welcome to Bank USSD Service')
#     print('1. check balance')
#     print('2. Transfer')
# def Check_balance(balance):
#     print(f'Your current balance is #{balance}')
# def transfer(balance):
#     if balance <= 0:
#         print('Insufficient balance for transfer')
#         return balance
#     account_number=input("Enter the recipient's 10-digit account number: ")
#     if len(account_number) != 10 or not account_number.isdigit():
#         print('Invalid account number. Must be 10 digit')
#         return balance
#     amount =input('Enter the amount: ')
#     if amount <=0:
#         print('Transfer must be greater than zero')
#     elif amount > balance:
#         print('Insufficient funds for this Transfer')
#     else:
#         balance -= amount
#         print(f'Successfully transfer #{amount} to account {account_number}')
#         check_balance(balance)
#         return balance
# def main():
#     balance=300000
#     while True:
#         display_menu()
#         choice= input('Enter your Choice: ')
#         if choice =='1':
#             Check_balance(balance)
#         elif choice =='2':
#             balance = transfer(balance)
#         elif choice =='3':
#             print('Thanks for using our service!')
#             break
#         else:
#             print('Invalid choice. please try again.')
# main()
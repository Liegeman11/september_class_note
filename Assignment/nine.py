
# def display_menu():
#     user=input("""welcome to USSD Banking. N6.98 network Charge will apply to your account \nfor banking service on this channel. press 1 to accept or 2 to reject >>>
#                                         1.Accept
#                                             2.Reject
# """)
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
                
                

def display_menu():
    print('Welcome to Bank USSD Service')
    print('1. Check balance')
    print('2. Transfer')
    print('3. Exit')

def Check_balance(balance):
    print(f'Your current balance is #{balance}')

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
    balance = 300000
    while True:
        display_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            Check_balance(balance)
        elif choice == '2':
            balance = transfer(balance)
        elif choice == '3':
            print('Thanks for using our service!')
            break
        else:
            print('Invalid choice. Please try again.')

main()

    
    
    
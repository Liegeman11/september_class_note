
class BankUSSD:
    balance = 100000 

    def __init__(self, pin, service_code):
        self.pin = pin
        self.service_code = service_code 
        self.access_granted = False

    def main(self):
        entered_code = input("Enter USSD code (e.g., *234#): ")
        self.access_service(entered_code)
        
        if self.access_granted:
            while True:
                self.display_menu()
                choice = input("Please select an option: ")
                
                if choice == '1':
                    self.buy_airtime()
                elif choice == '2':
                    self.check_balance()
                elif choice == '3':
                    self.transfer()
                elif choice == '4':
                    self.withdraw()
                elif choice == '5':
                    print("Thank you for using our service.")
                    break
                else:
                    print("Invalid option selected. Please try again.")

    def display_menu(self):
        print("Welcome to Bank USSD Service")
        print("1. Buy Airtime")
        print("2. Check Balance")
        print("3. Transfer")
        print("4. Withdraw")
        print("5. Exit")

    def access_service(self, entered_code):
        if entered_code == self.service_code:
            self.access_granted = True
            print("Access granted to USSD service.")
        else:
            print("Incorrect USSD code. Access denied.")
            exit()

    def verify_pin(self, entered_pin):
        return entered_pin == self.pin

    def deduct_service_fee(self):
        service_fee = 5
        if BankUSSD.balance >= service_fee:
            BankUSSD.balance -= service_fee
            return True
        else:
            print("Insufficient balance to cover the service fee.")
            return False

    def buy_airtime(self):
        entered_pin = input("Enter your PIN to confirm: ")
        if not self.verify_pin(entered_pin):
            print("Incorrect PIN. Transaction canceled.")
            return
        phone_number = input("Enter the recipient's phone number: ")
        
        if len(phone_number) != 11 or not phone_number.isdigit():
            print('Invalid account number. Must be 10 digits.')
            return
        airtime_amount = float(input('Enter the amount: '))
        if airtime_amount <= 0:
            print('Transfer amount must be greater than zero.')
        elif airtime_amount > BankUSSD.balance:
            print('Insufficient funds for this transfer.')
        else:
            BankUSSD.balance -= airtime_amount
            print(f'Successfully transferred #{airtime_amount} to this phone number:{phone_number}.')
            # self.check_balance()
            print(f"Remaining balance: #{BankUSSD.balance}")

    def check_balance(self):
        entered_pin = input("Enter your PIN to confirm: ")
        if not self.verify_pin(entered_pin):
            print("Incorrect PIN. Transaction canceled.")
            return
        else:
            print(f'Your current balance is: #{BankUSSD.balance}.')
            
    def transfer(self):
        entered_pin = input("Enter your PIN to confirm: ")
        if not self.verify_pin(entered_pin):
            print("Incorrect PIN. Transaction canceled.")
            return

        if BankUSSD.balance <= 0:
            print('Insufficient balance for transfer')
            return
        
        account_number = input("Enter the recipient's 10-digit account number: ")
        if len(account_number) != 10 or not account_number.isdigit():
            print('Invalid account number. Must be 10 digits.')
            return
        
        amount = float(input('Enter the amount: '))
        if amount <= 0:
            print('Transfer amount must be greater than zero.')
        elif amount > BankUSSD.balance:
            print('Insufficient funds for this transfer.')
        else:
            BankUSSD.balance -= amount
            print(f'Successfully transferred #{amount} to account {account_number}.')
            # self.check_balance()
            print(f"Remaining balance: #{BankUSSD.balance}")

    def withdraw(self):
        entered_pin = input("Enter your PIN to confirm: ")
        if not self.verify_pin(entered_pin):
            print("Incorrect PIN. Transaction canceled.")
            return

        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= BankUSSD.balance:
            BankUSSD.balance -= amount
            print(f"#{amount} has been withdrawn.")
            self.check_balance()
        elif amount > BankUSSD.balance:
            print("Insufficient funds.")
        else:
            print("Invalid amount. Please enter a positive number.")
bank_ussd = BankUSSD(pin="1234", service_code="*234#")
bank_ussd.main()
# class Bank:
#     name = "Onyx Bank Limited"
#     motto = "Transaction made esay for all"
#     location = "Ijebu Remo"
    
# uba =Bank()
# uba.name = "united Banks for african"
# uba.motto = "everything we do, we do it well"
# uba.location = "lagos"
# fidelity =Bank()
# access =Bank()
# wema =Bank()
# zenith =Bank()
# first =Bank()
# print(uba.name)
# for each in (uba.name, fidelity.name, access.name, wema.name ):
#     print(each)
    
class Bank:
    balance =0
    def __init__(self,name, motto, location):
        self.name=name
        self.motto =motto
        self.location =location
    def saving(self):
        user_inp=int(input('enter the amount to save:'))
        print(f'your initial balance is {self.balance}')
        self.balance += user_inpprint(f'thank you for saving{user_inp} with {self.name}')
    def check_bal(self):
        return self.balance
uba = Bank("uba", "everything we do, we do it well", "lagos")
fidelity = Bank("uba", "we do everything", "lagos")
fidelity =


class ATM(object):
    def __init__(self, cardNumber, pinNumber):
        self.balance = int(5000)
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber

    def balanceEnquiry(self):
        print('Your Balance is ' + str(self.balance) + ' dollars.')

    def cashWithdrawl(self):
        withdrawAmmount = int(input('How much money you want to withdraw?\n'))

        if(withdrawAmmount <= int(self.balance)):
            self.balance = self.balance - withdrawAmmount
            print('Money Withdrawn')
        else:
            print('You dont have enough money to withdraw')

    def addMoney(self):
        moneyAdding = int(input("How much money you want to add? \n"))
        self.balance = self.balance + moneyAdding
        print('Money added')

    def balanceEnquiry(self):
        print('Your Balance is ' + str(self.balance) + ' dollars.')


ATM = ATM(789789, 87878)

ATM.cashWithdrawl()
ATM.balanceEnquiry()

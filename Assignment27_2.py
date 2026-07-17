class BankAccount:
    ROI = 10.5
    def __init__(self,name,amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Account holder: ", self.Name)
        print("Account balance: ", self.Amount)

    def Deposite(self):
        DepositAmount = int(input("Enter the deposit amount: "))
        self.Amount = self.Amount + DepositAmount

    def Withdraw(self):
        WithdrawAmount = int(input("Enter the withdraw amount: "))
        if(WithdrawAmount <= self.Amount):
            self.Amount = self.Amount - WithdrawAmount
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        Interest = (self.Amount*BankAccount.ROI)/100
        print("Interest is: ", Interest)

bobj = BankAccount("Anuj", 20000)
bobj.Display()
bobj.Deposite()
bobj.Display()
bobj.CalculateInterest()
bobj.Withdraw()
bobj.Display()
bobj.CalculateInterest()



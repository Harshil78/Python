class accountHolder:
    def __init__(self):
        self.accNo=int(input("Enter Account No:-"))
        self.accName = input("Enter Account Holder Name:-")
        self.accEmail = input("Enter Account Holder Email Address:-")

    def dispDetails(self):
        print("")
        print("Holder Details")
        print("------------------------------------------")
        print("AC Number :-",self.accNo)
        print("AC Name :-",self.accName)
        print("AC Email :-",self.accEmail)
        print("==========================================")


class depositAccount(accountHolder):
    def debitAmt(self):
        self.accountBalance = int(input("Enter AC Balance:-"))
        self.initialBal = self.accountBalance
        print("")
        self.debitAmount=int(input("Enter Debit Amount:-"))
        remainAmount = self.accountBalance - self.debitAmount
        self.accountBalance = remainAmount
        self.disTrans("DebitAmount", self.debitAmount)

    def creditAmt(self ):
        print("")
        self.creditAmount = int(input("Enter Credit Amount:-"))
        remainAmount = self.accountBalance + self.creditAmount
        self.accountBalance = remainAmount
        self.disTrans('CreditAmount', self.creditAmount )

    def disTrans(self, transType, amount):
        print('-' * 30)
        if (transType == "DebitAmount"):
            print(f'Intial Balance : {self.initialBal}')
            print(f'DebitAmount : {amount}')
            print(f'FinalAmount : {self.accountBalance }')
            print('-' * 30)
        if (transType == "CreditAmount"):
            print(f'Intial Balance : {self.initialBal}')
            print(f'CreditAmount : {amount}')
            print(f'FinalAmount : {self.accountBalance}')
            print('-' * 30)


class loanAccount():
    def __init__(self):
        print(" ")
        self.loanAmount = int(input("Enter Loan Amount:-"))
        self.EMI = int(input("Enter EMI Amount:-"))
        self.installments=int(input("Number Of Installments Has Been Paid:-"))
        self.loanBalance = self.loanAmount-self.EMI*self.installments

    def dispLoanDetails(self):
        if self.loanBalance>self.loanAmount:
            print('-' * 30)
            print(f'LoanAmount : {self.loanAmount}')
            print(f'EMI : {self.EMI}')
            print(f'EMI Paid : {self.installments}')
            print(f'Remaining Loan Balance : {self.loanBalance}')
        else:
            print("Your Has Been Completed")

objDeposit = depositAccount()
objDeposit.dispDetails()
objDeposit.debitAmt()
objDeposit.creditAmt()
objLoan = loanAccount()
objLoan.dispLoanDetails()
# a=accountHolder()
# a.dispDetails()
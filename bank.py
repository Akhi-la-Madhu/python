class bankaccount:
    def getData(self,name,accno,acctype,balance):
        self.name=name
        self.accno=accno
        self.acctype=acctype
        self.balance=balance
    def displayCustomer(self):
        print("Customer name:",self.name)
        print("Account number:",self.accno)
        print("Account type:",self.accno)
        print("Account balance:",self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Account balance:",self.balance)
    def withdrawal(self,amount):
        if self.balance-amount<0:
            print("Insufficient balance")
        else:
            self.balance=self.balance-amount
            print("Amount withdrawn")
            print("Account balance:",self.balance)
print("HELLO WELCOME TO BANKING SYSTEM")
ch=0
obj=bankaccount()
while ch!=5:
    print("Select your choice")
    print("1.New customer")
    print("2.Deposit")
    print("3.Withdrawel")
    print("4.Display")
    print("5.Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        obj=bankaccount()
        n=input("Enter name:")
        no=int(input("Enter account no:"))
        t=input("Enter Account type(SB/C):")
        b=int(input("Enter Amount:"))
        obj.getData(n,no,t,b)
    if ch==2:
            b=int(input("Enter the amount to be deposit:"))
            obj.deposit(b)
    if ch==3:
            b=int(input("Enter the amount to be withdrawn:"))
            obj.withdrawal(b)
    if ch==4:
            obj.displayCustomer()
    else:
        print("Program terminated !!!")
            
    

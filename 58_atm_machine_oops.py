# details as per the mobile number
# pin
# options 1. withdrwal 2. check blance 3. change pin 4. acount statement
# amount 100,200,500,1000,2000
# balnce = balance-entered amount = current balance
# reciept = y=balance n=pls collect your card

class CustomerDetail:

    def customerData(self):
        name = ""
        dob = ""
        mobileno = ""
        pin = ""
        accBal = 0
        amount = 0
        fbal = ""

        self.fbal = fbal
        self.name = name
        self.dob = dob
        self.mobileno = mobileno
        self.pin = pin
        self.accBal = accBal
        self.amount = amount
        

    def showPerInfo(self):
        print("********** Account Information **********")
        print(f"Account Holder Name: {self.name} ")
        print(f"Date of Birth: {self.dob}")
        print(f"Register Mobile No: {self.mobileno}")
        with open(f"{self.name}.txt", "w") as f:
            f.write(
                f"Account Holder Name: {self.name}\nDate of Birth:{self.dob}\nRegister Mobile No:{self.mobileno}")

    
    def deposit(self):
        print("********** Deposit Process **********\n")
        self.amount = int(input("Enter Amount:"))
        

        self.accBal = self.accBal + self.amount

        with open(f"{self.name}Balence.txt", "w") as f:
            print(f"Current Balence:{self.accBal}")
            f = f.write(f"{self.accBal}")

    def withdwal(self):
        print("\n********** Withdrwal Process **********")
        self.amount = int(input("Enter Amount:"))

        self.accBal= self.accBal- self.amount

        with open(f"{self.name}Balence.txt", "w") as f:
            f = f.write(f"{self.accBal}")
        check_bal = int(input("For Check Balence(1):"))

        if check_bal == 1:
            self.checkBal()
        else:
            exit()

    def checkBal(self):
        print("\n********** Account Balence **********")
        with open(f"{self.name}Balence.txt", "r") as f:
            f = f.read(self.accBal)
            print(f"Currnt Balence:{str(f)}")
            print("\n********** Thank you For Banking With Us **********")

    def machineInt(self):
        print("********** Banking Options **********\n")
        print("Withdwal(1)\nDeposit(2)\nCheckBalence(3)\nAccount Detail(4)")
        choice = int(input("Your Choice: "))

        if choice == 1:
            self.withdwal()

        elif choice == 2:
            self.deposit()


        elif choice == 3:
            self.checkBal()

        elif choice == 4:
            self.showPerInfo()

        else:
            print("Enter Valid Option")

    


####### Customer Information ######
dhrumil = CustomerDetail()
fannie = CustomerDetail()
rina = CustomerDetail()
krishna = CustomerDetail()

dhrumil.name = "Dhrumil Piyush Patel"
dhrumil.dob = "30/07/2004"
dhrumil.mobileno = +917802032338
dhrumil.pin = 2664
dhrumil.cusid = 1
dhrumil.accBal = 500
dhrumil.fbal = ""

rina.name = "Rina Piyush Patel"
rina.dob = "27/04/1983"
rina.mobileno = +9188449512
rina.pin = 3701
rina.cusid = 3
rina.accBal = 500

krishna.name = "Krishna Piyush Patel"
krishna.dob = "28/08/2013"
krishna.mobileno = +91884412345
krishna.pin = 1234
krishna.cusid = 4
krishna.accBal = 500

##### Machine Interface #####

print("********** Welcome To Patel Atm **********\n")

cusid = int(input("Enter Your Customer Id: "))

pin = int(input("Enter Your Pin: "))

if cusid == 1 and pin == 2664:
    print("***** Pin is verified *****\n")
    dhrumil.machineInt()

elif cusid == 2 and pin == 2330:
    print("***** Pin is verified *****\n")
    fannie.machineInt()

elif cusid == 3 and pin == 3701:
    print("***** Pin is verified *****\n")
    rina.machineInt()

elif cusid == 4 and pin == 1234:
    print("***** Pin is verified *****\n")
    krishna.machineInt()


else:
    print("\nInvalid Customer Id or Pin")

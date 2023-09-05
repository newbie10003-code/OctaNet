# Create an ATM machine
# Steps to perform
# 1. Display the ATM welcome message
# 2. Ask the user to enter the 4 digit pin
# 3. If the pin is correct, display the menu
# 4. If the pin is incorrect, display the error message
# 5. If the user selects the option 1, display the balance
# 6. If the user selects the option 2, ask the user to enter the amount to withdraw
# 7. If the user selects the option 3, ask the user to enter the amount to deposit
# 8. If the user selects the option 4, display the ATM thank you message
# 9. If the user selects any other option, display the error message
# 10. Ask the user to enter the option to continue or not
# 11. If the user selects the option 1, continue the process from step 5
# 12. If the user selects the option 2, display the ATM thank you message

accountNo = 1234567890
pin = 1234
balance = 10000
transHistory = {"Date" : ["Type", "Amount"],
                "20-08-2023" : ["Credit", "2000"],
                "22-08-2023" : ["Debit", "1000"],
                "27-08-2023" : ["Debit", "500"],
                "31-08-2023" : ["Credit", "1000"]}
flag = False

class ATM:
    def __init__(self) -> None:
        print("Welcome to XYZ Bank Atm")
        print("Please insert your card")
        self.accountType = int(input("Select account type: \n1. Current Account \n2. Savings Account\n"))
        self.accountNo = accountNo
        self.pin = pin
        self.balance = balance
        self.transHistory = transHistory

    def transferHistory(self):
        for i in user.transHistory:
            print(i, " ", user.transHistory[i])

    def withdraw(self):
        amt = int(input("Enter the amount you want to withdraw: "))
        if amt > self.balance:
            print("Insufficient amount! Please update balance to withdraw")
        else:
            self.balance -= amt
            print("Amount successfully withdrawn!")
            print("Updated balance is: ", self.balance)

    def deposit(self):
        amt = int(input("Enter the amount you want to deposit: "))
        self.balance += amt
        print("Successfully deposited!")
        print("Updated balance is: ", self.balance)

    def transfer(self):
        amt = int(input("Enter the amount you want to transfer: "))
        accNo = int(input("Enter the account number you want to transfer to: "))
        if amt > self.balance:
            print("Insufficient amount! Please update balance to transfer")
        else:
            self.balance -= amt
            print(f"Amount: {x} successfully transfered to {y}!", y = accNo, x = amt)
            print("Updated balance is: ", self.balance)

tries = 3
user = ATM()
while True:
    while tries != 0:
        flag = False
        pin = int(input("Please enter your pin number: "))
        if pin != user.pin:
            print("Wrong pin entered! Please enter the correct pin to continue")
            flag = True
            tries -= 1
            continue
        else:
            print("Value of tries: ", tries)
            tries = 0
            print("Updated Value of tries: ", tries)
            flag = False
            break
    
    if flag:
        break

    choice = int(input("Please select option: \n1. View transaction history \n2. Withdraw \n3. Deposit \n4. Transfer \n5. Quit\n"))
    if choice == 5:
        break

    if choice == 1:
        print("====================================================================")
        user.transferHistory()
        print("====================================================================")
        
    if choice == 2:
        print("====================================================================")
        user.withdraw()
        print("====================================================================")
    
    if choice == 3:
        print("====================================================================")
        user.deposit()
        print("====================================================================")

    if choice == 4:
        print("====================================================================")
        user.transfer()
        print("====================================================================")
    
    else:
        continue

if flag:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("No of tries exceeded! Your card has been temporarily blocked for the day")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    print("Thank you for coming!")
    print("====================================================================")
import mysql.connector as sql
import random
import sys

mycon=sql.connect(host='127.0.0.1', user="root", password="shot-010907")
print(mycon)
mycursor=mycon.cursor()
print('done')
mycursor.execute("CREATE DATABASE atm_store_db")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)

mycon = sql.connect(host='127.0.0.1', user="root", password="shot-010907", database="atm_store_db")
mycursor = mycon.cursor()

mycursor.execute("CREATE TABLE customers_table(customer_id INT PRIMARY KEY AUTO_INCREMENT, First_name VARCHAR(20), Last_name VARCHAR(20), Date_of_birth VARCHAR(10), Email VARCHAR(30), Account_no BIGINT, Created_pin INT(4), Acc_balance FLOAT)")

mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)
    
    
class Bank:
    def __init__(self):
        self.atm_machine()
    def atm_machine(self):
        print('''
            Welcome to Reality Bound Bank
            
            Do you have an Account?
            1. Yes
            2. No
            ''')
        user=input('select option: ')
        if user == '1':
            self.login()
        elif user == '2':
            self.sign_up()
        
    def sign_up(self):
        print("Sign Up selected.")
        First_name = input('Enter your first name: ')
        Last_name = input('Enter your last name: ')
        Date_of_birth = input('Enter your date of birth: ')
        Email = input('Enter your email: ')
        Account_no = random.randint(1111111111, 9999999999)
        Created_pin = int(input('Generate your pin: '))
        Acc_balance = 0
        
        query = 'INSERT INTO customers_table(First_name,Last_name, Date_of_birth, Email, Account_no, Created_pin, Acc_balance) VALUE(%s,%s,%s,%s,%s,%s,%s)'
        val = (First_name, Last_name, Date_of_birth, Email, Account_no, Created_pin, Acc_balance)
        mycursor.execute(query,val)
        mycon.commit()
        print(mycursor.rowcount, 'row added')
        print("account creation is successfully.")
        print(f"Congratulation {First_name} {Last_name}, your pin {Created_pin} have been accepted")
        print(f"Your Account number is {Account_no}, your account balance is {Acc_balance}, pls make your first deposit!")
        print(f"Welcome, thank you for choosing Reality bound bank")
        self.atm_machine()
        
    def login(self):
        print("Login selected.")
        self.Account_no = input('Enter your account number: ')
        Pin = input('Enter your pin: ')
        query = 'SELECT * FROM customers_table WHERE Account_no = %s and Created_pin = %s'
        val = (self.Account_no, Pin)

        mycursor.execute(query,val)
        info = mycursor.fetchall()
        print(info)
        if info:
            self.home_page()
            
    def home_page(self):
            print('''
                1. Deposit
                2. Withdraw
                3. Transfer
                4. Account balance
                5. back
                6. Close account
                7. Exit
                ''')
            choice = input('select operation: ')
            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.transfer()
            elif choice == '4':
                self.account_balance()
            elif choice == '5':
                self.back()
            elif choice == '6':
                self.close_account()
            elif choice == '7':
                self.exit()
        
    def deposit(self):
        print('Deposit selected')
        amount = int(input("Enter amount: $"))
        Account_no = input("Enter account number: ")
        base = ("SELECT * FROM customers_table WHERE Account_no = %s")
        data = [Account_no]
        mycursor.execute(base,data)
        result = mycursor.fetchall()
        # print(result)
        current_balance = result[0][7]
        new_balance = int(current_balance) + int(amount)
        query = ('UPDATE customers_table SET Acc_balance = %s WHERE Account_no = %s')
        current = (new_balance, Account_no)
        mycursor.execute(query,current)
        mycon.commit()
        print(f"Deposit of ${amount}is successful")
        print(f"Your new Account balance is ${new_balance}")
        self.home_page()
        
    def withdraw(self):
        print('Withdraw selected')
        amount = int(input("Enter amount: $"))
        pin = input("Enter pin: ")
        base = ("SELECT * FROM customers_table WHERE Account_no = %s")
        data = [self.Account_no]
        mycursor.execute(base,data)
        result = mycursor.fetchall()
        current_balance = result[0][7]
        if int(current_balance) >= int(amount):
            new_balance = int(current_balance) - int(amount)
            query =  ('UPDATE customers_table SET Acc_balance = %s WHERE Account_no = %s')
            current = (new_balance,self.Account_no)
            mycursor.execute(query,current)
            mycon.commit()
            print(f"Withdrawal of ${amount} is successful")
            print(f"Your new Account balance is ${new_balance}")
            self.home_page()
        else:
            print(f"insufficient balance")    
            self.home_page()
            
    def transfer(self):
        print('transfer selected')
        bank = input("Enter name of bank: ")
        Account_no2 = input("Enter receiver account number: ")
        base = ("SELECT * FROM customers_table WHERE Account_no = %s")
        amount = int(input("Enter amount: $"))
        data = [self.Account_no]
        mycursor.execute(base,data)
        result = mycursor.fetchall()
        current_balance = result[0][7]

        base2 = ("SELECT * FROM customers_table WHERE Account_no =%s")
        data2 = [Account_no2]
        mycursor.execute(base2,data2)
        result2 = mycursor.fetchall()
        current_balance2 = result2[0][7]
        if int(current_balance) >= int(amount):
            new_balance = int(current_balance) - int(amount)
            query = ('UPDATE customers_table SET Acc_balance = %s WHERE Account_no = %s')
            current = (new_balance, self.Account_no)
            mycursor.execute(query,current)
            mycon.commit()
            
            new_balance2 = int(current_balance2) + int(amount)
            query = ('UPDATE customers_table SET Acc_balance = %s WHERE Account_no = %s')
            current = (new_balance2, Account_no2)
            mycursor.execute(query,current)
            mycon.commit()
            print(f"transfer of ${amount} to {Account_no2} is successful")
            print(f"Your new Account balance is ${new_balance}")
            self.home_page()
        else:
            print("insufficient balance")
            self.home_page()

    def account_balance(self):
        print('Account balance selected')
        base = ("SELECT * FROM customers_table WHERE Account_no = %s")
        data = [self.Account_no]
        mycursor.execute(base, data)
        result=mycursor.fetchone()
        print(result)
        self.home_page()
        
    def back(self):
        print('''
            Are you sure you want to go back!
            1. Yes
            2. No
            ''')
        choose = input('Take a choice: ')
        if choose == '1':
            print('Back selected')
            self.atm_machine()
        elif choose == '2':
            self.home_page()
        else:
            print('invalid choice!')
            self.back()
    
    def close_account(self):
        print('''Are you sure you want to close your account with us
            1. Yes
            2. No
            ''')
        choice = input('Take a choice: ')
        if choice == '1':
            print('Close account selected')
            sql = "delete from customers_table WHERE Account_no = %s"
            data=[self.Account_no]
            mycursor.execute(sql,data)
            mycon.commit()
            print('Your account number have been deleted successful')
            sys.exit
    
    def exit(self):
        print('Exit selected')
        print('Thank you for choosing Reality Bound Bank, Bye Bye ')
        sys.exit

        
        
tank = Bank()
        
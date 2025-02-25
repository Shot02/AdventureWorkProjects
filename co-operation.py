import random
import sys

class cooperative:
    """
    A class representing a simple co-operative system with loan and saving functionality.
    """
    
    def __init__(self):
        self.user_saving = {}
        self.opening()
        
    def opening(self):
            print("""
            Welcome to T&S co-operative
            
            Do you have an account with us?
            1. No
            2. Yes
            3. Exit
            """)
            option = input('your option: ')
            if option == '1':
                self.registration()
            elif option == '2':
                self.login()
            elif option == '3':
                sys.exit
            else:
                print('wrong input')
    
    def registration (self):
        print('Welcome to the registration section. Pls fill the required')
        print()
        first_name = input(f'Enter your first name: ')
        last_name = input(f'Enter your last name: ')
        phone_number = input(f'Enter your phone number: ')
        email = input(f'Enter your email: ')
        membership_no = random.randrange(1111111111, 9999999999)
        membership_id = random.randrange(111, 999)
        created_pw = int(input(f'input your password: '))
        
        print()
        
        self.user_saving = {
        'first_name': first_name,
        'last_name': last_name,
        'Phone_num': phone_number,
        'email': email,
        'membership_no': membership_no,
        'membership_id': membership_id,
        'password': created_pw,
        'saving_balance': 0,
        'loan_balance': 0
        }
        
        print(f"Your pw {created_pw} has been accepted, please remember it.")
        print(f"Your membership number is: {membership_no}")
        print(f"Your membership id is: {membership_id}")
        print(f"Registration successful. Welcome, {first_name} {last_name}")
        print()
        self.opening()
        
    def login (self):
        self.user_saving
        print('login selected. Welcome')
        print()
        email=input(f'Enter your email: ')
        if self.user_saving['email'] == email:
            membership_id=input(f'Input your membership_id: ')
            if membership_id == self.user_saving['membership_id']:
                print(f"Login successful, Welcome back")
                self.home_page()
            else:
                print(f'incorrect id number. Try again')
                self.login()
                print()
        else:
            print(f'incorrect email. Try again')
            self.login()
            print()
            
    def home_page(self):
        print("""
            1. Deposit
            2. Take Loan
            3. Refund Loan
            """)
        operation=input('Select operation: ')
        if operation == '1':
            self.deposit()
        elif operation == '2':
            self.take_loan()
        elif operation == '3':
            self.refund_loan()
        else:
            print('Invalid option. Try again')
        
    def deposit(self):
        print('deposit selected')
        amount = float(input("Enter amount: $ "))
        save_balance = amount + self.user_saving['saving_balance']
        loan_balance = amount * 2 + self.user_saving['loan_balance']
        self.user_saving['saving_balance'] = save_balance
        self.user_saving['loan_balance'] = loan_balance
            
cooperative() 

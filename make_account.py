#Write a function:
#make_account(initial_balance)
#that creates and returns two functions representing operations on a bank account:
#- a function for depositing money,
#- a function for withdrawing money.
#The account balance must be initialized using initial_balance and must persist betwen function calls.
#The following rules apply;
#- Deposits and withdrawals must use positive numeric values.
#- The account balance must never become negative.
#- Invalid operations must raise appropriate Python exceptions.
#- The account balance must not be directly accessible from outside the returned functions.

def make_account(initial_balance):
    try:
        balance = initial_balance + 0
    except TypeError:
        raise TypeError("Initial balnce must be numeric")
        
    if balance < 0:
        raise ValueError("Initial balance cannot be negative")
        
    def deposit(amount):
        nonlocal balance
        try:
            amount = amount + 0
        except TypeError:
            raise TypeError("Deposit amount must be numeric")
            
        if amount <=0:
            raise ValueError("Deposit amount must be positive")
            
            
        balance += amount
        return balance
    
    def withdraw(amount):
        nonlocal balance
        try:
            amount = amount + 0
        except TypeError:
            raise TypeError("Withdrawal amount must be numeric ")
            
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
            
        if amount > balance:
            raise ValueError("Insufficient funds")
            
        balance -= amount
        return balance
            
            
        
    return deposit, withdraw
    
    
deposit, withdraw = make_account(450)
print(make_account)
deposit(300)

withdraw(234)


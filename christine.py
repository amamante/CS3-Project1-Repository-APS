# ============================================================
#  BankAccount Encapsulation — complete the class below.
#  The class name, the @property getter lines, and the set_
#  method signatures are already set for you; just fill in the
#  bodies marked with TODO.
# ============================================================


class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance


    # ----- read-only getters via @property (NO @property.setter!) -----
    @property
    def account_number(self):
        return self.__account_number


    @property
    def balance(self):
        return self.__balance


    # ----- traditional setter METHODS (called WITH parentheses) -----
    def set_account_number(self, account_number):
        self.__account_number = account_number


    def set_balance(self, balance):
        if balance < 0:
            print("Warning: balance cannot be negative — ignored.")
        else:
            self.__balance = balance


# ------------------------------------------------------------
#  Step 6 — Test your class.
#  Uncomment and complete the lines below once your class works.
# ------------------------------------------------------------
acct = BankAccount("ACC1", 500)

print(acct.account_number)   # Expected: ACC1   (read — no parentheses)
print(acct.balance)          # Expected: 500    (read — no parentheses)


acct.set_balance(800)        #                 (change via the METHOD)
print(acct.balance)          # Expected: 800


acct.set_balance(-50)        # Expected: a warning is printed
print(acct.balance)          # Expected: 800    (negative was IGNORED!)
print("hi")

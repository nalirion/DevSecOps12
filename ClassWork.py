class bank_account:
    def __init__(self, balance=0, owner='',id=0,credit_score=0):
        self.__balance = balance
        self.owner = owner
        self.id = id
        self.__credit_score = credit_score

    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return f'bank account {self.owner} id : {self.id}'
    def __eq__(self, other):
        return self.__balance == other.__balance
    
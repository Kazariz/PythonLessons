class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Баланс не может быть отрицательным")


acc = Account(100)
print(acc.balance)
acc.balance = 200
print(acc.balance)

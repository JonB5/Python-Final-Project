################################
## Solution prepared by Dr. Fitz at Florida Tech.
## Do not copy, store, or reproduce without permission from the author.

## Florida Tech Students in CSE 2050 for Spring 2023
## may use this code as part of their Final Project.
## Do not post this code online in any repository, archival system, 
## or device, and do not distribute, transform, or share with friends or any other entity.
################################

class Category:
    def __init__(self, category, name):
        self._category = category
        self.name = name
        self._wallet = []

    def add_revenue(self, amount, description=''):
        if (type(amount) != int or type(amount) != float) and amount < 0:
            raise Exception(f"Error: amount to deposit in {self._category} "
                            f"category balance has to be a positive number")
        self.wallet.append({'amount': amount, 'description': description})

    def add_expense(self, amount, description=''):
        if not self.is_number(amount):
            raise Exception(f"Error: amount to withdraw from {self.category} "
                            f"category balance has to be a negative number")
        if not self.check_category_balance(amount):
            return False
        if amount > 0:
            amount *= -1
        self.wallet.append({'amount': amount, 'description': description})
        return True

    def get_balance(self):
        balance = 0
        for action in self._wallet:
            balance += action['amount']
        return balance

    def transfer_money(self, amount, target):
        if not self.is_number(amount):
            raise Exception(f"Error: amount to send money from {self.category} "
                            f"category balance has to be a number")

        if not isinstance(target, Category):
            raise Exception("Error: Category does not exist")
        sufficient_money = self.add_expense(amount, f"Send money to {target.category}")

        if not sufficient_money:
            return False
        target.add_revenue(amount, f"Send money from {self.category}")
        return True

    def check_category_balance(self, amount):
        if abs(amount) > self.get_balance():
            # Not enough funds for expense
            return False
        return True

    def is_number(self, value):
        return (type(value) == int or type(value) == float)

    # Category String output
    def __str__(self):
        # Arrange category's name with *. Max 30 char.
        header = self.category.center(30, '*')
        body = ''

        # Loop through wallet and get every action, 
        # Then arrange description (max 23)+ amount fixed to max 2 decimals(max 7) in a string.
        for action in self.wallet:
            description = action['description'][0:23]
            description = description.ljust(23)
            amount = round(action['amount'], 2)

            if type(amount) == int:
                amount = str(amount) + '.00'
            amount = str(amount).rjust(7)
            body += description + amount + '\n'

        # Line displays category's total.
        footer = 'Total: ' + str(self.get_balance())
        return f"{header}\n{body}{footer}"

    ################################
    # Advanced construct of decorators
    # Learn more about decorators here: https://www.freecodecamp.org/news/python-property-decorator/
    ################################
    @property
    def wallet(self):
        return self._wallet

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if type(value) != str:
            raise Exception("Error: category's name is not a String")
        self._category = value
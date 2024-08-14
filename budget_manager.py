# Personal Budget Management Application
# Manage categories (food, entertainment, utilities, etc.)
# Private budget details

# Class: private attributes for category name & allocated budget

# Getters & Setters:
# Category name
# Budget allocated

# Add Budget: method
# Add expenses to category & adjust budget
# Validate expense amount before deductions

# Display Budget Details: method
# Details of a budget category:
    # name
    # allocated budget
    # remaining budget after expenses

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.expenses = []

    def get_cat_name(self):
        return self.__category_name
    
    def get_allo_bud(self):
        return self.__allocated_budget
    
    def set_cat_name(self, new_cat_name):
        self.__category_name = new_cat_name

    def set_allo_bud(self, new_allo_bud):
        self.__allocated_budget = new_allo_bud

    def add_expense(self, amount):
        if 0 < amount <= (self.get_allo_bud()-sum(self.expenses)):
            self.expenses.append(amount)
            print(f"\nExpense Amount: ${amount} \nAdded to Budget Category: {self.get_cat_name()}")
        else:
            print("\nInsufficient budget allocated for this expense")

    def deduct_expenses(self):
        return self.get_allo_bud() - sum(self.expenses)

    def display_cat_summary(self):
        print(f"\nCategory: {self.get_cat_name()}\nAllocated Budget: ${self.get_allo_bud()}\nRemaining Budget after Expenses: ${self.deduct_expenses()}")


food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.add_expense(100)
food_category.add_expense(4000)
food_category.display_cat_summary()

entertainment_category = BudgetCategory("Entertainment", 100)
entertainment_category.add_expense(100)
entertainment_category.display_cat_summary()

utilities_category = BudgetCategory("Utilities", 200)
utilities_category.add_expense(100)
utilities_category.display_cat_summary()

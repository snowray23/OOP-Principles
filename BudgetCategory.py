# bare with me as i am a bit lost on oop 


#Task 1: Define Budget Category Class
class Budget:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget


#Task 2: Implement Getters and Setters
    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, new_name):
        self.__category_name = new_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_budget):
        if new_budget >= 0:
            self.__allocated_budget = new_budget
        else:
            print("Error: Budget must be a positive number.")


#Task 3: Add Budget Functionality
    def add_expense(self, new_expense):
        if new_expense <= 0:
             print("Sorry, your expense needs to be a positive amount.")
        elif new_expense > self.__allocated_budget:
             print("Sorry, we can't afford it.")
        else:
             print("Expense was added.")


#Task 4: Display Budget Details
    def display_budget_details(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: {self.__allocated_budget}")
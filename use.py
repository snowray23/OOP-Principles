from BudgetCategory import Budget

def use():
    fun_category = Budget("fun", 500)
    fun_category.add_expense(50)
    fun_category.display_budget_details()

if __name__ == "__main__":
    use()
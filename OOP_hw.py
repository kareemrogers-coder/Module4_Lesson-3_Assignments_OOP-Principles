# 1. Encapsulation in Personal Budget Management

# Objective: The aim of this assignment is to reinforce the understanding of encapsulation in Python, focusing on the use of private attributes and getters and setters. Students will apply these concepts to create a Personal Budget Management system.

# Problem Statement: You are required to build a Personal Budget Management application. The application will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details remain private and are accessed or modified through public methods.

# Task 1: Define Budget Category Class

# Create a class BudgetCategory with private attributes for category name and allocated budget.
# Initialize these attributes in the constructor.
# Expected Outcome: A BudgetCategory class capable of storing category details securely.

from helper import d

budget = 0

class BudgetCategory():
       
        def __init__(self, category_name, allocated_budget):
                self.__category_name = category_name
                self.__allocate_budget = allocated_budget

# Task 2: Implement Getters and Setters

# Write getter and setter methods for both the category name and the allocated budget.
# Ensure that the setter methods include validation (e.g., budget should be a positive number).
# Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.



        # implement the getter:

        def get_category_name(self):
                return self.__category_name
        
        def get__allocate_budget(self):
                return self.__allocate_budget
        
        #implement the setters:

        def set__category_name(self,new_category):
                self.set__category_name = new_category
                print(f"New catrgory is: {new_category} ")
        
        def set__allocate_budget(self, new_budget):
                flag = False
                for budget in new_budget:
                       if budget.isdigit() and budget >= 0:
                              flag = True
                              continue
                       else:
                        flag = False
                        print("invalid entry, please valid amount")
                        break
                if flag:
                      self.__allocate_budget = new_budget
                      print(f"New budget amount is: {new_budget}")


# Task 3: Add Budget Functionality

# Implement a method to add expenses to a category and adjust the budget accordingly.
# Validate the expense amount before making deductions from the budget.
# Expected Outcome: Ability to track expenses per category and update the remaining budget safely.        


        def add_expense(self, budget_exp):
                if isinstance(budget_exp, (int, float)) and budget_exp >= 0:
                    self.__allocate_budget += budget_exp
                    print(self.__allocate_budget)
                else:
                    print("Expense amount must be a positive number")


####testing parameters
        # testing = BudgetCategory("water", budget)

                # testing.add_expense(100)

                        # testing.add_expense(200)

                                # print(testing.get_category_name())

# Task 3: Add Budget Functionality

# Implement a method to add expenses to a category and adjust the budget accordingly.
# Validate the expense amount before making deductions from the budget.
# Expected Outcome: Ability to track expenses per category and update the remaining budget safely.
# Task 4: Display Budget Details
# Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.
# Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.

electric_bill = BudgetCategory("electric", allocated_budget = 1000)
print (f"New total expense are: ")
{electric_bill.add_expense(1000)} 

d()

print(f"July billing cycle reveals that our {electric_bill.get_category_name()} bill is at a staggering ${electric_bill.get__allocate_budget()} and is due in 10 days")



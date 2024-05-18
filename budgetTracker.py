import calendar
import datetime

class Budget:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

class BudgetTracker:
    def __init__(self):
        self.budget = {}

    def add_budget(self, category, amount, date):
        if category in self.budget:
            self.budget[category].append((amount, date))
        else:
            self.budget[category] = [(amount, date)]

    def get_total_spending(self):
        total = 0
        for category in self.budget:
            for amount, _ in self.budget[category]:
                total += amount
        return total

    def get_category_spending(self, category):
        if category in self.budget:
            return sum(amount for amount, _ in self.budget[category])
        else:
            return 0

    def view_spending_patterns(self):
        print("Spending Patterns:")
        for category in self.budget:
            total_spending = sum(amount for amount, _ in self.budget[category])
            print("--------Your Spending Amount---------")
            print(f"{category}: {total_spending}/-")
            print("-------------------------------------")
        print()

    def view_budget_by_date(self, date):
        print(f"Budget on {date}:")
        budget_found = False
        for category in self.budget:
            budget_on_date = [amount for amount, budget_date in self.budget[category] if budget_date == date]
            if budget_on_date:
                total_spending = sum(budget_on_date)
                print(f"{category}: {total_spending}/-")
                budget_found = True
        if not budget_found:
            print("None")
        print()

def main():
    tracker = BudgetTracker()
    print(f"🎯 Running Budget Tracker!")
    expense_file_path = "budget.csv"
    budget = 2000

    while True:
        print("1. Add Budget")
        print("2. View Spending Patterns")
        print("3. View Total Spending")
        print("4. View Budgets by Date")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"🎯 Getting User Budget")
            budget_name = input("Enter budget name: ")
            budget_amount = float(input("Enter budget amount: "))
           budget_categories = [
                "🍔 Food",
                "🏠 Home",
                "💼 Work",
                "🎉 Fun",
                "✨ Misc",
            ]
            while True:
                print("Select a category: ")
                for i, category_name in enumerate(budget_categories):
                    print(f"  {i + 1}. {category_name}")

                value_range = f"[1 - {len(expense_categories)}]"
                selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

                if selected_index in range(len(budget_categories)):
                    selected_category = budget_categories[selected_index]
                    new_budget = Budget(
                        name=budget_name, category=selected_category, amount=budget_amount
                    )
                    tracker.add_budget(selected_category, expense_amount, datetime.date.today())
                    break
                else:
                    print("Invalid category. Please try again!")

        elif choice == "2":
            tracker.view_spending_patterns()

        elif choice == "3":
            total_spending = tracker.get_total_spending()
            print("---------Your Total Spending Amount----------")
            print(f"Total Spending: {total_spending}/-")
            print("----------------------------------------")

        elif choice == "4":
            date_input = input("Enter date to view expenses (YYYY-MM-DD): ")
            budget_date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
            print("---------View Expenses by Date----------")
            tracker.view_expenses_by_date(expense_date)
            print("----------------------------------------")

        elif choice == "5":
            print("Exiting...thank you, see you soon :)")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

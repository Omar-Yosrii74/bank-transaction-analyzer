import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bank_models import BankAnalyzer  


class App(BankAnalyzer):

    def show_chart(self):
        category_data = self.get_expenditure_by_category()

        if not category_data:
            print("No data available to plot.")
            return

        summary = pd.Series(category_data)

        plt.figure(figsize=(10, 7))
        summary.plot(kind='pie', autopct='%1.1f%%', startangle=140, shadow=False)
        plt.title('Financial Analysis: Spending by Category')
        plt.ylabel('')
        print("\n[Graphics] Displaying Pie Chart... (Close the window to continue)")
        plt.show()


if __name__ == "__main__":
    my_app = App('bank_data.csv')

    if my_app.load_data():
        while True:
            print("\n" + "="*45)
            print("    WELCOME TO BANK TRANSACTION ANALYZER    ")
            print("="*45)
            print("\nSelect an option to proceed:\n")
            print("1. View overall spending")
            print("2. Top 5 Transactions")
            print("3. View monthly spending")
            print("4. Spending by category")
            print("5. Export Summary Report to CSV")
            print("6. Exit")
            print("="*45)

            try:
                choice = int(input("\nEnter your choice (1-6): "))
            except ValueError:
                print("\nInvalid input! Please enter a number between 1 and 6.")
                continue

            if choice == 1:
                print("\n--- Overall Spending  ---\n")
                total = my_app.get_total_expenditure()
                avg = np.mean(my_app.data['Amount'])
                print(f"Total Spending: {total:,.2f} EGP")
                print(f"Average Transaction: {avg:,.2f} EGP")

            elif choice == 2:
                print("\n--- Top 5 Transactions ---\n")
                top_items = my_app.get_top_expenses(5)
                for i, tx in enumerate(top_items, 1):
                    print(f"{i}. Category: {tx.category:<12} | Amount: {tx.amount:,.2f}")

            elif choice == 3:
                print("\n--- Monthly Spending Overview ---\n")
                monthly = my_app.get_monthly_expenditure()
                monthly_sorted = sorted(monthly.items(), key=lambda x: pd.to_datetime(str(x[0])))
                for month_period, amt in monthly_sorted:
                    month_ts = month_period.to_timestamp()
                    print(f"Month: {month_ts.strftime('%B %Y')} | Total Spent: {amt:,.2f} EGP")

            elif choice == 4:
                print("\n--- Spending by Category ---\n")
                cat_summary = my_app.get_expenditure_by_category()
                cat_summary_sorted = dict(sorted(cat_summary.items(), key=lambda x : x[1], reverse=True))
                for cat, amt in cat_summary_sorted.items():
                    print(f"• {cat:<12}: {amt:,.2f}")
                highest_category = max(cat_summary, key=cat_summary.get)
                lowest_category = min(cat_summary, key=cat_summary.get)
                print(f"\nHighest spending category: {highest_category} ({cat_summary[highest_category]:,.2f})")
                print(f"Lowest spending category: {lowest_category} ({cat_summary[lowest_category]:,.2f})")
                my_app.show_chart()

            elif choice == 5:
                print("\n--- Exporting Summary Report ---\n")
                summary_data = pd.Series(my_app.get_expenditure_by_category())
                summary_data.to_csv(
                    'spending_summary_report.csv',
                    header=['Amount'],
                    index_label='Category')
                print("\n✅ Success: Report saved as 'spending_summary_report.csv'")

            elif choice == 6:
                print("\nThank you for using  THE TRANSACTION ANALYZER. Goodbye!\n")
                break

            else:
                print("\nInvalid choice. Please select 1-6.")
    else:
        print("\nNo transaction data found.")
        print("Please check that the data file exists, then restart the app.")

       
       

        
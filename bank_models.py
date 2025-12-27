import pandas as pd

class Transaction:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount


class BankAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_csv(self.file_path)
            self.data.dropna(inplace=True)
            return True
        except FileNotFoundError:
         print("Data file not found.")
         return False


    def get_total_expenditure(self):
        if self.data is not None:
            return self.data['Amount'].sum()
        return 0

    def get_expenditure_by_category(self):
        if self.data is not None:
            return self.data.groupby('Category')['Amount'].sum().to_dict()
        return {}

  
    def get_monthly_expenditure(self):
        if self.data is not None:
         self.data['Date'] = pd.to_datetime(self.data['Date'])
         monthly = self.data.groupby(self.data['Date'].dt.to_period('M'))['Amount'].sum()
         monthly = monthly.sort_index()
         return monthly.to_dict()
        return {}


    def get_top_expenses(self, n=5):
        if self.data is not None:  
            top_expenses_df = self.data.nlargest(n, 'Amount')
            return [Transaction(row['Category'], row['Amount']) for index, row in top_expenses_df.iterrows()]
        return []
    
    
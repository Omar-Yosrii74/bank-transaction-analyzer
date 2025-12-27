# Sample code to generate bank data and save it to a CSV file

import pandas as pd
import random

categories = ['Food', 'Transport', 'Shopping', 'Bills', 'Entertainment']
data = []

for i in range(100):
    year = random.randint(2019, 2023)         
    month = random.randint(1, 12)              
    day = random.randint(1, 28)                
    row = {
        'Date': f'{year}-{month:02d}-{day:02d}',  
        'Category': random.choice(categories),
        'Amount': random.randint(100, 2000)
    }
    data.append(row)

pd.DataFrame(data).to_csv('bank_data.csv', index=False)

print("\nSample bank data generated and saved to 'bank_data.csv'.\n")


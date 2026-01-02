# 🏦 Bank Transaction Analyzer (Python OOP & Data Science)

## 📌 Project Overview
A professional Python-based financial tool designed to analyze bank transactions. This project demonstrates the integration of **Object-Oriented Programming (OOP)** with data science libraries like **Pandas, NumPy, and Matplotlib** to process and visualize financial data.

---

## 🚀 Key Features
* **Automated Data Cleaning:** Uses Pandas to handle missing values and prepare the dataset.
* **Statistical Analysis:** Leverages NumPy for high-speed calculation of totals and averages.
* **OOP Implementation:** Maps raw data rows into specialized `Transaction` objects.
* **Time-Series Tracking:** Groups expenditures by month to monitor spending trends.
* **Data Visualization:** Plots expenses using **Matplotlib** (Pie Charts).
* **Report Generation:** Exports final analysis summaries back into CSV format.
* **Budget Tracking:** Set budgets per category and receive warnings when expenses exceed limits.

---

## 🛠️ Built With
* **Python 3.x**
* **Pandas:** Data manipulation and CSV processing.
* **NumPy:** Mathematical and statistical operations.
* **Matplotlib:** Data visualization and plotting.

---

## 🏗️ System Architecture
The project follows a modular structure for better maintainability:
1.  **`models.py`**: The **Logic Layer**. Contains class definitions (`BankAnalyzer`, `Transaction`).
2.  **`main.py`**: The **Presentation Layer**. Handles the interactive CLI Menu and Graphics.
3.  **`data_gen.py`**: A utility script to generate synthetic bank data.



---

## 💻 How to Run
1.  **Generate Data:** Run the generator script first:
    ```bash
    python data_gen.py
    ```
2.  **Start Analyzer:** Run the main application:
    ```bash
    python main.py
    ```
3.  **Navigate Menu:** Use options **1-8** to explore statistics, OOP objects, monthly trends, charts, and budget management.

---

## 🧪 Applied Concepts
* **Inheritance:** `App` class inherits from `BankAnalyzer`.
* **Encapsulation:** Logic is hidden within class methods.
* **File I/O:** Reading and writing CSV files.
* **Error Handling:** Robust `try-except` blocks for file operations.

---

## 📈 Sample Plot
When selecting **Option 4**, the system generates a **Spending Distribution Pie Chart**, showing the percentage of expenses across different categories.



---

**Developed for Academic Evaluation - 2025**
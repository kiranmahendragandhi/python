# bonus_calc.py

# 1. Define the data
employees = {
    "Alice": 5000,
    "Bob": 6200,
    "Charlie": 4500
}
bonus_rate = 0.10  # 10% bonus

print("=== STARTING BONUS CALCULATION ===")

# 2. Process the data and print results
for name, salary in employees.items():
    bonus = salary * bonus_rate
    print(f"Employee: {name} | Salary: ${salary} | Bonus: ${bonus:.2f}")

print("=== PROCESS COMPLETED SUCCESSFULLY ===")

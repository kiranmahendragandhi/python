# bonus_calc.py
import os

# 1. Read the environment choice from Jenkins
# If Jenkins doesn't send anything, it defaults to 'Local-Test'
env_choice = os.environ.get('ENVIRONMENT', 'Local-Test')

print(f"=== DEPLOYMENT ENVIRONMENT: {env_choice.upper()} ===")
print("=== STARTING BONUS CALCULATION ===")

employees = {
    "Alice": 5000,
    "Bob": 6200,
    "Charlie": 4500
}
bonus_rate = 0.10 

for name, salary in employees.items():
    bonus = salary * bonus_rate
    print(f"Employee: {name} | Salary: ${salary} | Bonus: ${bonus:.2f}")

print("=== PROCESS COMPLETED SUCCESSFULLY ===")

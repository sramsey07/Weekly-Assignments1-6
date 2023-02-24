hourlyWages = float(input("Enter hourly wage: "))

regularHours = float(input("Enter total regular hours worked: "))

overtimeHours = float(input("Enter total overtime hours worked: "))

weeklyPay = (hourlyWages * regularHours) + (hourlyWages * overtimeHours * 1.5)

print("Emplyee's total weekly pay: ", weeklyPay)

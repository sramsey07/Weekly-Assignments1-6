salary=float(input("Enter the salary: "))
percentage=int(input("Enter the percentage the teacher receives: "))
years=int(input("Enter the number of years: "))

i = 0
temp = 0

print("Year      Salary")

while(i<years):
    print(i+1,"      ",round(salary,2))
    salary = salary*(100+percentage)/100
    i=i+1

n=int(input("Enter number of iterations: "))

total=0
dinominator=1
x=1

while(x<=n):
    if(x%2==1):
        total=total+(1/dinominator)
    else:
        total=total-(1/dinominator)
    x=x+1
    dinominator=dinominator+2

print("The approximation of pi is: ",total*4)

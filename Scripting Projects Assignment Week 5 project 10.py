purchasePrice = float(input("Enter the purchase price: "))

month = 1
interestRate = 0.12
downPayment = purchasePrice * 0.10

payment = (purchasePrice - downPayment) * 0.05
currentBalance = purchasePrice - downPayment


print("{:14s}{:19s}{:19s}{:19s}{:19s}{:19s}".format("Month", "Current Balance", "Interest", "Principal", "Monthly Payment", "Balance"))

while currentBalance > 0:
    if currentBalance < payment:
        interestAmount = 0
        principal = currentBalance
        pay = currentBalance
        finalBalance = 0
    else:
        interestAmount = currentBalance * (interestRate/12)
        principal = payment - interestAmount
        pay = interestAmount + principal
        finalBalance = currentBalance - principal

    print("{:<14d}{:<19.2f}{:<19.2f}{:<19.2f}{:<19.2f}{:<19.2f}".format(month,currentBalance,interestAmount,principal,pay,finalBalance))

    currentBalance = finalBalance

    month = month + 1

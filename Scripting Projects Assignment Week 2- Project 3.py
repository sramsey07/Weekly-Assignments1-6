newVideos = 3.00
oldies = 2.00
new = int(input("Enter the number of new videos: "))
old = int(input("Enter the number of old videos: "))
nights = int(input("Enter the number of nights: "))
totalCost = (newVideos * new + oldies * old) * nights
print("The total cost per night is $" + str(round(totalCost)))

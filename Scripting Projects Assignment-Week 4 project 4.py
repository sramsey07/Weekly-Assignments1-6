height = float(input("Enter the height the ball is dropped from: "))

index = float(input("Enter the bounce index of the ball: "))

bounces = int(input("Enter the number of times the ball bounces: "))

distance = height

for i in range(bounces-1):
    height *= index
    distance += 2*height

distance +=height * index

print("The distance traveled is: " + str(distance) + " units.")

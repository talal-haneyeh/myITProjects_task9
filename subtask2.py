number = input("enter ")
number = int(number)

count = 0
sum = 0

min = number

while(number != -1):
    count = count + 1
    if (number <= min):
        min = number
    sum = sum + number
    number = input("enter ")
    number = int(number)

if (count == 0):
    print ("min = -1 and avg = -1")
    
else:
    print ("count = " + str(count) + "\n min = " + str(min) + "\n sum = " + str(sum) + "\n Avg = " + str(sum/count))
 
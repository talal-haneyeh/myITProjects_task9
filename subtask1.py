num = input("Please enter a number ")
num = int(num)

b = 0
a = 0
 
while(not((num >= b * b) and (num < a * a))):
     b = a
     a = a + 1

q = b*b
print(q)

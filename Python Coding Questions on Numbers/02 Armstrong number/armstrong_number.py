#What is Armstrong Number?
#It is a number which is equal to the sum of cube of its digits.
#For eg: 153, 370 etc.
#Lets see it practically by calculating it,
#Suppose I am taking 153 for an example
#First calculate the cube of its each digits
#  1^3 = (1*1*1) = 1
#  5^3 = (5*5*5) = 125
#  3^3= (3*3*3) = 27
#Now add the cube
#  1+125+27 = 153
#It means 153 is an Armstrong number.

num = int(input("Enter number: "))
sum = 0
number = num

while num != 0:
    sum += pow((num % 10), 3)
    num //= 10

if sum == number:
    print(number," is an armstrong number")
else:
    print(number," is not an armstrong number")

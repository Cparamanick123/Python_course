'''ASSIGNMENT 2:
Module 3: Control Structures in Python
'''
#Task 1: Check if a Number is Even or Odd

number=int(input("Enter a number : "))
if number% 2==1:
    print(f"{number} is an odd number")
else:
    print(f"{number} is an even number")
    
#Task 2: Sum of Integers from 1 to 50 Using a Loop
sum=0
for i in range(1,51):
    sum+=i
print("The sum of numbers from 1 to 50 is : ",sum)#output 1275
   
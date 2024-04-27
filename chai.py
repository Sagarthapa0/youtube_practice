#Q. counting positive numbers

# numbers=[1,2,-3,4,5,6,-7,8,9,10]
# positive_number_count=0
# for i in numbers:
#     if i>0:
#         positive_number_count+=1
#         print(f"positive number is {i}")
#     if i<0:
#         pass
# print(positive_number_count)

#Q. calculate the sum of evennumber up to given number n.

# n=int(input("Enter the number "))
# sum=0
# for i in range(0,n+1):
#     if i%2==0:
#         sum=sum+i
#     else:
#         pass
# print(f"Sum of even number is {sum}")

#Q. Reverse a string with a loop

# name="Sagar"
# reversed_name=""
# for char in name:
#     reversed_name=char+reversed_name
# print(reversed_name)

#Q. given the string find the first non-repeated character

# input_string="teetertea"
# for char in input_string:
#     if input_string.count(char)==1:
#         print("char is ",char)
#         break

#Q. factorial of a number using while loop

# fact=1
# i=1
# n=int(input("enter a number "))
# while i<=n:
#     fact=fact*i
#     i=i+1
# print(fact)

#Q. check if the number is prime

n=int(input("Enter a number "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("the number is not prime ", n)
            break
else:
    print("invalid number")
# calculation={
#    "1":"add",
#    "2":"diff"
# }
# num1=float(input("num1 : "))
# num2=float(input("num2 : "))
# which=None
# while which in [1,2]:
#     which=input("you want to do ")
# if input is add:
#    print("value of",num1 ,"+", num2,"is",num1+num2)
# elif input is diff:
#    print("value of",num1 ,"-", num2,"is",num1-num2)
# print("value of",num1 ,"/", num2,"is",num1/num2)
# print("value of",num1 ,"*", num2,"is",num1*num2)

# num1=float(input("Enter the first number here :"))
# num2=float(input("Enter the second number here :"))
# print("""
#       Enter 1 for 'Addition'
#       Enter 2 for 'substration'
#       Enter 3 for 'multiply'
#       Enter 4 for 'Division'
# """)
# choice=float(input("choice a number from 1-4 : "))
# if choice==1:
#     print("sum is ",num1+num2)
# elif choice==2:
#     print("diff is ",num1-num2)

# a=input("enter your name ")
# print("my name is",a)

# x=int(input("enter first number :"))
# y=int(input("enter second number :"))
# print("sum is ",x+y)


# def factorial(n):
#         if n==0 or n==1:
#             return 1
#         else:
#             return n*factorial(n-1)
# print(factorial(6))        
# print(factorial(5))        
# print(factorial(4))        

# f=open("demofile.txt","r")
# for x in f:
#     print(x)
# f.close()

f=open("demofile.txt","w")
f.write("now add this")

f=open("demofile.txt","r")
print(f.read())
f.close()
# n=int(input("enter number "))
# sum=1
# for i in range(1,n+1):
#     sum=sum*i
#     print(sum)

#print the length of list ------1

# food=["momo","chaumin","coke"]
# fruits=["apple","banana","guava"]
# def len_list(list):
#     print(len(list))
# len_list(food)

#print the elements of a list in a single line-------2

# food=["momo","chaumin","coke"]
# def elements(list):
#     print(list,end=" ")
# elements(food)


#find the factorial ------------3

# n=int(input("enter number"))
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
# factorial(n)

#convert usd to inr----------4

# usd=int(input("how much usd "))
# def convert(usd):
#     inr=usd*83
#     print("total of ",usd, "usd in inr is ",inr)
# convert(usd)


#####--RECURSION

# def show(n):
#     if (n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)    

#factorial

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return fact(n-1)*n
# n=int(input("enter number "))
# print(fact(n))


# Q.calculate sum of first n natural number

# def sum(n):
#     if n==0:
#         return 0
#     return sum(n-1)+n  
# sum=sum(5)
# print(sum)
    

# Q.print all elements in list

# def print_list(list,idx):
#     if idx==len(list):
#         return
#     print(list[idx])
#     print_list(list,idx+1)
# fruits=["mango","litchhi","banana"]
# print_list(fruits,0)




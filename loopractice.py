# Q.print first ten natural number

# i=1
# for i in range(1,11):
#     print(i)
#     i+=1


#  Q.calculate the sum of all numbers from 1 to given numbers

# i=1
# sum=0
# n=int(input("enter a number "))
# for i in range(1,n+1):
#     sum=sum+i
#     i+=1
# print(sum)


# Q. MUltiplication table

# n=int(input("Give a number for multiplication "))
# for i in range(1,11):
#     mul=i*n

#     print(f"{i} * {n} = {mul}")


# Q.sum of series up to n terms

n=5
start=2
sum_seq=0
for i in range(0,n):
    print(start,end="+")
    sum_seq+=start
    start=start*10+2
print("sum of above series is:", sum_seq)
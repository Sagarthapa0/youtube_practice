# a,b=2,3
# txt="@"
# print(a*txt*b)

# a="2"
# print((a+txt)*3)

# num1=int(input("num1 : "))
# num2=int(input("num2 : "))
# print("sum = ",num1+num2)

# side=float(input("Side is : "))
# print("area is ",side*side)

# list=[4,6,2,8]
# list.sort()
# print(list.append(10))
# print(list)

# first=input("Your first favroite movie is ")
# second=input("Your second favroite movie is ")
# third=input("Your third favroite movie is ")
# list=[first,second,third]
# print("User favriotemovies are",list)

# dict={
#     "name":"sagar",
#     "subject":"python"
# }
# print(dict)
# print(dict["name"])

# set={1,2,4,"sagar"}
# set.pop()
# print(set)

#dictionary

# marks={}
# x=int(input("enter physics marks "))
# marks.update({"phy":x})
# y=int(input("enter chemistry marks "))
# marks.update({"che":y})
# z=int(input("enter maths marks "))
# marks.update({"maths":z})
# print(marks)
# percentage=float(((x+y+z)/300)*100)
# print("percentage is ",percentage, "%")


#loops

# i=100
# while i>=1:
#     print(i)
#     i-=1

# n=int(input("give a number you want to multiply : "))
# print("multiple of 5 is")
# i=1
# while i<=10:
#     print("\t",n*i)
#     i+=1


# list=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx < len(list):
#     print(list[idx])
#     idx+=1

# nums=(1,4,9,16,25,36,49,64,81,100)

# x=36
# i=0
# while i<=len(nums)-1:
#     if (nums[i]==x):
#         print("found",i)
#     i+=1

# i=1
# while i<=10:
#     if i==4:
#         i+=1
#         continue
#     print(i)
#     i+=1

# nums=(1,4,9,16,25,36,49,64,81,100)
# x=49
# for el in nums:
#     if x==el:
#         print("Found",el)
#         break
#     else:
#         print("not found",el)
    
# n=int(input("enter number "))
# for i in range(1,11):
#     print(n*i)

# n=5      
# sum=0 
# for i in range(1,n+1):
#     sum += i
# print(sum)


# n=5
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

#file updating-----

# f=open("practice.txt","w")
# data=f.write("My name is sagar java \n i am from chitwan java")

# f=open("practice.txt","r")
# data=f.read()
# newdata=data.replace("java","python")
# print(newdata)
# f=open("practice.txt","w")
# f.write(newdata)
# f.close()
# if "hero" in newdata:
#     print("yes")
# else:
#     print("no")



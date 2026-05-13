# 8 may 2026


# def fun(x=0,y=0):
#     print(x+y)

# fun(10,20)

# def display(*arg):
#     print(arg)
#     print(type(arg))
    
# display(10,20,30)
# display(10,'python','java',20,30)

# * targets every arguement and shows them in a tuple
# it packs data in tuple -> packing
# works on list and tuple


# def sum(*n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     print(sum)

# sum(10,20,30,40)

# def display(*n):
#     print(n)
#     print(type(n))

# values=eval(input("Enter all values"))
# display(*values) #unpacking


# def add(x=0,y=0,z=0):# =0  means setting default value 
#     print("x= ",x)
#     print("y= ",y)
#     print("z= ",z)

# # add(z=10,x=20,y=29)

# # error
# add(x=10)
# add(z=10,x=30)
# add(x=10,y=20,z=100)

# * star ->tuple
# ** star ->dict


# def add(**kwargs):
#     print(kwargs)

# add()
# add(x=10,y=20,z=30,p=5,q=6)


# d={"x":10,"y":20,"z":30}
# sum=0
# for i in d:
#     # ways to sum values of dict 
#     sum=sum+d.get(i)
#     # sum=sum+d[i]

# print(sum)

# d=eval(input("enter value"))
# sum=0
# def summ():
#     for i in d:
#         sum=sum+d.get(i)
#         # sum=sum+d[i]

#     print(sum)

# summ()

# def hello(greet):
#     print("hello",greet)

# hello("ali")




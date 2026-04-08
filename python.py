# 16 jan
# a=10
# print(a,end=" ")
# print(a)
# print("Hello world")

# 17 jan
# a=int(input("Enter a number "))
# b=int(input("Enter a number "))
# print(a+b)

# operators
# 1 arithmatic ----> + - / * % //(floor division) **(exponential)
# 2 assignment ----> = += -= /= %= //= **= 
# 3 comparison ----> < >= <= !=
# 4 logical -----> and or not
# 5 bitwise ----->
# 6 membershp ----> in  not in
# 7 identity ----> is is not

# arithmatic
# a=10
# b=2
# print(a+b)
# print(a-b)
# print(a/b)
# print(a*b)
# print(a//b)
# print(a**b)


# # area of square
# side = int(input("Enter side"))
# print(side**2)

# # area of circle
# radius = int(input("Enter radius"))
# print(3.14*radius**2)

# # area of rectangle
# length = int(input("Enter length"))
# breadth = int(input("Enter breadth"))
# print(length*breadth)

# # area of triangle
# base=int(input("Enter base"))
# height=int(input("Enter height"))
# print(1/2*b*h)


# 19 january
# ternary operator
# print(a) if a>b else print(b)

# 20 january
# print("a" in "ali")
# a = 20
# b = 10
# print(a+b)
# print(a>b)
# print(a<b)
# print(a==b)
# print(a and b)

# 27 jan
# input takes default value in string
# you have to write "int" ti make it int type from string type or else it will just print the 2 digits without adding
# num1= int(input("Enter a number "))
# num2= int(input("Enter a number "))
# print(num1+num2)

# num1= input("Enter a number ")
# num2= input("Enter a number ")
# print(num1+num2)

# 29 january
# ternary operator
# even odd
# num = int(input("Enter a number"))
# print("even") if num%2==0 else print("odd")

# # check if the person is eligible to vote
# age = int(input("Enter age"))
# print ("eligible") if age >=18 else print("not eligible")

# # positive negative
# num = int(input("Enter number"))
# print ("postive") if num>=0 else if print("zero") else print("negative")

# # pass or fail passing 33
# marks = int(input("Enter marks"))
# print ("pass") if marks>=33 else print("fail")

# divisible by 5 or not
# num = int(input("Enter number"))
# print ("divisible") if num%5==0 else print("not divisible")

# divisible by 5 or 11 or not
# num = int(input("Enter number"))
# print ("divisible") if num%5==0 and num%11==0 else print("not divisible")

# vowel or consonant
# alp = str(input("enter an alphabet : "))
# print("vowel") if alp=='a' or alp=='e' or alp=='i' or alp=='o' or alp=='u' else print("consonant")

# simple interest
# pr = int(input("Enter principle"))
# rt = int(input("Enter rate"))
# tm = int(input("Enter time"))
# si=pr*rt*tm/100
# print(si)

# square and cube of a number
# a = int(input("Enter a number"))
# print(a**2)
# print(a**3)

# 3 feb
li1 = [1,34,54,2,4,2]
li2 = [1,34,54,2,4,2]
# print(li)

# appends adds data on last ( adds whole list)
# li.append(1300)
# print(li)


# extend also adds more data unlike append i.e. without list
# li1.extend(li2)
# print(li1)

# pop removes last element from the list (if we leave the bracket blank)
# li1.pop()
# print(li1)

# remove - remove certain item from the list i.e. not according to indexing if there is duplicacy it removes the first one only
# li1.remove(54)
# print(li1)

# to remove multiple use count first and then use remove
# count - counts data in a list
# print(li1.count(2))
# print(li1)
# li1.remove(54)
# print(li1)


# clear - empties/clear the list but the list still exits
# li1.clear()
# print(li1)

# del li - deletes list
# del li1
# print(li1)

# reverse - reverses the list
# li2.reverse()
# print(li2)

# sort - sorts in ascending to do it decending = (reverse=True) to do it thru sort
# li2.sort()//ascending
# li2.sort(reverse=True)//decending
# print(li2) 
# print(li2)

# copy - makes different memory address
# li2.copy()
# print(li2)


# common functions

# len - length of data
# print(len(li2))

# max - max value
# print(max(li2))

# min - min value
# print(min(li2))

# sum - adds value
# print(sum(li2))
# heterogenous which can store multiple data

# 4 feb

# tuple
# immutable -> non changable
# same as list
# duplicate allowed
# heterogenous
# indexing
# insertion order preserved
# data = ()
# data = tuple()
# it will give the data type if only one variable inserted inside a tuple
# data = (1,2,3,4)
# print(data)
# cant make changes to tuple 
# len max min sum of data can be used also
# data.count
# data.index
# sorted is extra it will arrange in ascenind order but in list format but you will have to store it in a value
# use tuple if u dont want anyone to make changes in a data


# data = 1,2,3,4 # packing of data it will give in tuple
# a,b,c,d = data # unpacking of data , if u put more variables than required it will give error

# 6 feb
# set{}
# to make a blank set - data.set{

# unique values are stored not duplicate (not allowed)
# unordered data is stored
# indexing not allowed 
# mutable
# heterogenous data allowed
# data = {1,2} #dictionary if blank, set if data inside

# print(type(data))
# to add element in a set
data = {12,4,43,23}

# data.add(100) # to add single data
print(data)

# data.update()# to add multiple data
# data.pop() # to remove last data (randomly will delete data)
# data.remove() # to remove particular data passes error
# data.discard() #to remove data doesnt pass error
# data.clear() #clears value of set but set is stil present
# del data() # deletes whole set

# mathamatical function of set
# union
# intersection
# difference
# symmentic_difference

# data1={10,30,20,40}
# data2={10,50,20,60}

# data.union - combine both set and take duplicate value  
# data1=data1.union(data2)
# print (data1)

# data.intersection - common value
# data.difference - returns unique value of itself(present in x but not in y)
# data.sym_diff - returns unique values only

# 11 feb
# flavour of python - cpython
# 35 keywords
# normal and sofr keywords
# - case match type - soft keywords
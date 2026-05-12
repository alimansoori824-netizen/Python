# for variable in iterable(collection data type - str,list,tuple,dict,range,set):
    # for body


# ord() - converts char into ascii value
# chr() - converts ascii value into char

# adding string 
# A -> B
# B -> C

# s=input("Enter char")
# x=ord(s)
# print(x)

# y=x+1#jump of +1
# z=chr(y)
# print(z)

# jump will be given in ques
# if multiple char - we use for loop

# short code
# ch=input("Enter char")
# print(chr(ord(ch)+2))


# s=input("Enter string")
# for ch in s:
#     print(chr(ord(ch)+1))
    

# output together
# s=input("Enter string")
# s1=''
# for ch in s:
#     s1=s1+chr(ord(ch)+1)

# print(s1)


# 23 april --------------------------------------------------------------------------------------------------
# l=[10,20,30,40,50]
# l1=[]
# for i in l:
    # print(i)
    # print(i+5)#adds 5 in every element
    # l1.append(i**2)#square of every element

# print(l1)

# t=(1,2,3,4,5)
# l=list(t)
# l1=[]
# # typecasting - converstion of one data type into another e.g convert tuple into list
# # print(type(t1))#typecasting example
# #to perform action in tuple , we must convert it into list first cuz its mutable
# for i in l:
#     l1.append(i+5)

# t=tuple(l1)
# print(t)

# l=[1,2,3,4,5]

# for i in range(len(l)):
#     x=l[i]+5 #either this 
#     # l[i]=l[i]+5 #or this
#     l[i]=x

# print(l)

# d={'x':10,'y':20,'z':'python'}
# for i in d:#d can be modified
    # print(i)#targets key and prints it 
    # print(i,'=',d[i])#targets both key and value and prints it

# if d in for loop is d.keys() -> same output , will print keys
# if d in for loop is d.values() -> will print values


# if d in for loop is d.items() -> will print both keys and values in pair in tuples 
# we'll take 2 var in loop cuz it gives both key and value

# for i,j in d.items():
#     print(i,'=',j)

# for i in d:
    # print(d[i])#prints values

# s={10,20,30,'python','java'}

# for i in s:
#     print(i)#set is unordered

# we wont use set and frozen set cuz it is unordered

n=5
for i in range(1,n+1):
    print('*'*i)

n=1
for i in range(5,n-1,-1):
    print('*'*i)
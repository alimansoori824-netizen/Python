##26 march
##datatypes

##numeric-
##int
##float
##complex

##ordered-
##string -->collection of characters, enclosed with single double and triple quote,duplicates are allowed,indexing supported,slicing allowed,ordered collection,immutable in nature 
##list
##tuple

##map data type-
##dict

##     -
##set
##frozenset
##boolean
##namespace

##inbuilt function -
##print()
##input()
##type()
##id() - memory address

##max() - shows element of highest ascii value
##min() - 
##sum() - 
##len() - shows count/length of data


##30march ----------------------------------------------------------------------------------

##ascii values-
##A-Z = 65-90
##a-z = 97-122
##0-8 = 48-57
##'  ' = 32

# s=input("enter name ")
# print(f'this is {s}')
# print(f'type of {s} is {type(s)}')
##f''is a better way than print()
# print(ord('A')) - shows ascii value

# -------------------------------------------------------------------------------------------
# 31 march

# string methods - 
# lower() - converts into lowercase
# upper() - upper case
# title() - makes 1st char of each word capital
# swapcase() - makes uppercase to lowercase and vice versa
# startswith() - wheather start from a specific char or not - return true or false
# endswith() - wheather ends ---------------
# split() - breaks 
# join() - joins string into one
# index() - finds position of an element
# count() - tells frequency/ no of repition of a char

# jango helps in development of a webpage in python(uses html,css)
# syntax
# collection.method
# example


# s=input("Enter your name") 
# print(s.lower()) # converts upper to lowercase
# print(s.upper()) # converts lower to uppercase
# print(s.title()) # makes a title
# print(s.swapcase()) #makes cap into smol and vice versa
# print(s.capitalize()) #makes 1st letter cap
# print(s.count('a')) - counts specific char
# print(s.index('m')) - index position of a char

# index() -
# s=input("Enter any string :")
# ch=input("Enter any char :")
# start=int(input("Enter start point :" )) # will start seaching from this point
# stop=int(input("Enter stop point :" )) # will search till this point
# print(s.index(ch,start,stop))

# print(s.index(input("Enter any char :")),int(input("Enter start point :" )),int(input("Enter stop point :" )))
# optimized code

# dynamic count() - 
# s=input("Enter string")
# ch=input("Enter char")
# print(s.count(ch))

# hw 
# try "is" methods eg ch.is" "
# "is" ones returns boolean value or checks 

# 2 april

# syntax
# string.split(arg1,arg2)
# arg1- from where we wanna split , arg2 how many times we wanna break 
# by default it takes space as arg
# s="This is python class"

# print(s.split())
# print(s.split(' ',2))#space breaks and 1 breaks it into two space
# print(s.split(' ',0))#space breaks and 0 wont breaks it into any space
# print(s.split(' ',))#breaks it into default space
# print(s.split('p'))#p wont come in result 
# split - 2arguement ('split from',how many times split(count))
# by default - split breaks from space

# s="This is python python python"
# print(s.split('p'))# if multple p then every p will get replaced

# strip
# m='||| Python |||'
# print(m.strip('|')) # removes all |
# print(m.lstrip('|')) # removes all left |
# print(m.rstrip('|')) # removes all right |


# join - join 2 strings
# syntax - join()
# one arg only
# variable/arg shud be iterable(means collection)
# thats why1 list inside them multiple strings

# s1="Python"
# s2="Java"
# s3="PHP"
# x=",".join([s1,s2,s3])
# print(x)

# startswith
# s='python'
# print(s.startswith('p'))#true
# print(s.startswith('w'))#false

# endswith 
# s='python'
# print(s.endswith('n'))#true
# print(s.endswith('w'))#false
# can also take multiple arg i.e py

# 'is' methods returns boolean values only 

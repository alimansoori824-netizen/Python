# 8 april

# dictionary
# collection of key:'value' pairs
# enclosed by curly braces
# pairs are seperated by comma (,)
# key value seperated by colon(:)
# key must be unique
# value may be duplicate
# indexing not supported
# slicing not supported
# mutable in nature

# d1={1:'Ali',
#    2:37,
#    3:'bhopal'
# }
# d2={'name':'Ali',
#     'age':37,
#    'city':'bhopal'
# }
# print(d)
# print(type(d))
# print(len(d))
# print(max(d1))#name cuz n in name is the max
# print(min(d1))#age cuz a in age is min
# min max depends on key
# sum also targets key(error)
# print(sum(d))#sum will work 1+2+3
# print(sum(d1))

# dictionary methods - 
# copy() - same elements -> creates new object (prove by memory address)
# clear() - removes both keys and values/allpairs so it becomes useless -> use del to delete
# get() - d.get('key)   if we want value from a dictionary (pass key inside to get value of key)
# keys() - returns all key
# values() - returns all values
# items() - returns both (key and value)
# fromKeys() - if new dict and same keys as before takes keys with no value and return null
# update() - merge 2 dict
# setdefault() - can add new key value pair (new key shudnt be the existing one)
# pop() - targets key and removes it
# popItems() - removes last key value pair



# d={'name':'Ali',
#     'age':37,
#    'city':'bhopal'
# }
# print(d)

# i=eval(input("Enter any dict : "))
# d3= i.copy()
# print(i)
# print(id(d3),id(i))#diff memory address
# d3 = i.clear()
# print(d3)

# del i
# print(i)
# print(i.keys())
# print(i.values())
# print(i.items())#both key and value
# x = i.get('age')#specific key name

# 9 april
# dict is an object and memory address is assigned to it
# pop removes key from the dict
# popitem removes last pair 
# print(i.popitem())#returns key first
# print(i)
# {'name':'ali','city':'bhopal'}

# iterable -> collection of element
# l={'name','city'}
# s='python'
# d=dict().fromkeys(l)#makes name and city values none
# d=dict().fromkeys(s)#makes each char(python)into a diff key
# d=dict().fromkeys(s,10)#makes each char(python)into a diff key and 2nd arg assign value
# print(d)

# update
# d1={'name','city'}
# d2={'age','email'}
# d1.update(d2)
# print(d1)

# SetDefault
# to add new pair
# if key already exists it wont change the value
d1={'name':'python','city':'Bhopal'}
d1.setdefault('name','ali')#wont affect name's value
#              key    value
d1.setdefault('name1','ali')
print(d1)

# web designing is mostly done in dict and list
# cuz they both are mutable 
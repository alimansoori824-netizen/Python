# 10 april
# set
# unordered collection - order isnt fixed
# thats why indexing not supported
# thats why slicing also not supported
# unique value
# enclosed with curly braces{} and comma(,)seperated elements
# use heterogenous collection to differentiate
# mutable in nature
# elements are printed thru hashing algo
# duplicate items are printed once only
s={1,2,3,4,'python','java','php'}
# print(s)
# print(type(s))
# print(id(s))
# print(len(s))
# print(max(s))#biggest element (btwn int and str it cant give output)
# print(min(s))#same error
# print(sum(s))#same error

# 1 set methods
s1={1,2,3,4,5}
s2={4,5,6,7,8}
# multiple(2 or more) set methods -
# union()-creates new set between 2 sets and common values will be printed once only in the new set
# intersection() - common value btwn 2 sets
# difference() - the values which arent in 1st set will be prnted
# symetric-difference() - opposite of intersection - wont print the common values of 2 sets
# till here new set create
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))




# intersection.update()- updates common value in old set
# difference-update()- 
# symentic-difference.update()
# till here old set update
# print(s1.intersection_update(s2))
# print(s1)



# issubset
# issuperset
# till here boolean



# 13 april
# set methods
# add() - add single element in single postition
# update() - add multiple element in random postition
# remove() - remove element (not in collection - error)
# discard() - same but doesnt throw error(continues code)
# pop() - remove random element
# clean() - removes all element
# copy() - new object of same element

# s={1,2,'java','python','python'}
# ne=(3,4,'php')#tuple
# print(type(ne))
# s.add(ne)
# print(s)

# new={2,4,6}
# s.update(ne)
# print(s)

# s.remove('python')#doubt
# s.discard('python')
# print(s)

# s.copy()
# print(s)

# s.clear()
# print(s)

# ----------------------------------------------------------


#  1. add()  add a single element
# Adds one element to the set.
# s = {1, 2, 3}
# s.add(4)
# print(s)
#  Output:
# {1, 2, 3, 4}


#  2. update() → add multiple elements
# Adds multiple elements (from list, tuple, set, etc.)
# s = {1, 2}
# s.update([3, 4, 5])
# print(s)
#  Output:
# {1, 2, 3, 4, 5}


#  3. remove() → remove element (gives error if not found)
# s = {1, 2, 3}
# s.remove(2)
# print(s)
#  Output:
# {1, 3}

#  If element not present:
# s.remove(10)   # Error
#  Error:
# KeyError



#  4. discard() → remove element (no error)
# s = {1, 2, 3}
# s.discard(10)   # no error
# print(s)
#  Output:
# {1, 2, 3}


#  5. pop() → remove random element
# Removes any random element (since sets are unordered).
# s = {1, 2, 3}
# s.pop()
# print(s)
#  Output (can vary):
# {2, 3}



#  6. clear() (not clean()) → remove all elements ✅
# s = {1, 2, 3}
# s.clear()
# print(s)
#  Output:
# set()


#  7. copy() → create a new set
# s = {1, 2, 3}
# new_s = s.copy()
# print(new_s)
#  Output:
# {1, 2, 3}


# freeze
# to freeze a set - you cant make changes 

# update methods wont work on it then

s={1,2,3,'python','php'}
fs=frozenset(s)
print(fs)
print(type(fs))
print(len(fs))
# print(sum(fs))#error

# list - collection of heterogenous(diff datatype of elements) and homogenous(same datatype) data
# enclose with []
# ordered collection
# indexing support
# slicing support
# mutable in nature (changable)

l = eval(input("Enter any list"))#used eval so it doesnt return as string
print(l)
# if data is heterogenous inside list then max min and sum won't work
print(type(l))
print(id(l))
print(len(l))
# print(max(l))
# print(min(l))
# print(sum(l))

# ['python','java',20,30]
# error in max , min and sum

# list methods
# copy() - create new object with same elements (diff memory address means they are diff lists)
# append() - add single element at last position
# clear() - clear all elements from given list
# extend() - add multiple elements at last position
# insert() - add single element at targeted position
# pop() - removes element on the basis of indexing (by default -1 means it deletes last position)
# remove() - directly targets element 
# sort() - arrange in ascending order 
# reverse() - reverse out all inde postion
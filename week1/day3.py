#Collections

#Lists
lst =[1, 3, "Hello", 2.5]
print(lst[1])
lst.append("last")
lst.pop(2)
print(lst)


#SETS
set1 = {1, 3, 5, 7, 9, 2, 4, 6, 8, "hello", "goodbye"}
print(set1) # prints in numerical/alphabetucal
set1.add(8)
print(set1) #wont repeat an 8 since there is one
#lst_set = list(set1).sort()


set2 = {2, 4, 6, 8, 0}
print(set1.intersection(set2)) #what they have in common 
print(set1.union(set2)) # all values in both set


set1.remove(8)
for i in range(len(set1)):
    set1.pop()
    print(set1)
print(set1)

# TUPLES
tup = (1, 2, 3)
print(tup)
print(tup[2])
#tup[0]= 10 - WILL NOT WORK
tup = (2, 4, 6)
print(tup)

tup1 = tuple([3])
print(type(tup1))

#customers = [('first', 'last'), ('gabriel','klein'), ('fred', 'johnson')]
#for elem in customers:
#   print(elem[1])


print("*** DICTIONARIES ***")
dict1 = {"fred":35, "stacy":35, "tom":22, "fred":42} #adding fred again will print one updated fred
print(dict1)
dict1["leah"] = 42
print(dict1)
dict1["stacy"] = 36
print(dict1) 


dict1.pop("leah")
print(dict1)

for key in dict1.keys():
    print(key + "_____" + str(dict1[key]))



import collections as c
# from collections import Counter  #is another way we can import directly to "Counter" instead of having to use "c.Counter"

# COUNTERS

count1 = c.Counter([1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 3, 2])
print(count1)

count2 = c.Counter(A=3, B=5, C=2)
print(count2)

lst = ["apple", "Apple", "APPLE"] #example that counts but differs in capital
print(c.Counter(map(lambda elem: elem.lower(), lst))) #map is a function that computes the arguement at each of the intervals but will have to use lambda

# ORDERED DICTIONARY
od = c.OrderedDict()
od["a"]=  3
od["b"] = 2
od["c"] = 1

print(od)


#DEFAULT DICTIONARY
#dict1 = {"a":1, "b":2, "c":3}
#print(dict1["d"])
# look @ video/notes
dict1 = c.defaultdict(int)
dict1["a"] = 1
dict1["b"] = 2
dict1["c"] = 1

print(dict1["d"])
print(dict1)

#NAMED TUPLE
Employee = c.namedtuple('Employee',['name', 'age', 'dept'])

emp1 = Employee("fred", 35, "IT")
print(emp1)
print(emp1[0])
print(emp1.name)



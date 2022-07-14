#def filter_list(lst) -> list:
#1) Write a Python function that will take in a list of numbers and return a new list of numbers that include only the elements of the first that are between 10 and 19 (inclusive)
	
	#ex) filter_list([1, 3, 5, 9, 10, 45, 26, 19, 15, 3]) ------> [10, 19, 15]


#** ERROR****
# lst1 = [1, 3, 5, 9, 10, 45, 26, 19, 15, 3]
#def filter_lst(lst):
	#for i in range(len(lst)):
		#lst.remove(lst[i] >10 and [i]<19)
	#return lst
#print(filter_lst(lst1))
#***ERROR***

lst1 = [1, 3, 5, 9, 10, 45, 26, 19, 15, 3]

def filter_lst(lst1):
	lst2 = []
	for x in lst1: 
		if x >= 10 and x <= 19: 
			lst2.append(x)  
	print(lst2)
	return lst2 

filter_lst(lst1)


#def intersect_sets(set1, set2) -> set:
#2) Write a Python function that will take in two sets and return the intersection of both. If there are no common values, print to the console that there are no common values.
	
	#ex) intersect_sets({1, 2, 3}, {2, 3, 4, 5}) ------> {2, 3}

set1 = {1, 2, 3}

set2 = {2, 3, 4, 5}

def intersect_sets(set1, set2) -> set:
	set3 = set1.intersection(set2)
	if set3 == set():
		print("There are no common values")
	print(set3)
intersect_sets(set1, set2)

#def create_dict(lst_keys, lst_values) -> dict:
#3) Write a Python function that will take in a list of unique keys and a list of tuples that will represent values, and return a dictionary with each element in the lst_values mapped to a key in lst_keys. lst_values will be a list of tuples, lst_keys will be a list of strings. length of each list will be the same.

	#ex) create_dict(["fred", "stacy", "bob"], [(1, 5), (4, 7), (9, 2)]) ------> {"fred":(1, 5), "stacy":(4, 7), "bob":(9, 2)}


def create_dict(lst_keys, lst_values) -> dict:
	result = (dict)
	length = len(lst_keys)
	for i in range(length):
		result[lst_keys[i]] = lst_values[i]
	print(result)
	return result

create_dict(["fred", "stacy", "bob"], [(1, 5), (4, 7), (9, 2)])

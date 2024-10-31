#Task1

my_set = set()
my_set.add("apple")
my_set.add("banana")
my_set.add("orange")


#Task2

for item in my_set:
    print(item)

#Task3

my_set.update(["grape", "melon", "kiwi"])


#Task4

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  



my_set = {1, 2, 3}
my_set.discard(4)
print(my_set)  

#Task5

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
common_values = set_a.intersection(set_b)
print(common_values)  


#Task6

#difference and difference update

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

difference_values = set_a.difference(set_b)
print(difference_values) 

set_a.difference_update(set_b)
print(set_a)  


#intersection and intersection update

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

intersection_values = set_a.intersection(set_b)
print(intersection_values)  

set_a.intersection_update(set_b)
print(set_a) 

#symetries

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

symmetric_difference_values = set_a.symmetric_difference(set_b)
print(symmetric_difference_values) 

set_a.symmetric_difference_update(set_b)
print(set_a)  

'''
- difference: Returns a new set containing the elements that are in the first set but not in the second set.
- difference_update: Modifies the first set by removing the elements that are also present in the second set.
- intersection': Returns a new set containing the elements that are common to both sets.
- intersection_update: Modifies the first set by keeping only the elements that are also present in the second set.
- symmetric_difference*: Returns a new set containing the elements that are in either of the sets, but not in both.
- symmetric_difference_update: it Modifies the first set by keeping only the elements that are in either of the sets, but not in both.
Example with difference and difference update'''
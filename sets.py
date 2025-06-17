#using set() constructor
beverages = set(["coffee", "juice", "tea"])
print("Beverages set:", beverages)

#adding items to set
beverages.add("milk")
beverages.add("soda")
print("Updated beverages set:", beverages)

#checking if item present
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("Is 'microwave' present?", "microwave" in mySet)

#removing an item from set
mySet.remove("kettle")
print("After removing kettle:", mySet)

#looping through the set
for item in mySet:
    print(item)

#adding list items to a set
my_set = {"apple", "banana", "cherry", "date"}
my_list = ["fig", "grape"]
my_set.update(my_list)
print("Set after adding list elements:", my_set)

#combining two sets
ages = {21, 22, 23}
first_names = {"Shamillah", "Diana", "Emma"}
combined = ages.union(first_names)
print("Combined set:", combined)







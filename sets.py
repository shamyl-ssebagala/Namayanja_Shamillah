# Exercise 3: Sets

# 1. Use set() constructor to create a set of 3 favorite beverages
beverages = set(("Tea", "Coffee", "Juice"))
print("Beverages set:", beverages)

# 2. Add 2 more items to the beverages set
beverages.add("Milk")
beverages.add("Soda")
print("After adding items:", beverages)

# 3. Check if "microwave" is present in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}

if "microwave" in mySet:
    print("microwave is present in the set")
else:
    print("microwave is not present")

# 4. Remove "kettle" from the set
mySet.remove("kettle")
print("After removing kettle:", mySet)

# 5. Loop through the set
print("Items in mySet:")
for item in mySet:
    print(item)

# 6. Add list elements to a set
my_set = {"book", "pen", "bag", "phone"}
my_list = ["charger", "earphones"]

for item in my_list:
    my_set.add(item)

print("Updated set:", my_set)

# 7. Join two sets (ages and first names)
ages = {18, 20, 22, 25}
first_names = {"Shamyla", "Brian", "Sarah"}

joined_set = ages.union(first_names)

print("Joined set:", joined_set)
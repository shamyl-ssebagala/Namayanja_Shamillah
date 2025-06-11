 # List of names
names = ["Alice", "Brian", "Cynthia", "David", "Emma"]

# Output the second item
print("The second name is:", names[1])

# Change the first item to a new value
names[0] = "Alex"

# Print the updated list
print("Updated list:", names)

# Add a sixth item
names.append("Frank")

# Print the updated list
print("Updated list with sixth name:", names)

# Insert "Bathel" as the third item (index 2)
names.insert(2, "Bathel")

# Print the updated list
print("Updated list with Bathel as the third item:", names)

# Remove the 4th item (index 3)
removed_item = names.pop(3)

# Print the updated list and the removed item
print("Removed item:", removed_item)
print("Updated list after removing the 4th item:", names)

# Print the last item using negative indexing
print("The last item is:", names[-1])

# New list with 7 items
colors = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Black"]

# Print the 3rd, 4th, and 5th items (index 2 to 4)
print("3rd to 5th items:", colors[2:5])

# List of countries
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda"]

# Make a copy
countries_copy = countries.copy()

print("Original:", countries)
print("Copy:", countries_copy)

#loop through
for country in countries:
    print("Country:", country)

#list of animals
animals = ["zebra", "elephant", "lion", "giraffe", "antelope"]

# Ascending order
animals.sort()
print("Ascending:", animals)

# Descending order
animals.sort(reverse=True)
print("Descending:", animals)

#animals with only letter "a"
for animal in animals:
    if 'a' in animal:
        print("Animal with 'a':", animal)
        
#combining two new lists
    first_names = ["John"]
second_names = ["Shamillah","Ssebagala"]

# Join the lists
full_names = first_names + second_names
print("Combined names:", full_names)










# Exercise 1: Lists

# 1. Create a list with 5 names and output the 2nd item
people = ["Moryce", "Diana", "Mary", "Kayla", "Ivan"]
print("2nd item:", people[1])

# 2. Change the value of the first item
people[0] = "Shamyla"
print("After changing first item:", people)

# 3. Add a sixth item to the list
people.append("Peter")
print("After adding sixth item:", people)

# 4. Add "Bathel" as the 3rd item in the list
people.insert(2, "Bathel")
print("After adding Bathel:", people)

# 5. Remove the 4th item from the list
people.pop(3)
print("After removing 4th item:", people)

# 6. Use negative indexing to print the last item
print("Last item:", people[-1])

# 7. Create a new list with 7 items and print the 3rd, 4th and 5th items
items = ["Book", "Pen", "Bag", "Phone", "Laptop", "Bottle", "Shoes"]
print("3rd, 4th and 5th items:", items[2:5])

# 8. Write a list of countries and make a copy of it
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"]
countries_copy = countries.copy()

print("Original countries list:", countries)
print("Copied countries list:", countries_copy)

# 9. Loop through the list of countries
print("Countries:")
for country in countries:
    print(country)

# 10. List of animals and sort in ascending and descending order
animals = ["Zebra", "Lion", "Elephant", "Antelope", "Giraffe"]

animals.sort()
print("Ascending order:", animals)

animals.sort(reverse=True)
print("Descending order:", animals)

# 11. Output only animal names with the letter 'a'
print("Animals containing letter 'a':")
for animal in animals:
    if "a" in animal.lower():
        print(animal)

# 12. Join two lists containing first names and second names
first_names = ["Shamyla", "Brian", "Sarah"]
second_names = ["Ssebagala", "Mugisha", "Nantongo"]

full_names = first_names + second_names

print("Joined list:")
print(full_names)
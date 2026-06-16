# Exercise 2: Tuples

# Given tuple
phones = ("samsung", "iphone", "tecno", "redmi")

# 1. Output your favorite phone brand
print("Favorite phone brand:", phones[0])

# 2. Use negative indexing to print the 2nd last item
print("Second last phone:", phones[-2])

# 3. Update "iphone" to "itel"
phone_list = list(phones)
phone_list[1] = "itel"
phones = tuple(phone_list)
print("Updated tuple:", phones)

# 4. Add "Huawei" to your tuple
phone_list = list(phones)
phone_list.append("Huawei")
phones = tuple(phone_list)
print("After adding Huawei:", phones)

# 5. Loop through the tuple
print("Phone brands:")
for phone in phones:
    print(phone)

# 6. Remove/delete the first item in the tuple
phone_list = list(phones)
phone_list.pop(0)
phones = tuple(phone_list)
print("After deleting first item:", phones)

# 7. Create a tuple of cities in Uganda using tuple() constructor
cities = tuple(("Kampala", "Jinja", "Mbarara", "Gulu", "Masaka"))
print("Cities:", cities)

# 8. Unpack your tuple
city1, city2, city3, city4, city5 = cities
print(city1)
print(city2)
print(city3)
print(city4)
print(city5)

# 9. Print the 2nd, 3rd and 4th cities
print("2nd, 3rd and 4th cities:", cities[1:4])

# 10. Join two tuples
first_names = ("Shamyla", "Brian")
second_names = ("Ssebagala", "Mugisha")

full_names = first_names + second_names
print("Joined tuple:", full_names)

# 11. Create a tuple of colors and multiply it by 3
colors = ("Red", "Blue", "Green")
multiplied_colors = colors * 3
print("Colors multiplied by 3:", multiplied_colors)

# 12. Count the number of times 8 appears in the tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

print("Number of times 8 appears:", thistuple.count(8))
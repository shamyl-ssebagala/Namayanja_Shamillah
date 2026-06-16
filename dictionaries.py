# Exercise 5: Dictionaries

# Given dictionary
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# 1. Print the value of shoe size
print("Shoe size:", Shoes["size"])

# 2. Change "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print("After changing brand:", Shoes)

# 3. Add key/value pair "type": "sneakers"
Shoes["type"] = "sneakers"
print("After adding type:", Shoes)

# 4. Return list of all keys
print("Keys:", list(Shoes.keys()))

# 5. Return list of all values
print("Values:", list(Shoes.values()))

# 6. Check if key "size" exists
if "size" in Shoes:
    print("Key 'size' exists in dictionary")

# 7. Loop through the dictionary
print("Dictionary items:")
for key in Shoes:
    print(key, ":", Shoes[key])

# 8. Remove "color" from dictionary
Shoes.pop("color")
print("After removing color:", Shoes)

# 9. Empty the dictionary
Shoes.clear()
print("After clearing dictionary:", Shoes)

# 10. Dictionary of my choice and copy it
student = {
    "name": "Shamyla",
    "course": "Software Engineering",
    "year": 3
}

student_copy = student.copy()
print("Original:", student)
print("Copy:", student_copy)

# 11. Nested dictionaries
students = {
    "student1": {
        "name": "Brian",
        "age": 20
    },
    "student2": {
        "name": "Sarah",
        "age": 22
    }
}

print("Nested dictionary:", students)
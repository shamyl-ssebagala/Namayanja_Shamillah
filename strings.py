# Exercise 4: Strings

# 1. Concatenate an integer and a string
age = 20
text = " years old"

result = str(age) + text
print("Concatenation result:", result)

# 2. Remove spaces at beginning, middle, and end
txt = "      Hello,       Uganda!       "
clean_txt = txt.replace(" ", "")
print("Without spaces:", clean_txt)

# 3. Convert txt to uppercase
txt_upper = txt.upper()
print("Uppercase:", txt_upper)

# 4. Replace 'U' with 'V'
replaced_txt = txt.replace("U", "V")
print("Replaced string:", replaced_txt)

# 5. Return 2nd, 3rd and 4th characters
y = "I am proudly Ugandan"
print("2nd-4th characters:", y[1:4])

# 6. Fix the string error using correct quotes
x = 'All "Data Scientists" are cool!'
print(x)
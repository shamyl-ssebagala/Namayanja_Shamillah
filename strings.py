#concatenating integer and a string
age = 25
message = "I am " + str(age) + " years old."
print(message)

#removing spaces at the beginning middle and end
txt = "      Hello,       Uganda!       "
clean_txt = txt.strip().replace("       ", " ").replace("  ", " ")
print(clean_txt)

#converting to uppercase
print(clean_txt.upper())

#replacing character in the string
replaced_txt = clean_txt.replace("U", "V")
print(replaced_txt)

#Return characters in the 2nd, 3rd, and 4th positions of y
y = "I am proudly Ugandan"
print(y[1:4])

#Correct the string with quotation mark error
x = 'All "Data Scientists" are cool!'
print(x)








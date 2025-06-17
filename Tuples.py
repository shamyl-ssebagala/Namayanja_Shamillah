# Original tuple
x = ("samsung", "iphone", "tecno", "redmi")

#favourite phone brand using the index
print("My favorite phone brand is:", x[1]) 

#using negative indexing
print("Second last item:", x[-2])

#update item, change to list then back to tuple
x_list = list(x)
x_list[1] = "itel"
x = tuple(x_list)
print("Updated tuple:", x)

#adding new item
x = x + ("Huawei",)
print("Tuple after adding Huawei:", x)

#looping through
for phone in x:
    print(phone)

#deleting using the index
x = x[1:]
print("After removing first item:", x)

#using tuple() constructor
cities = tuple(["Kampala", "Entebbe", "Gulu", "Mbarara", "Jinja"])
print("Cities tuple:", cities)

#unpack tuple
city1, city2, city3, city4, city5 = cities
print(city1, city2, city3, city4, city5)

#Use a range of indexes to print 2nd, 3rd, and 4th cities
print("Selected cities:", cities[1:4])

#joining two tuples
first_names = ("Shamillah", "Namayanja")
second_names = ("Diana", "Namatovu")
full_names = first_names + second_names
print("Full names tuple:", full_names)

#multiplying tuples
colors = ("red", "blue", "green")
colors_multiplied = colors * 3
print("Multiplied colors:", colors_multiplied)

#counting items 
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print("Number of times 8 appears:", thistuple.count(8))














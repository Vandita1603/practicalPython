#Ways to sort list of dictionaries by values in Python – Using lambda function
l1 = [{"name": "Nandini", "age": 20},
       {"name": "vandita", "age": 20},
       {"name": "preeti", "age": 19}]
# using sorted and lambda to print list sorted
# by age
print("The list sorting by age: ")
print(sorted(l1, key=lambda i: i['age']))
print("\r")
# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print("The list sorting by age and name: ")
print(sorted(l1, key=lambda i: (i['age'], i['name'])))
print("\r")
# using sorted and lambda to print list sorted
# by age in descending order
print("The list sorting by age in descending order: ")
print(sorted(l1, key=lambda i: i['age'], reverse=True))
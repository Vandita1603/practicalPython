#Ways to sort list of dictionaries by values in Python – Using item getter
from operator import itemgetter
# Initializing list of dictionaries
l1 = [{"name": "Nandini", "age": 20},
       {"name": "Vandita", "age": 20},
       {"name": "Preeti", "age": 19}]
# using sorted and itemgetter to print list sorted by age
print("The list sorting by age: ")
print(sorted(l1, key=itemgetter('age')))
print("\r")
# using sorted and itemgetter to print
# list sorted by both age and name
# notice that "Manjeet" now comes before "Nandini"
print("The list sorting by age and name: ")
print(sorted(l1, key=itemgetter('age', 'name')))
print("\r")
# using sorted and itemgetter to print list
# sorted by age in descending order
print("The list sorting by age in descending order: ")
print(sorted(l1, key=itemgetter('age'), reverse=True))
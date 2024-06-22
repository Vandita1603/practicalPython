def Merge(dict1, dict2): 
    res = dict1 | dict2
    return res 
       
# Driver code 
dict1 = {'x': 10, 'y': 8} 
dict2 = {'a': 6, 'b': 4} 
dict3 = Merge(dict1, dict2) 
print(dict3)
print("OUTPUT OF ANOTHER METHOD --> ")
dict1.update(dict2)
print(dict1)
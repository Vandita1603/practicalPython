#Python program to find the sum of all items in a dictionary
dict1={'math':97,'computer':95, 'science':87}
print(dict1.values())
sum=0
for i in dict1.values():
    sum =sum+i

print("the sum is :- ", sum)
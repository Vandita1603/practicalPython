#Python program to find second largest number in a list
list1 = [10, 20, 4, 45, 99]
 
# mx = max(list1[0], list1[1]) 
# secondmax = min(list1[0], list1[1]) 
# n = len(list1)
# for i in range(2,n): 
#     if list1[i] > mx: 
#         secondmax = mx
#         mx = list1[i] 
#     elif list1[i] > secondmax and \
#         mx != list1[i]: 
#         secondmax = list1[i]
#     elif mx == secondmax and \
#         secondmax != list1[i]:
#           secondmax = list1[i]
 
# print("Second highest number is : ",\
#       str(secondmax))

list1.sort()
# print(list1)
print("the second largest element is :", list1[-2])

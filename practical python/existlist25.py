list1=[56,78,0,9,2,4]
item=78
if item in list1:
    print(item," exists")
else:
    print(item," does not exists")
#=================================
print("output of another method ----->")
e_count=list1.count(8)
if e_count>0:
    print("element exist")
else:
    print("does not exist")
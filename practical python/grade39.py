#Program to create grade calculator in Python 
m= 44
cs = 67
h= 76
e = 99
s = 58
 
tot = m+e+cs+h+s
avg = tot / 5
 
if avg >= 91 and avg <= 100:
    print("Your Grade is A1")
elif avg >= 81 and avg < 91:
    print("Your Grade is A2")
elif avg >= 61 and avg < 81:
    print("Your Grade is B")
elif avg >= 41 and avg < 61:
    print("Your Grade is C")
elif avg >= 22 and avg < 41:
    print("Your Grade is D")
else:
    print("Invalid Input!")
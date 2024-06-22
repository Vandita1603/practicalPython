st= 2
n=int(input("Enter a number :-"))
sq=0
for i in range(0,n):
    print(st, end="+")
    sq += st
    st = st * 10+2
print("\n The sum of series is :-",sq)
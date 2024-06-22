from collections import Counter
arrayA = ['Sun', 12, 14, 11, 34]
arrayB = [6, 12, 'Sun', 11]
arrayC = [19, 6, 20, 'Sun', 12, 67, 11]
arrayA = Counter(arrayA)
arrayB = Counter(arrayB)
arrayC = Counter(arrayC)
# Intersection
commonDict = dict(arrayA.items() & arrayB.items() & arrayC.items())
res = []
# result
for (key, val) in commonDict.items():
   for i in range(0, val):
      res.append(key)
print("The common values among the arrays are:\n ",res)
#Python | Sort Python Dictionaries by Key or Value
d={5: 'vandita', 6:'anvesha',4: 'preeti', 3:'kajal', 2: 'saumya', 1:'tina'}
myk=list(d.keys())
myk.sort()
sd={i : d[i] for i in myk}
print(sd)
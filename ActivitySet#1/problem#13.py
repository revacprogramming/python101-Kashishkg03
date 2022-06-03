# Network Programming
# https://www.py4e.com/lessons/network
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d =dict()
for line in handle:
    if not line.startswith("from"):
        continue 
        
lst = list()
for value,count in d.items():
    lst.append(values,count)
lst.sort()
for value,count in lst:
    print(value,count)
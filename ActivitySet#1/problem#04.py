hrs = input("Enter Hours: ")
h = float(hrs)
rate = input("enter the rate: ")
r=float(rate)
if h<=40:
	print(h*r)
else:
    print(40*r + (h-40)*1.5*r)
score = float(input("Enter Score from'0.0-1.0'"))
if score<=1.0:
 if score >=0.9:
    print("A")
elif score>= 0.8:
    print("B")
elif score>= 0.7:
    print("C")
elif score>= 0.6:
    print("D")
elif score< 0.6:
    print("F")
else:
    print("out of order from'0.1-1.0'")


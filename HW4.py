score = float(input("Enter Score: "))
if 1>score>0:
    if 1>=score>=0.9:
        print("A")
    elif 0.9>score>=0.8:
        print("B")
    elif 0.8>score>=0.7:
        print("C")
    elif 0.7>score>=0.6:
        print("D")
    elif score<0.6:
        print("F")
    else:
        print("Please enter a valid(in the range of 0 and 1) value.")

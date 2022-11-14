def computepay(h, r):
    if h > 40:
        return 40*r+(h-40)*r*1.5
    elif h<=40:
        return h*r

hrs = input("Enter Hours:")
h = float(hrs)
r = float(input("Rate? "))
p = computepay(h, r)
print("Pay", p)


hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Please input rate: ")
hRate = float(rate)
if h > 40:
    ourPrice = 40*hRate+(h-40)*hRate*1.5
elif h <= 40:
    ourPrice = h*hRate
print(ourPrice)

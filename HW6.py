numbers = []

while True:
    num = input("Please enter a number> ")
    if num.upper() == "DONE":
        print(f"Maximum is {max(numbers)}")
        print(f"Minimum is {min(numbers)}")
        break
    else:
        try:
            intNum = int(num)
            numbers.append(intNum)
        except:
            print("Invalid input")
            continue
        continue


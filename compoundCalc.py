principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Please enter the principle amount:\n"))
    if principle < 0:
        print("Principle cant be less than or equal to zero!")
    else:
        break

while True:
    rate = float(input("Please enter the interest rate:\n"))
    if rate < 0:
        print("Interest rate cant be less than or equal to zero!")
    else:
        break

while True:
    time = int(input("Please enter the time:\n"))
    if time < 0:
        print("Time cant be less than or equal to zero!")
    else:
        break


total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
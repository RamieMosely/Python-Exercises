principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Please enter the principle amount:\n"))
    if principle <= 0:
        print("Principle cant be less than or equal to zero!")

while rate <= 0:
    rate = float(input("Please enter the interest rate:\n"))
    if principle <= 0:
        print("Interest rate cant be less than or equal to zero!")

while time <= 0:
    time = int(input("Please enter the time:\n"))
    if time <= 0:
        print("Time cant be less than or equal to zero!")

total = principle * pow((1 + rate / 100), time)
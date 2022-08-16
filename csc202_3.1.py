years = int(input("Enter number of years: "))
print(" ")
num = 0
add = 0
year = 1
for i in range(years):
    for a in range(12):
        num += 1
        inch = float(input("Enter inches of rainfall for month " + str(num) + " of year " + str(year) + ": "))
        add += inch
        if  num % 12 == 0:
            year += 1
            num -=12
            print(" ")

months = years * 12
average = add / months
print("Total number of months: " + str(months))
print("Total inches of rainfall: " + str(add) + " inches")
print("Average rainfall per month for entire period: " + str(average) + " inches")

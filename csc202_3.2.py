#A Colour Mixing Program
print("This is a colour mixing program")
primary = ["red", "blue", "yellow"]
secondary = ["purple", "orange", "green"]

colour1 = input("Enter your first primary colour: ")
colour1 = colour1.lower()
if colour1 == primary[0] or colour1 == primary[1] or colour1 == primary[2]:
    print(" ")
else:
    print("Error: Incorrect entry")
    
colour2 = input("Enter your second primary colour: ")
colour2 = colour2.lower()
if colour1 == primary[0] or colour1 == primary[1] or colour1 == primary[2]:
    print(" ")
else:
    print("Error: Incorrect entry")
if colour1 == colour2:
    print("You entered the same colour twice!")
else:
    if colour1 == "red" and colour2 == "blue":
        print("Your colour is " + secondary[0])
    elif colour1 == "blue" and colour2 == "red":
        print("Your colour is " + secondary[0])
    elif colour1 == "red" and colour2 == "yellow":
        print("Your colour is " + secondary[1])
    elif colour1 == "yellow" and colour2 == "red":
        print("Your colour is " + secondary[1])
    else:
        if colour1 == "blue" and colour2 == "yellow":
            print("Your colour is " + secondary[2])
        else:
            if colour1 == "yellow" and colour2 == "blue":
                print("Your colour is " + secondary[2])

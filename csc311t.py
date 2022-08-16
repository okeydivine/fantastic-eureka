import numpy as np

#These lists are created to hold the values
dictionary = []
const = []
#These lists hold useful variables for use in the defined functions
var = ['p','q','r','x','y','z']
eq = ["equation_1","equation_2","equation_3","equation_4","equation_5","equation_6"]
#This function will prompt the user for entries
def entry():
    l = []
    for j in var:
        j = int(input("Co-efficient of " + j + ": "))
        l.append(j)
    return l

def c_entry():
    c = int(input("Constsant: "))
    const.append(c)

def p_result():
    for i in range(0,6):
        result = var[i] + " = " + str(round(X[i]))
        print(result)

print("\nEnter values for the 6 by 6 equation\n")
n = 0
for i in range(0,6):
    print("The following entries are for the " + eq[n])
    r = entry()
    dictionary.append(r)
    c_entry()
    n+=1
    print("\n")

#The real work begins....

A = np.array(dictionary)
B = np.array(const)
X = np.linalg.solve(A,B)

print(X)
print("Your results:")
p_result()
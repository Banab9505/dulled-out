a = 76
b = 32
c = 2



def function():
    if 3 > 9:
        print("cookies")
    elif a + 43 > 200:
        print("not cookies")
    else:
        if 9 > 32:
             print(3 ** 2)
        else:
            if a + c == c + 76:
                print("stand")
            else:
                print("balloon")
print("hello")

function()
def simple():
    if a + b == c + 106:
        print(42/6)
    else:
        function()
simple()

def expression(x):
    return 6*x
d = expression(6.7)
print(d)


#1 ml = 1.6 km

def kilometers(x):
    print("kilometers: ")
    return 1.6*x
  

f = kilometers(9)
print(f)

#total is always the positive sum and the other variable follows the entire list
j = 1
total = 0
total2 = 0
total3 = 0
m = 0
for m in range(1, 5):
    total += m
print(total)

           
while j < 5:
    total2 += j
    j += 1
print(total2)


e = [5, 4, 3, 3, 2, 1, 1]
total3 = 0
i = 0
while i < len(e) and e[i] > 0:
    total3 += e[i]
    i += 1
print(total3)

e2 = [5, 4, 4, 3, 3, 2, 1, -1, -2, -2, -3]
total4 = 0
v = 0
for v in e2:
    total4 += v
print(v)


e3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

total5 = 0
z = len(e3)-1
while e3[z] < 0:
    total5 += e3[z]
    z -= 1
print(total2)
    






    



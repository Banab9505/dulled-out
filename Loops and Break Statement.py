#total is always the positive sum and the other variable follows the entire list
j = 1
total = 0
total2 = 0
total3 = 0
f = 0
for f in range(1, 5):
    total += f
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
b = 0
for b in e2:
    total4 += b
print(b)


e3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

total5 = 0
c = len(e3)-1
while e3[c] < 0:
    total5 += e3[c]
    c -= 1
print(total2)
    






    

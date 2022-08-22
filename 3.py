row = []
rowlength = int(input("enter the length of the row: "))
while True:
    if 5 <= rowlength <= 15:
        break        
    else:
        print("\nerror: Given row r, 5 ≤ r.length ≤ 15\nenter again\n")
        rowlength = int(input("enter the length of the row: "))
        

while rowlength > 0:
    x=int(input("enter the height(<200) or -1 if its a tree:"))
    if x >200:
        print("\nerror: maximum heigth is 200\nenter again\n")
        continue
    row.append(x)
    rowlength -=1
print(row)

sorted = []
between = []

for i in row:
    if i != -1:
        between.append(i)
between.sort()
iter = 0
for i in row:
    if i != -1:
        sorted.append(between[iter])
        iter += 1
    else:
        sorted.append(-1)
print(sorted)
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

'''
Q3. Sort Without Moving
    Some people are standing in a row in a park. There are trees between them whichcannot be moved.
     Your task is to rearrange the people by their heights in a nondescending order without moving the trees.

constraints:
    ● Given row r, 5 ≤ r.length ≤ 15,
    ● maximum height of the people could be 200.
    ● Height of the tree is denoted as -1
    ● [output] Sorted row with all the trees untouched.

Example
For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190]

Test Case 1:
    input: [-1, 3, 4, -1, 1]
    output: [-1, 1, 3, -1, 4]

Test Case 2:
    input: [-1, -1, -1, -1, -1]
    output: [-1, -1, -1, -1, -1]

Test Case 3:
    input: [10, 9, 8, -1, 4, 3, -1, 7, 6, -1, -1, 2, 1, -1, 0]
    output: [0, 1, 2, -1, 3, 4, -1, 6, 7, -1, -1, 8, 9, -1, 10]

'''
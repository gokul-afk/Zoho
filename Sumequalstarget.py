n=int(input("No. of integers = "))
numbers=[]
while n > 0:
    x=int(input("interger: "))
    if not(1 <= x <= 100):
        print("\nerror: Enter integer between 1 and 100\nenter again\n")
        continue
    n-=1
    numbers.append(x)
print("Numbers =", numbers)
target = int(input("Target Sum = "))

flag = 1

for i in range(0, len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] + numbers[j] == target):
            print("Possible")
            flag = 0
            break
    if flag == 0:
        break    
if flag :
    print("Not Possible")

'''


Given an array of integers and a target value, determine if there are any two integers in the array
whose sum is equal to the given target value. Return true if the sum exists and return false if it does
not.

Constraint:     1<=integers<=100

Input:
    No. of integers = 4
    Numbers = [2, 7, 11, 15]
    Target Sum = 9,
Output:
    Possible


Input:
    No. of integers = 5
    Numbers = [2,4,5,7,8]
    Target Sum = 11,
Output:
    Possible


Input:
    No. of integers = 5
    Numbers = [2,8,5,7,18]
    Target Sum = 3,
Output:
    Not Possible


Input:
    No. of integers = 2
    Numbers = [2,7]
    Target Sum = 9,
Output:
    Possible


Input:
    No. of integers = 7
    Numbers = [1, 6, 5, 2, 4, 3, 7]
    Target Sum = 7
Output:
    Possible
'''
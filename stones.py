stones = [75,89]
print(stones)
while len(stones) > 1:
    stones.sort()
    if stones[-1] == stones[-2]:
        stones.pop(-1)
        stones.pop(-1)
    else:
        stones[-1]-=stones[-2]
        stones.pop(-2)
if not stones:
    print(0)        
else:
    print(stones[0])

'''
You are given an array of integers stones where stones[i] is the weight of the ith stone.
We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash
them together. Suppose the heaviest two stones have weights x and y with x <= y.
The result of this smash is:
●If x == y, both stones are destroyed, and
●If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y -
x.
At the end of the game, there is at most one stone left.
Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Test Case 1:
    input: [80,117,45,100,89,91]
    output: 16

Test Case 2:
    input: [8,8,5,5,4,4]
    output: 0

Test Case 3:
    input: [8,8,5,5,4]
    output: 0

Test Case 4:
    input: []
    output: 0

Test Case 5:
    input: [5,87,90,78,90,75,89]
    output: 0

Test Case 6:
    input: [51]
    output: 51

Test Case 7:
    input: [75,89]
    output: 14
'''
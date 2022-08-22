stones = []
n = int(input("enter the number of stones: "))
for i in range(n):
    stones.append(int(input()))
print(stones)
while len(stones) > 1:
    stones.sort()
    if stones[-1] == stones[-2]:
        stones.pop(-1)
        stones.pop(-1)
    else:
        stones[-1]-=stones[-2]
        stones.pop(-2)
if len(stones) == 0:
    print(0)        
else:
    print(stones[0])
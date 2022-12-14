
def isValid(maze, x, y, res):
    
    if x >= 0 and y >= 0 and x < m and y < n and maze[x][y] == 1 and res[x][y] == 0:
        return True
    return False
 
def RatMaze(maze, move_x, move_y, x, y, res):
    global count
    if x == m-1 and y == n-1:
        count += 1
        return True
    for i in range(8):
        

        x_new = x + move_x[i]

        y_new = y + move_y[i]

        if isValid( maze, x_new, y_new, res):
 

            res[x_new][y_new] = 1
            count += 1
            if RatMaze(maze, move_x, move_y, x_new, y_new, res):
                return True
            res[x_new][y_new] = 0
            count -= 1
    return False
 
def solveMaze(maze):

    res = [[0 for i in range(m)] for j in range(n)]
    res[0][0] = 1
    move_x = [1,0,1,-1,1,0,-1,-1]
    move_y = [1,1,0,1,-1,-1,0,-1]  
 
    if RatMaze(maze, move_x, move_y, 0, 0, res):
        for i in range(m):
            for j in range(n):
                print(res[i][j], end=' ')
            print()
    else:
        print('Solution does  not exist')
 
 
count=0
maze = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 1 ],
[1, 1, 0, 0, 1, 1, 0, 1, 0, 1 ],
[0, 0, 0, 0, 1, 0, 1, 0, 0, 1 ],
[1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
[1, 0, 1, 1, 1, 1, 0, 0, 0, 1 ],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
[1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]
]

m= len(maze)
n= len(maze[0]) 
solveMaze(maze)

print(count)


'''
OUTPUT
1 0 0 1 0 0 0 0 0 0 
1 0 1 0 1 0 0 0 1 0
0 1 0 0 0 1 0 1 0 1
0 0 0 0 0 0 1 0 0 1
0 0 0 0 0 0 0 0 1 0 
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 0 1 
0 0 0 0 0 0 0 0 0 1
18


[[1, 0, 0, 1, 1, 1, 1, 0, 0 ],
[1, 0, 1, 0, 0, 0, 0, 1, 0 ],
[1, 0, 1, 0, 0, 0, 0, 1, 0 ],
[1, 0, 1, 0, 0, 1, 0, 0, 1 ],
[1, 0, 1, 0, 1, 0, 1, 0, 1 ],
[1, 0, 0, 1, 0, 0, 1, 0, 1 ],
[1, 0, 0, 0, 0, 1, 0, 0, 1 ],
[0, 1, 1, 1, 1, 0, 0, 1, 0 ],
[0, 0, 0, 0, 0, 0, 0, 0, 1 ]]
33

[1, 0, 1, 1, 0, 1, 1, 0, 0 ],
[1, 0, 1, 1, 1, 0, 0, 1, 0 ],
[1, 0, 1, 0, 0, 0, 0, 1, 0 ],
[1, 1, 1, 0, 0, 1, 0, 0, 1 ],
[1, 0, 1, 0, 1, 0, 1, 0, 1 ],
[1, 0, 0, 1, 0, 1, 1, 1, 1 ],
[1, 0, 0, 0, 0, 1, 0, 0, 1 ],
[0, 1, 1, 1, 1, 0, 0, 1, 0 ],
[0, 0, 0, 0, 0, 0, 0, 0, 1 ]
13

[1,0,0,1],
[1,1,0,1],
[1,0,1,1],
[1,0,0,1]
4
'''
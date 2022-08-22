
mat = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 1 ],
[1, 1, 0, 0, 1, 1, 0, 1, 0, 1 ],
[0, 0, 0, 0, 1, 0, 1, 0, 0, 1 ],
[1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
[1, 0, 1, 1, 1, 1, 0, 0, 0, 1 ],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
[1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]


row = len(mat)
col = len(mat[0])

print(row,col)

'''
Q5. Where's the carrot?
'Kittu' (name) rabbit needs help in finding shortest path to the carrot.
Given a MxN matrix where each element can either be 0 or 1. We need to find the
shortest path between Kittu’s pos(0,0) to Carrot’s pos(M,N). The path can only be
created out of a cell if its value is 1.
Input:
 [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
[1, 0, 1, 0, 1, 0, 1, 0, 1, 1 ],
[1, 1, 0, 0, 1, 1, 0, 1, 0, 1 ],
[0, 0, 0, 0, 1, 0, 1, 0, 0, 1 ],
[1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
[1, 0, 1, 1, 1, 1, 0, 0, 0, 1 ],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
[1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
[1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]
Output:
Shortest Path is 18
Input :
 [[1, 0, 0, 1, 1, 1, 1, 0, 0 ],
[1, 0, 1, 0, 0, 0, 0, 1, 0 ],
[1, 0, 1, 0, 0, 0, 0, 1, 0 ],
[1, 0, 1, 0, 0, 1, 0, 0, 1 ],
[1, 0, 1, 0, 1, 0, 1, 0, 1 ],
[1, 0, 0, 1, 0, 0, 1, 0, 1 ],
[1, 0, 0, 0, 0, 1, 0, 0, 1 ],
[0, 1, 1, 1, 1, 0, 0, 1, 0 ],
[0, 0, 0, 0, 0, 0, 0, 0, 1 ]]
Output :
Shortest Path is 33

'''
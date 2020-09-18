# Maze Solver - Using Breadth First Search (BFS)/ Depth First Search (DFS) Approach:

# Input :    # Expected Output :

# 1 0 0 0      # 1 0 0 0
# 1 1 0 1      # 1 1 0 0 
# 0 1 0 0      # 0 1 0 0
# 1 1 1 1      # 0 1 1 1


# Function for Output Solution according to the given User Input
def solvedPath(Traversed):
    print("Your Path(Output) : ")

    for i in Traversed:
        for j in i:
            print(str(j) + " ", end="")
        print("")

# if not a valid position, return false
def explorePath(Column, Row):
    Traversed = [[0 for i in range(Row)] for i in range(Row)]

    if mazeTraversal(Column, 0, 0, Traversed, Row):
        solvedPath(Traversed)
    else:
        print("Path does not exist")

# Check if it is possible to go to (x, y) from current position. The
# function returns false if the cell has value 0 or already visited
def attestedPaths(Column, x, y, Traversed, Row):
    if x >= 0 and x < Row and y >= 0 and y < Row and Column[x][y] == 1:
        return True
    else:
        return False

# Find Shortest Possible Route in a Matrix mat from source cell (0, 0)
# to destination cell (x, y)
def mazeTraversal(Column, x, y, Traversed, Row):
    if x == Row-1 and y == Row-1:
        Traversed[x][y] = 1
        return True

    if attestedPaths(Column, x, y, Traversed, Row):
        Traversed[x][y] = 1
    
        if mazeTraversal(Column, x+1, y, Traversed, Row):
            return True
    
        if mazeTraversal(Column, x, y+1, Traversed, Row):
            return True


# Giving Dynamic User Input

if __name__ == "__main__":
    Column=[]

    Row=int(input("Number of rows :\n"))
    
    for i in range(Row):
        print("Enter row No. :",i+1)
        
        row=list(map(int,input().split()))
        
        Column.append(row)
    
    explorePath(Column, Row)
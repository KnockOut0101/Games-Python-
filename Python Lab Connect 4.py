
grid=[]

for i in range(6):
    row = [0,0,0,0,0,0,0]
    grid.append(row)


#creat_grid()
print(len(grid))

def grid_insert(symbol,column,grid=grid):
    for i in range(len(grid),-1,-1):
        if(grid[i][column]!=0):
            continue
        elif(grid[i][column==0]):
            grid[i][column]=symbol

def print_grid():
    for i in range(len(grid)):
        print(grid[i],"\n")

grid_insert('O',4)

print_grid()


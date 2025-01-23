from random import random
import time

# Helper function as was described in guide to create a 2D grid of all 0s
# Not using it so commented out, but kept in for future reference
def dead_state(width, height):
# Learnt an interesting thing about the below block of code
# When I do [row]*height, I am creating duplicate references to the same memory location
# So if I change one row, all rows get changed. SUPERRRRR!!
    '''row = [0]*width 
    return [row]*height'''
    return [[0 for _ in range(width)] for _ in range(height)]
    

def random_state(width, height):
# TODO: Type check if width and height are numerals

# This is one way to do it functionally, but sadly python has made it incredibly difficult
# to do this, since map returns a map object, and the statement itself is very confusing.
    '''state = dead_state(width, height)
    return list(map(lambda xs:list(map(lambda x:random.randint(0,1), xs)),state))'''

# When doing what the guide says - 
    ''' state = dead_state(width, height)
    for row in state:
        for i in range(len(row)):
            random_number = random()
            if random_number > 0.5:
                cell_state = 0
            else:
                cell_state = 1
            row[i] = cell_state'''
# This method is obviously way less efficient, as it creates an intermediate step in the process of 
# creating the grid. So imma do my own thing.

# Custom randomizer function, which always returns a 0 or 1 depending on the probability
# distribution set by the user. 
# I want to mess with probabilites, so I created a custom random function using the same logic as described in the guide. 
    def custRandom():
        return 1 if random() > 0.7 else 0 
# Here 1 represents alive and 0 represents dead
# My way is to completely ignore dead_state and use implement its functionality here
# Directly creating the 2D grid with my custom random function - 
    return [[custRandom() for _ in range(width)] for _ in range(height)]


def render(grid):
# For this function, I will be using # to represent live cells, and _ to represent dead cells. 
# This can be changed as per taste later. 

# Now this function might have some problems. The first line depends on the list being non-empty.
# TODO: Need to add this safety later. Also add type checking whether grid is a 2D list or not. 
    width = len(grid[0])
    
# The logic of the formula width*3+2 is that for every element I am printing, there are 3 chars being printed. 
# These characters are the state of cell and 2 spaces around it. 
# +2 is to account for the boundaries of the grid, the | char.     
    border = "-" * (width*3+2)
    print(border)
    for row in grid:
        print_row = " ".join(["_ " if cell == 0 else "# " for cell in row])
        print(f"| {print_row}|")
    print(border)

def next_board_state(board_state):
    height = len(board_state)
    width = len(board_state[0])
    new_state = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            status = board_state[i][j]
            sum = 0
            if 0<i<(height-1) and 0<j<(width-1):
                sum+=board_state[i-1][j-1]+board_state[i-1][j]+board_state[i-1][j+1]
                sum+=board_state[i][j-1]+board_state[i][j+1]
                sum+=board_state[i+1][j-1]+board_state[i+1][j]+board_state[i+1][j+1]
            elif i==0 and j==0:
                sum+=board_state[0][1]+board_state[1][0]+board_state[1][1]
            elif i==0 and j==width-1:
                sum+=board_state[0][width-2]+board_state[1][width-1]+board_state[1][width-2]
            elif i==height-1 and j==0:
                sum+=board_state[height-1][1]+board_state[height-2][0]+board_state[height-2][1]
            elif i==height-1 and j==width-1:
                sum+=board_state[height-1][width-2]+board_state[height-2][width-1]+board_state[height-2][width-2]
            elif i==0:
                sum+=board_state[0][j-1]+board_state[0][j+1]
                sum+=board_state[1][j-1]+board_state[1][j]+board_state[1][j+1]
            elif i==height-1:
                sum+=board_state[height-1][j-1]+board_state[height-1][j+1]
                sum+=board_state[height-2][j-1]+board_state[height-2][j]+board_state[height-2][j+1]
            elif j==0:
                sum+=board_state[i-1][0]+board_state[i+1][0]
                sum+=board_state[i-1][1]+board_state[i][1]+board_state[i+1][1]
            elif j==width-1:
                sum+=board_state[i-1][width-1]+board_state[i+1][width-1]
                sum+=board_state[i-1][width-2]+board_state[i][width-2]+board_state[i+1][width-2]
                
            if status==1:
                if 2<=sum<=3:
                    new_state[i][j]=1
                else:
                    new_state[i][j]=0
            else:
                if sum==3:
                    new_state[i][j]=1
                else:
                    new_state[i][j]=0 
    return new_state


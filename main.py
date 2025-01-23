# This is the main file for this project 
# TODO: Create Conway's Game Of Life

# To watch the program in slow motion, uncomment lines 7 and 29

from board import random_state, render, next_board_state
#import time

# Cell pattern for bye
bye_state = [
    [1,1,0,0,1,0,0,1,0,1,1,1],
    [1,0,1,0,1,0,0,1,0,1,0,0],
    [1,0,1,0,1,0,0,1,0,1,0,0],
    [1,1,0,0,0,1,1,1,0,1,1,0],
    [1,0,1,0,0,0,0,1,0,1,0,0],
    [1,0,1,0,0,0,0,1,0,1,0,0],
    [1,1,0,0,1,1,1,1,0,1,1,1],
]

width = int(input("What is the width of the grid: "))
height = int(input("What is the height of the grid: "))
board_state = random_state(width, height) 
#board_state = bye_state
render(board_state)

while True:
    board_state = next_board_state(board_state)
    render(board_state)
#    time.sleep(1) 
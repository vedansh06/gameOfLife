﻿# gameOfLife

Game of Life, also called Life, is a simple mathematical simulation game that takes place on a 2D grid. It is a cellular automaton, meaning that the states of cells on the grid keep changing automatically with respect to its 8 surrounding cells (neighbours) by following some rules - 

1.	Any live cell with 0 or 1 live neighbours becomes dead, because of underpopulation
2.	Any live cell with 2 or 3 live neighbours stays alive, because its neighbourhood is just right
3.	Any live cell with more than 3 live neighbours becomes dead, because of overpopulation
4.	Any dead cell with exactly 3 live neighbours becomes alive, by reproduction.

It is zero-player game, meaning that no input is required from the player. The game depends on the initial position of the live cells on the grid, the zero generation. Then the above rules are applied to all the cells in the zero generation, to bring forth the first generation. 

This project provides a simple implementation of running some random zero generations through a Game of Life simulator.

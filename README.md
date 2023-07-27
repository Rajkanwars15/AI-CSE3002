# AI-CSE3002
![image](https://github.com/Rajkanwars15/AI-CSE3002/assets/89787756/72dc1a2f-f06c-4719-899c-98900f7f0687)

## Lab Record

## [Tic Tac Toe Problem](tictactoe.py)
**1 June 2023**
> Write a program to solve Tic-Tac-toe problem

> Rules of the Game
 The game is to be played between two people (in this program between HUMAN and COMPUTER). • One of the player chooses ‘O’ and the other ‘X’to mark their respective cells. • The game starts with one of the players and the game ends when one of the players has one whole row/ column/ diagonal filled with his/her respective character (‘O’or ‘X’). • If no one wins, then the game is said to be draw

![image](https://github.com/Rajkanwars15/AI-CSE3002/assets/89787756/27ea1be3-c1d5-444d-b41a-0a0f75f17476)


### Complexities
| function          | Time             | Space |
|-------------------|------------------| ----- |
| print_board()     | O(n)             | O(n) |
| take_turn()       | O(n)             | O(n) |
| check_game_over() | O(n)             | O(n) |
| play_game()       | O(n<sup>2</sup>) | O(n) |

## [BFS & DFS](bfsdfs.py)
**8 June 2023**
> Compare Breadth First Search and Depth First Search for the given set of elements.

### Complexities
| function | Time     | Space |
|----------|----------|-------|
| BFS      | O(V + E) | O(V)  |
| DFS      | O(V + E) | O(V)  |

## [Water Jug](waterjug.py)
**15 June 2023**
> Write a program to solve production system(Water Jug) problem

![image](https://github.com/Rajkanwars15/AI-CSE3002/assets/89787756/7b234965-3ec1-4254-9d6f-b7653cea1de6)


### Complexities
| function         | Time         | Space |
|------------------|--------------|-------|
| waterJugSolver() | O(jug1*jug2) | O(jug1*jug2)  |
To explore and store all possible states (jug1 + 1) x (jug2 + 1) iterations.

## [N-Queens](nqueen.py)
**22 June 2023**
> Write a program to solve 8-Queens problem with reduced number of moves

![image](https://github.com/Rajkanwars15/AI-CSE3002/assets/89787756/38411398-9aa1-46ef-9650-6972753dd050)


### Complexities
| function         | Time  | Space |
|------------------|-------|-------|
| n_queens() | O(N!) | O(N)  |

## [Magic Square](magicSquare.py)
**13 July 2023**
> Write a program to solve Tic-Tac-toe problem, implement as User versus Computer. Tic-Tac-toe

> A magic square of order n is an arrangement of n^2 numbers, usually distinct integers, in a square, such that the n numbers in all rows, all columns, and both diagonals sum to the same constant. A magic square contains the integers from1 to n^2.
The constant sum in every row, column and diagonal is called the magic constant ormagic sum, M. The magic constant of a normal magic square depends only on n and has the following value:
M = n(n^2+1)/2
For normal magic squares of order n = 3, 4, 5, ...,
the magic constants are: 15, 34, 65, 111, 175, 260, ...

![image-removebg-preview](https://github.com/Rajkanwars15/AI-CSE3002/assets/89787756/22691cef-6e76-4ceb-a835-75f6f635eb83)

### Complexities
| function        | Time             | Space |
|-----------------|------------------| ----- |
| print_board()   | O(n)             | O(n) |
| take_turn()     | O(n)             | O(n) |
| heck_game_over() | O(n)             | O(n) |
| play_game()     | O(n<sup>2</sup>) | O(n) |

## [Map Coloring](mapColoring.py)
**20 July 2023**
> Implement constraint satisfaction through map colouring problem.

![](/Users/raj/Downloads/colorful.png)

### Complexities
| function            | Time             | Space |
|---------------------|------------------|-------|
| is_valid_assignment() | O(m)             | O(1)  |
| map_coloring()      | O(m<sup>n</sup>) | O(n)  |
| overall             | O(m<sup>n</sup>) | O(n)  |
m -> average number of neighboring regions for each node </br>
n -> number of regions
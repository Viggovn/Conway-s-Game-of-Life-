import random
import time

#board size and variables
UserInputSizeGridX = int(input("How Big do you want the X axis to be? "))
UserInputSizeGridY = int(input("How Big do you want the Y axis to be? "))
TotalCells = UserInputSizeGridX * UserInputSizeGridY

Board = []
TempBoard = []

#amount of time the board will refresh
generation = 0

#function
def AmountOfAliveNeighbours(Board, CurrentIndex):
    y = CurrentIndex // UserInputSizeGridX
    x = CurrentIndex % UserInputSizeGridX
    neighbours = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            ny = y + dy
            nx = x + dx
            if 0 <= ny < UserInputSizeGridY and 0 <= nx < UserInputSizeGridX:
                index = ny * UserInputSizeGridX + nx
                if Board[index] == 1:
                    neighbours += 1
    return neighbours

#creating the board
for i in range(TotalCells):
    Board.append(0)

for i in range(len(Board)):
    AliveOrDeath = random.randint(1, 10)
    if AliveOrDeath > 7:
        Board[i] = 1
    else:
        continue

#the main game loop
while generation < 50:
    for i, Cells in enumerate(Board, start=1):
        print(Cells, end=" ")
        if i % UserInputSizeGridX == 0:
            print()

    #Apllying the rules too the cells
    for i in range(len(Board)):
        AmountAlive = AmountOfAliveNeighbours(Board, i)
        if AmountAlive < 2 or AmountAlive > 3:
            TempBoard.append(0)
        elif Board[i] == 0 and AmountAlive == 3:
            TempBoard.append(1)
        else:
            TempBoard.append(1)
    
    Board = TempBoard
    TempBoard = []
    generation += 1

    print()
    print()
    time.sleep(2)

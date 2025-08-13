UserInputSizeGridX = int(input("How Big do you want the X axis to be? "))
UserInputSizeGridY = int(input("How Big do you want the Y axis to be? "))
TotalCells = UserInputSizeGridX * UserInputSizeGridY

Board = []

for i in range(TotalCells):
    Board.append(0)
    
for i, Cells in enumerate(Board, start=1):
    print(Cells, end=" ")
    if i % UserInputSizeGridX == 0:
        print()

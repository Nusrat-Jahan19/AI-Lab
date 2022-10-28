
def hCol(pos): 
 for i in range(len(pos)):
    countHorizontal(i, pos) 
 
def duCol(pos):
 for i in range(len(pos)):
  countDiagonalUp(i, pos) 
def ddCol(pos):
 for i in range(len(pos)):
  countDiagonalDown(i, pos)
 
def countHorizontal(point, pos):
 global count
 for i in range(point + 1, len(pos)):
  if pos[i] == pos[point]:
   count += 1
 
def countDiagonalUp(point, pos):
 global count
 for i in range(point + 1, len(pos)):
  if pos[i] == pos[point] + i - point:
   count += 1 
 
def countDiagonalDown(point, pos):
 global count
 for i in range(point + 1, len(pos)):
  if pos[i] == pos[point] - i + point:
   count += 1

count = 0
pos = [0]*8
for i in range(8):
 pos[i] = int(input('Enter Position for Queen in Column ' + str(i+1) + ': '))

hCol(pos)
duCol(pos)
ddCol(pos) 
print('Total Number of Collisions: ', count)
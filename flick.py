
def printarray(array):
    n = range(len(array))
    for y in n:
        for x in n:
            print (array[x][y],end='\t')
        print()

def fill(n):
    x1,y1 = 1,0
    x,y = 0,0
    array = [[0] * n for j in range(n)]
    for i in range(1,n**2+1) :
        array[x][y] = i
        x2,y2 = x+x1, y+y1
        if 0 <= x2 < n and 0 <= y2 < n and array[x2][y2] == 0 :
            x,y = x2,y2
        else:
            x1,y1 = -y1,x1
            x,y = x+x1, y+y1
    return array

while True:
    n = int(input())
    if n == 0:
        break
    printarray(fill(n))

fr = open("input.gol", "r")

def create2DMatrix(width, height):
    matrix = []
    temp = []
    for i in range(height):
        for x in range(width):
            temp.append(0)
        matrix.append(temp)
        temp = []
    return matrix

def processfile(matrix):
    x = 0
    y = 0
    for row in fr:
        x = 0
        for char in row:
            if char == "1":
                matrix[y][x]=1
            x += 1
        y += 1

def returnFriends(x,y,matrix):
    #sedlacina
    #pocet = 0
    #if x < width - 1 and matrix[y][x+1]==1:
       # pocet += 1
    #if x < width - 1 and y < height - 1 and matrix[y+1][x+1]==1:
        #pocet += 1
   # if y < height - 1 and matrix[y+1][x]==1:
       # pocet += 1
   # if x > 0 and y < height - 1 and matrix[y+1][x-1]==1:
        #pocet += 1
    #if x > 0 and matrix[y][x-1]==1:
     #   pocet += 1
    #if x > 0 and y > 0 and matrix[y-1][x-1]==1:
     #   pocet += 1
    #if y > 0 and matrix[y-1][x]==1:
     #   pocet += 1
    #if x < width - 1 and y > 0 and matrix[y-1][x+1]==1:
     #   pocet += 1
    #return pocet
    count = 0
    #navrhnme seriu ifov aby to fungovalo 8ifov
    if y>0 and x>0 and matrix[y-1][x-1]:
        count +=1
    if y>0 and matrix[y-1][x]:
        count+=1
    if y>0 and x<(width-1) and ma[x+1]:
        count +=1
    if x>1 and matrix[y][x-1]:
        count +=1
    if x<(width-1) and matrix[y][x+1]:
        count +=1
    if y<(height-1) and x>0 and matrix[y+1][x-1]:
        count +=1
    if y<(height-1) and matrix[y+1][x]:
        count +=1
    if y<(height-1) and x<(width-1) and matrix[y+1][x+1]:
        count +=1
    print(count)
    return(count)

def rewrite(oldfield, newfield):
    pass
    for i in

width, height = fr.readline().split(" ")
width = int(width)
height = int(height)
oldfield = create2DMatrix(width, height)
newfield = create2DMatrix(width, height)
create2DMatrix(width,height)
processfile(oldfield)
returnFriends(1,0,oldfield)



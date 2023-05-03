import tkinter as tk
win= tk.Tk()
WIDTH = 600
HEIGHT = 600
cellist=[]

canvas= tk.Canvas(width=WIDTH,height=HEIGHT,bg="white")
canvas.pack()


fr = open("input.gol", "r")

def drawgrid(ws=30):
    count = HEIGHT // ws
    for i in range(count):
        canvas.create_line(0,i*ws,WIDTH,i*ws)
    count= WIDTH //ws
    for i in range(count):
        canvas.create_line(i*ws,0,i*ws,HEIGHT)

def drawcells(oldfield,cellist,ws):
    canvas.delete("all")
    drawgrid()
    #for item in cellist:
        #canvas.delete(item)
    #canvas.update()
    #cellist = []
    for y in range(height):
        for x in range(width):
            if oldfield[y][x]==1:
                cellist.append(canvas.create_oval(x*ws,y*ws,(x+1)*ws,(y+1)*ws,fill="green"))


def create2DMatrix(width, height):
    matrix = []
    temp = []
    for y in range(height):
        temp=[]
        for x in range(width):
            temp.append(0)
        matrix.append(temp)
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
    if y>0 and x<(width-1) and matrix[y-1][x+1]:
        count +=1
    if x>0 and matrix[y][x-1]:
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
    for x in range(width):
        for y in range(height):
            if oldfield[y][x] == 1:
                friends = returnFriends(x,y,oldfield)
                if friends == 2 or friends == 3:
                    newfield[y][x] = 1
                elif friends < 2:
                    newfield[y][x] = 0
                elif friends > 3:
                    newfield[y][x] = 0
            elif oldfield[y][x] == 0:
                friends = returnFriends(x, y, oldfield)
                if friends == 3:
                    newfield[y][x] = 1


width, height = fr.readline().split(" ")
width = int(width)
height = int(height)
oldfield = create2DMatrix(width, height)
newfield = create2DMatrix(width, height)
processfile(oldfield)
drawgrid()


def generations():
    global oldfield,newfield
    # print stary matrix
    print(oldfield)
    drawcells(oldfield,cellist,30)
    # vypocitaj novy matrix (process file)
    rewrite(oldfield,newfield)
    # novy hodis do stareho - pomocou dvoch cyklov
    for y in range(height):
        for x in range(width):
            oldfield[y][x]=newfield[y][x]
    # novy musis vynulovat
    newfield = create2DMatrix(width,height)
    canvas.after(100,generations)

generations()
win.mainloop()


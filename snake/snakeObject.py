class Snake:

    def __init__(self, pos, width, height):
        self.pos = pos
        self.width = width
        self.height = height
        self.body = []
    
    def grow(self, direction, winX, winY): #0 - Up, 1 - Down, 2 - Left, 3 - Right
        currentX = self.pos[0]
        currentY = self.pos[1]

        if self.body:
            length = len(self.body)
            tail = self.body[length - 1]
            currentX, currentY  = tail[0], tail[1]

        bodyX, bodyY = 0, 0 #start

        if direction == 0: # go up
            bodyX = currentX
            bodyY = currentY + self.height

        if direction == 1: #go down
            bodyX = currentX
            bodyY = currentY - self.height

        if direction == 2: #go left
            bodyX = currentX + self.width
            bodyY = currentY
        
        if direction == 3: #go right
            bodyX = currentX - self.width
            bodyY = currentY
        
        self.body.append([bodyX % winX, bodyY % winY]) #append position tupels

    def updatePos(self, x, y):
        Idx = len(self.body) - 1
        while Idx >= 1:
            self.body[Idx] = self.body[Idx - 1]
            Idx -= 1
        if self.body:
            self.body[0] = self.pos
        self.pos = [x, y]\

    def getLength(self):
        return len(self.body) + 1
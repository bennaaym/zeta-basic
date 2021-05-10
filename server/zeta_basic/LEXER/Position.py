class Position:

    def __init__(self,index,line,col):
        self.index = index
        self.line = line
        self.col = col

    def next(self,currentChar):
        self.index += 1 
        self.col +=1

        if currentChar == '\n':
            self.line += 1
            self.col = 0

    def copy(self):
        return Position(self.index,self.line,self.col)

    def __str__(self):
        return str(self.line)+" "+str(self.col)
class SymbolTable:
    
    def __init__(self):
        self.symbolTable = {}
        self.parent = None

    def get(self,varName):
        value = self.symbolTable.get(varName,None)
        
        if value == None and self.parent:
            return self.parent.get(varName)

        return value 
        
    def set(self,varName,value):
        self.symbolTable[varName] = value


    def remove(self,varName):
        del self.symbolTable[varName]

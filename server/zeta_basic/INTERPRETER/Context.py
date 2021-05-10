

class Context:

    def __init__(self,name,parent=None,parentEntryPosition=None,symbolTable=None):
        self.name = name
        self.parent = parent
        self.parentEntryPosition = parentEntryPosition
        self.symbolTable = symbolTable
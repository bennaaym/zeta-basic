
from zeta_basic.ERRORS.Error import RunTimeError

class DataType:

    def __init__(self,value,position,context):
        self.value = value
        self.context = context
        if  position: self.position = position.copy()

    def __str__(self):
        return str(self.value)
    
    def __add__(self,other):
        return None, self.illegalOperandType('+',other=other)

    def __sub__(self,other):
        return None, self.illegalOperandType('-',other=other)


    def __mul__(self,other):
        return None, self.illegalOperandType('*',other=other)


    def __truediv__(self,other):
        return None, self.illegalOperandType('/',other=other)

    def __pow__(self,other):
        return None, self.illegalOperandType('**',other=other)

    def __mod__(self,other):
        return None, self.illegalOperandType('%',other=other)

    def __floordiv__(self,other):
        return None, self.illegalOperandType('//',other=other)

    
    def __eq__(self, other):
        return None, self.illegalOperandType('==',other=other)

    def __ne__(self, other):
        return None, self.illegalOperandType('!=',other=other)

    def __lt__(self, other):
        return None, self.illegalOperandType('<',other=other)

    def __gt__(self, other):
        return None, self.illegalOperandType('>',other=other)

    def __le__(self, other):
        return None, self.illegalOperandType('<=',other=other)

    def __ge__(self, other):
        return None, self.illegalOperandType('>=',other=other)

   
    def _and(self,other):
        return None, self.illegalOperandType('&&',other=other)

    def _or(self,other):
        return None, self.illegalOperandType('||',other=other)

    def _not(self):
        return None, self.illegalOperandType('!')

    def isTrue(self):
        return False

    def toString(self):
        return str(self.value)

    def illegalOperandType(self,operation,other =None):
        if not other : other = self
        return RunTimeError(f'unsupported operand type(s) for {operation} : {type(self).__name__}, {type(other).__name__}', self.position, self.context)
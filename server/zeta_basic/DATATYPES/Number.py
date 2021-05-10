from zeta_basic.ERRORS.Error import RunTimeError
from .DataType import DataType
from .Bool import Bool

class Number(DataType):

    def __init__(self,value,position,context):
        super().__init__(value,position,context)

    
    def __add__(self,other):
        if isinstance(other, Number):
            return Number(self.value + other.value,self.position,self.context),None
        
        return None, DataType.illegalOperandType(self, '+',other)

    def __sub__(self,other):
        if isinstance(other, Number):
            return Number(self.value - other.value,self.position,self.context),None

        return None, DataType.illegalOperandType(self, '-',other)


    def __mul__(self,other):
        if isinstance(other, Number):
            return Number(self.value * other.value,self.position,self.context),None

        return None, DataType.illegalOperandType(self, '*',other)


    def __truediv__(self,other):
        if isinstance(other, Number):
            if other.value == 0:
                return None , RunTimeError('Division by zero', self.position,self.context)
                
            return Number(self.value / other.value,self.position,self.context) , None

        return None, DataType.illegalOperandType(self, '/',other)


    def __pow__(self,other):
        if isinstance(other, Number):
            if self.value == 0 and other.value ==0:
                return None,  RunTimeError('Zero to the power of zero', self.position,self.context)
            return Number(self.value ** other.value,self.position,self.context) , None

        return None, DataType.illegalOperandType(self, '*',other)



    def __mod__(self,other):
        if isinstance(other, Number):
            if other.value ==0:
                return None,  RunTimeError('Modulo zero', self.position,self.context)
            return Number(self.value % other.value,self.position,self.context) , None

        return None, DataType.illegalOperandType(self, '%',other)


    def __floordiv__(self,other):
        if isinstance(other, Number):
            if other.value == 0:
                return None , RunTimeError('Division by zero', self.position,self.context)
                
            return Number(self.value // other.value,self.position,self.context) , None

        return None, DataType.illegalOperandType(self, '//',other)


    
    def __eq__(self, other):
        if isinstance(other, Number):
            return Bool(str(self.value == other.value).upper(),self.position,self.context) , None
        elif isinstance(other, Bool):
            return Bool(str(self.isTrue() == other.isTrue()).upper(),self.position,self.context),None

        return Bool('FALSE', self.position, self.context), None
    
    def __ne__(self, other):
        if isinstance(other, Number):
            return Number(str(self.value != other.value).upper(),self.position,self.context) , None
        elif isinstance(other, Bool):
            return Bool(str(self.isTrue() != other.isTrue()).upper(),self.position,self.context),None

        return Bool('FALSE', self.position, self.context), None


    def __lt__(self, other):
        if isinstance(other, Number):
            return Bool(str(self.value < other.value).upper(),self.position,self.context) , None

        return None, DataType.illegalOperandType(self, '<',other)


    def __gt__(self, other):
        if isinstance(other, Number):
            return Bool(str(self.value > other.value).upper(),self.position,self.context) , None

        return None, DataType.illegalOperandType(self, '>',other)


    def __le__(self, other):
        if isinstance(other, Number):
            return Bool(str(self.value <= other.value).upper(),self.position,self.context) , None

        return None, DataType.illegalOperandType(self, '<=',other)


    def __ge__(self, other):
        if isinstance(other, Number):
            return Bool(str(self.value >= other.value).upper(),self.position,self.context) , None

        return None, DataType.illegalOperandType(self, '>=',other)


    def _and(self,other):
        if isinstance(other, Number):
            return Number(int(bool(self.value) and bool(other.value)),self.position,self.context) , None

        return None, DataType.illegalOperandType(self, '&&',other)


    def _and(self,other):
        return Bool(str(self.isTrue() and other.isTrue()).upper(),self.position,self.context),None

    def _or(self,other):
        return Bool(str(self.isTrue() or other.isTrue()).upper(),self.position,self.context),None

    def _not(self):
        return Bool(str(self.value).upper(),self.position,self.context),None


    def isTrue(self):
        return self.value !=0


Number.null = Number(0,None,None)
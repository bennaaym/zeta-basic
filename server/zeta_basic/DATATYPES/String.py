
from zeta_basic.ERRORS.Error import RunTimeError
from .DataType import DataType
from .Number import Number
from .Bool import Bool

class String(DataType):

    def __init__(self,value,position,context):
        super().__init__(value,position,context)


    def isTrue(self):
        return len(self.value) > 0


    def __add__(self,other):
        if isinstance(other, String):
            return String(self.value + other.value, self.position, self.context), None

        return None, DataType.illegalOperandType(self, '+',other)

    def __mul__(self, other):
        if isinstance(other, Number):
            return String(self.value * other.value, self.position, self.context), None
        
        return None, DataType.illegalOperandType(self, '*',other)
        

    def __eq__(self,other):
        if isinstance(other, String):
            return Bool(str(self.value == other.value).upper(),self.position,self.context),None
        elif isinstance(other, Bool):
            return Bool(str(self.isTrue() == other.isTrue()).upper(),self.position,self.context),None

        return  Bool('FALSE',self.position,self.context),None

    def __ne__(self,other):
        if isinstance(other, String):
            return Bool(str(self.value != other.value).upper(),self.position,self.context),None
        elif isinstance(other, Bool):
            return Bool(str(self.isTrue() == other.isTrue()).upper(),self.position,self.context),None
            
        return  Bool('FALSE',self.position,self.context),None


    def __lt__(self,other):
        if isinstance(other, String):
            return Bool(str(self.value < other.value).upper(),self.position,self.context),None
        return  None,DataType.illegalOperandType(self, '<')
    
    def __gt__(self,other):
        if isinstance(other, String):
            return Bool(str(self.value > other.value).upper(),self.position,self.context),None
        return  None,DataType.illegalOperandType(self, '>')

    def __le__(self,other):
        if isinstance(other, String):
            return Bool(int(self.value <= other.value),self.position,self.context),None
        return  None,DataType.illegalOperandType(self, '<=')

    def __ge__(self,other):
        if isinstance(other, String):
            return Bool(int(self.value >= other.value),self.position,self.context),None
        return  None,DataType.illegalOperandType(self, '>=')

    def _and(self,other):
        return Bool(str(self.isTrue() and other.isTrue()).upper(),self.position,self.context),None

    def _or(self,other):
        return Bool(str(self.isTrue() or other.isTrue()).upper(),self.position,self.context),None

    def _not(self):
        return Bool(str(self.value).upper(),self.position,self.context),None
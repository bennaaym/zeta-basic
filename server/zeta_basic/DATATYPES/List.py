from zeta_basic.ERRORS.Error import RunTimeError
from .DataType import DataType
from .Number import Number
from .Bool import Bool

class List(DataType):

    def __init__(self, value, position, context):
        super().__init__(value, position, context)
        self.isHomogeneous,self.hasNullValues = self.checkTypes()
        
    def __str__(self):        
        return f'[{",".join([str(x) for x in self.value])}]'

    def toString(self):
         return f'[{",".join([str(x) for x in self.value])}]'
         
    def checkTypes(self):
      
        isHomogeneous = True
        hasNullValues = False

        for x in self.value:
            if type(x).__name__ != 'Number':
                isHomogeneous = False
            if type(x).__name__  == 'Number' and x.value == 0:
                hasNullValues = True


        return isHomogeneous,hasNullValues
    
    def size(self):
        return len(self.value)

    def __add__(self,other):
        return self.binaryArithmeticOperation(other, '+', func = lambda x,y : x+y , func2 = lambda x : x + other.value)

    def __sub__(self,other):
        return self.binaryArithmeticOperation(other, '-', func = lambda x,y : x-y, func2 = lambda x : x - other.value )

    def __mul__(self,other):
        return self.binaryArithmeticOperation(other, '*', func = lambda x,y : x*y, func2 = lambda x : x * other.value )

    def __truediv__(self,other):
        return self.binaryArithmeticOperation(other, '/', func = lambda x,y : x/y, func2 = lambda x : x / other.value )

    def __floordiv__(self,other):
        return self.binaryArithmeticOperation(other, '//', func = lambda x,y : x//y, func2 = lambda x : x // other.value )

    def __eq__(self,other):
        if isinstance(other, List):
            if self.size() != other.size():
                return Bool('FALSE', self.position, self.context), None

            for x,y in zip(self.value,other.value):
                if x.value != y.value:
                    return   Bool('FALSE', self.position, self.context), None

            return Bool('TRUE', self.position, self.context), None
        elif isinstance(other, Bool):
            return Bool(str(self.isTrue() == other.isTrue()).upper(),self.position,self.context),None

        return Bool('FALSE', self.position, self.context), None

    def __ne__(self,other):
        if isinstance(other, List):
            if self.size() != other.size():
                return Bool('TRUE', self.position, self.context), None

            for x,y in zip(self.value,other.value):
                if x.value != y.value:
                    return Bool('TRUE', self.position, self.context), None
                    
            return Bool('FALSE', self.position, self.context), None
        
        elif isinstance(other, Bool):
            return Bool(str(self.isTrue() != other.isTrue()).upper(),self.position,self.context),None

        return Number('TRUE', self.position, self.context), None

    def binaryArithmeticOperation(self,other,operation,func,func2):
        if not self.isHomogeneous:
            return  self.nonNumericalTypesError(operation)

        if isinstance(other, List):
            if self.size() != other.size():
                return self.listsOfUnequalSizeError(operation)

            if (operation in ('%','/','//')) and other.hasNullValues:
                return self.divisionByZeroError()

            elements = list(map(func,
                                [x.value for x in self.value],
                                [y.value for y in other.value]))
                                                           

            return List(elements,self.position,self.context) , None
        
        elif isinstance(other, Number):
            
            if (operation in ('%','/','//')) and other.value == 0:
                return self.divisionByZeroError()

            elements = list(map(func2,[x.value for x in self.value]))
            return List(elements,self.position,self.context) , None

        return None,DataType.illegalOperandType(self, '+',other)
    
    def _and(self,other):
        return Bool(str(self.isTrue() and other.isTrue()).upper(),self.position,self.context),None

    def _or(self,other):
        return Bool(str(self.isTrue() or other.isTrue()).upper(),self.position,self.context),None

    def _not(self):
        return Bool(str(self.value).upper(),self.position,self.context),None
    

    def sum(self):
        if self.isHomogeneous:
            return Number(sum([x.value for x in self.value]),self.position,self.context),None
        return self.nonNumericalTypesError('SUM')

    def isTrue(self):
        return len(self.value) > 0
    

    def nonNumericalTypesError(self,operation):
        return None, RunTimeError(f'"{operation}" is not supported for Heterogeneous List or nonNumerical List dataype', self.position, self.context)

    def listsOfUnequalSizeError(self,operation):
        return None, RunTimeError(f'"{operation}" is unsupported for lists Of Unequal Size', self.position, self.context)

    def divisionByZeroError(self):
        return None, RunTimeError(f'Division by Zero', self.position, self.context)

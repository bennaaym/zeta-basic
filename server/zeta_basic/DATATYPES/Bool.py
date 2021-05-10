from zeta_basic.ERRORS.Error import RunTimeError
from .DataType import DataType


class Bool(DataType):

    def __init__(self, value, position, context):
        super().__init__(value, position, context)

    
    def __eq__(self, other):
        if isinstance(other, DataType):
            return Bool(str(self.isTrue()==other.isTrue()).upper(),self.position,self.context),None

    def __ne__(self,other):
        if isinstance(other, DataType):
            return Bool(str(self.isTrue()!=other.isTrue()).upper(),self.position,self.context),None


    def _and(self,other):
        if isinstance(other, DataType):
            return Bool(str(self.isTrue() and other.isTrue()).upper(),self.position,self.context),None

    def _or(self,other):
        if isinstance(other, DataType):
            return Bool(str(self.isTrue() or other.isTrue()).upper(),self.position,self.context),None

    def _not(self):
        if isinstance(other, DataType):
            return Bool(str(self.value).upper(),self.position,self.context),None
    

    def isTrue(self):
        return True if self.value == 'TRUE' else False




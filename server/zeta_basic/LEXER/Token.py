class Token :

    def __init__(self,type_,value = None,position=None):
        self.type = type_
        self.value = value
        if position: self.position = position.copy()

 
    def matches(self,type_,value):
        return self.type == type_ and self.value == value

    def __repr__(self):
        return f'{self.type} : {self.value}' if self.value else f'{self.type}'
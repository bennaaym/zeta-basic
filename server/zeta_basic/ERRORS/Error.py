class Error :

    def __init__(self,name,details,position):
        self.name = name
        self.details = details
        self.position = position

    
    def __str__(self):
        return f'Error : {self.name} -> {self.details} | line :{self.position.line} col : {self.position.col}'



class IllegalCharError(Error):

    def __init__(self,details,position):
        super().__init__('IllegalCharError',details,position)


class InvalidSyntaxError(Error):

    def __init__(self, details, position):
        super().__init__('InvalidSyntaxError', details, position)

    
class RunTimeError(Error):
    def __init__(self,  details, position,context):
        super().__init__('RunTimeError', details, position)
        self.context = context

    def __str__(self):
        return self.traceBack() + '\n' + f'Error : {self.name} -> {self.details} | line :{self.position.line} col : {self.position.col}'

    def traceBack(self):
        result = ''
        position = self.position
        context = self.context

        while context :
            result = f'line {position.line} in {context.name}' + result
            position = context.parentEntryPosition
            context = context.parent

        return result
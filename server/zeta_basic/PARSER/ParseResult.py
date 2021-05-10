
class ParseResult:

    def __init__(self):
        self.node = None
        self.error = None
        self.counter = 0
        self.reverseCount = 0

    def registerGetNext(self):
        self.counter +=1

    def register(self,res):
        self.counter += res.counter
        if res.error : self.error = res.error
        return res.node

    def tryRegister(self,res):
        if res.error: 
            self.reverseCount = self.counter
            return None
        return self.register(res)

    def success(self,node):
        self.node = node
        return self

    def failure(self,error):
        if  self.error == None or self.counter == 0 :
            self.error = error
        return self
from .AbstractSyntaxTreeNodes import *
from zeta_basic.LEXER.constants import *
from .ParseResult import ParseResult
from zeta_basic.ERRORS.Error import InvalidSyntaxError

class Parser:

    def __init__(self,tokens):
        self.tokens = tokens
        self.currentToken = None
        self.currentTokenIndex = -1
        self.getNextToken()


    def getNextToken(self):
        self.currentTokenIndex += 1
        self.updateCurrentToken()
        return self.currentToken
       

    def reverse(self,steps = 1):
        self.currentTokenIndex -= steps
        self.updateCurrentToken()
        return self.currentToken
    
    def updateCurrentToken(self):
        if self.currentTokenIndex >= 0 and self.currentTokenIndex < len(self.tokens):
            self.currentToken = self.tokens[self.currentTokenIndex]

    def parse(self):
        res = self.statement()
        if not res.error and self.currentToken.type != TT_EOF:
            return res.failure(InvalidSyntaxError('', self.currentToken.position))
        return res


    def atom(self):
        res = ParseResult()
        token = self.currentToken

        if token.type == TT_BOOL:
            res.registerGetNext()
            self.getNextToken()
            return res.success(BoolNode(token))
            
        elif token.type == TT_NUMBER:
            res.registerGetNext()
            self.getNextToken()
            return res.success(NumberNode(token))

        elif token.type == TT_STRING:
            res.registerGetNext()
            self.getNextToken()
            return res.success(StringNode(token))


        elif token.type == TT_IDENTIFIER:
            res.registerGetNext()
            self.getNextToken()
            return res.success(VarAccessNode(token))

        elif token.type == TT_LPAREN:
            res.registerGetNext()
            self.getNextToken()
            _expression = res.register(self.expression())

            if res.error : return res

            if self.currentToken.type == TT_RPAREN:
                res.registerGetNext()
                self.getNextToken()
                return res.success(_expression)
            else:
                return res.failure(InvalidSyntaxError('expected ")"', self.currentToken.position))
        
        elif token.type == TT_LSQUARE:
            list_expression = res.register(self.listExpression())
            if res.error : return res
            return res.success(list_expression)

        elif token.matches(TT_KEYWORD,'IF'):
            if_expression = res.register(self.ifExpression())
            if res.error : return res
            return res.success(if_expression)

        elif token.matches(TT_KEYWORD,'FOR'):
            for_expression = res.register(self.forExpression())
            if res.error : return res
            return res.success(for_expression)

        elif token.matches(TT_KEYWORD,'WHILE'):
            while_expression = res.register(self.whileExpression())
            if res.error : return res
            return res.success(while_expression)

        elif token.matches(TT_KEYWORD, 'PRINT'):
            print_expression = res.register(self.printExpression())
            if res.error : return res
            return res.success(print_expression)
        
        elif token.matches(TT_KEYWORD,'STRINGIFY'):
            stringify_expression = res.register(self.stringifyExpression())
            if res.error : return res
            return res.success(stringify_expression)

        elif token.matches(TT_KEYWORD, 'SUM'):
            sum_expression = res.register(self.sumExpression())
            if res.error : return res
            return res.success(sum_expression)


        return res.failure(InvalidSyntaxError('expected  IDENTIFIER, BOOL ,NUMBER, STRING,  IF, FOR, WHILE,PRINT,SUM,STRINGIFY "+", "-" ,"(" or "["   ', self.currentToken.position))



    def ifExpression(self):
        res = ParseResult()
        base_case = None
        else_case = None

        if not self.currentToken.matches(TT_KEYWORD, 'IF'):
            return res.failure(InvalidSyntaxError('expected IF keyword',self.currentToken.position))
			
        res.registerGetNext()
        self.getNextToken()

        condition = res.register(self.expression())
        if res.error : return res


        if not self.currentToken.matches(TT_KEYWORD, 'THEN'):
            return res.failure(InvalidSyntaxError('expected THEN keyword',self.currentToken.position))

        res.registerGetNext()
        self.getNextToken()

        _expression = res.register(self.expression())
        if res.error : return res

        base_case = (condition,_expression)

        if self.currentToken.matches(TT_KEYWORD,'ELSE'):
            res.registerGetNext()
            self.getNextToken()

            else_case = res.register(self.expression())
            if res.error : return res

        
        return res.success(IfNode(base_case,else_case))

    def forExpression(self):
        res = ParseResult()

        if not self.currentToken.matches(TT_KEYWORD, 'FOR'):
            return res.failure(InvalidSyntaxError('expected FOR keyword',self.currentToken.position))

        res.registerGetNext()
        self.getNextToken()

        if  self.currentToken.type != TT_IDENTIFIER:
            return res.failure(InvalidSyntaxError('expected IDENTIFIER ',self.currentToken.position))

        varName = self.currentToken
        res.registerGetNext()
        self.getNextToken()

        if  self.currentToken.type != TT_EQ:
            return res.failure(InvalidSyntaxError('expected assignment operator " = " ',self.currentToken.position))

        res.registerGetNext()
        self.getNextToken()

        startValue = res.register(self.expression())
        if res.error : return res

        if not self.currentToken.matches(TT_KEYWORD, 'TO'):
            return res.failure(InvalidSyntaxError('expected TO keyword',self.currentToken.position))

        res.registerGetNext()
        self.getNextToken()

        endValue = res.register(self.expression())
        if res.error : return res

        if  self.currentToken.matches(TT_KEYWORD, 'STEP'):
            res.registerGetNext()
            self.getNextToken()

            stepValue = res.register(self.expression())
            if res.error : return res

        else:
            stepValue = None


        if not self.currentToken.matches(TT_KEYWORD, 'DO'):
            return res.failure(InvalidSyntaxError('expected DO keyword',self.currentToken.position))

        res.registerGetNext()
        self.getNextToken()

        body = res.register(self.expression())
        if res.error : return res

        return res.success(ForNode(varName,startValue,endValue,stepValue,body))



    def whileExpression(self):
        res = ParseResult()

        if not self.currentToken.matches(TT_KEYWORD, 'WHILE'):
            return res.failure(InvalidSyntaxError('expected WHILE keyword',self.currentToken.position))

        res.registerGetNext()
        self.getNextToken()

        condition = res.register(self.expression())
        if res.error : return res


        if not self.currentToken.matches(TT_KEYWORD, 'DO'):
            return res.failure(InvalidSyntaxError('expected DO keyword',self.currentToken.position))

        res.registerGetNext()
        self.getNextToken()

        body = res.register(self.expression())
        if res.error : return res

        return res.success(WhileNode(condition,body))


    def printExpression(self):
        res = ParseResult()

        if not self.currentToken.matches(TT_KEYWORD, 'PRINT'):
            return res.failure(InvalidSyntaxError('expected PRINT keyword',self.currentToken.position))

        res.registerGetNext()
        self.getNextToken()

        body = res.register(self.expression())
        if res.error : return res

        return res.success(PrintNode(body))

    def sumExpression(self):
        res = ParseResult()

        if not self.currentToken.matches(TT_KEYWORD, 'SUM'):
            return res.failure(InvalidSyntaxError('expected SUM keyword',self.currentToken.position))

        res.registerGetNext()
        self.getNextToken()

        token = self.currentToken
        if token.type == TT_IDENTIFIER:
            res.registerGetNext()
            self.getNextToken()
            listNode= VarAccessNode(token)

        else:
            listNode = res.register(self.listExpression())
            if res.error : return res
        

        return res.success(SumNode(listNode))
            

    def stringifyExpression(self):
        res = ParseResult()

        if not self.currentToken.matches(TT_KEYWORD, 'STRINGIFY'):
            return res.failure(InvalidSyntaxError('expected STRINGIFY keyword',self.currentToken.position))

        res.registerGetNext()
        self.getNextToken()

        token = self.currentToken

        if token.type == TT_IDENTIFIER:
            res.registerGetNext()
            self.getNextToken()
            resNode = VarAccessNode(token)
        
        elif token.type == TT_BOOL:
            res.registerGetNext()
            self.getNextToken()
            resNode = BoolNode(token)
        
        elif token.type == TT_NUMBER:
            res.registerGetNext()
            self.getNextToken()
            resNode = NumberNode(token)

        elif token.type == TT_STRING:
            res.registerGetNext()
            self.getNextToken()
            resNode = StringNode(token)
        
        else:
            resNode = res.register(self.listExpression())
            if res.error : return res


        return res.success(StringifyNode(resNode))

    def listExpression(self):
        res = ParseResult()
        elementNodes = []
        position = self.currentToken.position.copy()

        if self.currentToken.type != TT_LSQUARE:
            return res.failure(InvalidSyntaxError('expected [',self.currentToken.position))

        res.registerGetNext()
        self.getNextToken()

        if self.currentToken.type == TT_RSQUARE:
            res.registerGetNext()
            self.getNextToken()

        else:
            elementNodes.append(res.register(self.expression()))
            if res.error:
                return res.failure(InvalidSyntaxError('expected ] , LET , IF , FOR ,WHILE, BOOL,STRING, NUMBER, IDENTIFIER , ( ,[ , ! ',self.currentToken.position))

            while self.currentToken.type == TT_COMMA:
                res.registerGetNext()
                self.getNextToken()

                elementNodes.append(res.register(self.expression()))
                if res.error: return res

            if self.currentToken.type != TT_RSQUARE:
                return res.failure(InvalidSyntaxError('expected "," or "]" ',self.currentToken.position))

            res.registerGetNext()
            self.getNextToken()

        return res.success(ListNode(elementNodes,position))

   


    def power(self):
        return self.binaryOperation(self.atom, (TT_POW),self.factor)

    def factor(self):
        res = ParseResult()
        token = self.currentToken

        if token.type in (TT_PLUS,TT_MINUS):
            res.registerGetNext()
            self.getNextToken()
            _factor = res.register(self.factor())
            
            if res.error : return res
            return res.success(UnaryOperationNode(token, _factor))

        return self.power()


    def term(self):
        return self.binaryOperation(self.factor,(TT_MULT,TT_DIV,TT_MOD,TT_FLOORDIV))


    def arithmeticExpression(self):
        return self.binaryOperation(self.term, (TT_PLUS,TT_MINUS))

    def comparaisonExpression(self):
        res = ParseResult()

        if self.currentToken.type == TT_NOT:
            operationToken = self.currentToken
            res.registerGetNext()
            self.getNextToken()

            rightNode = res.register(self.comparaisonExpression())
            if res.error : return res

            return res.success(UnaryOperationNode(operationToken, rightNode))

        node = res.register(self.binaryOperation(self.arithmeticExpression, (TT_EE,TT_NE,TT_LE,TT_GE,TT_GT,TT_LT)))

        if res.error : return res.failure(InvalidSyntaxError('expected LET, IF, FOR, WHILE,  IDENTIFIER, NUMBER, STRING,BOOL  "+", "-" ,"(" , "[" , "!" ', self.currentToken.position,))

        return res.success(node) 


    def expression(self):
        
        res = ParseResult()

        if self.currentToken.matches(TT_KEYWORD,'LET'):
            res.registerGetNext()
            self.getNextToken()

            if self.currentToken.type != TT_IDENTIFIER:
                return res.failure(InvalidSyntaxError('expected IDENTIFIER', self.currentToken.position))

            varToken = self.currentToken
            res.registerGetNext()
            self.getNextToken()

            if self.currentToken.type != TT_EQ:
                return res.failure(InvalidSyntaxError('expected assignment operator " = "', self.currentToken.position))

            res.registerGetNext()
            self.getNextToken()
            
            _expression = res.register(self.expression())

            if res.error : return res
            return res.success(VarAssignNode(varToken,_expression))        


        node =  res.register(self.binaryOperation(self.comparaisonExpression,(TT_AND,TT_OR)))
        
        if res.error :return res.failure(InvalidSyntaxError('expected LET, IF, FOR, WHILE,  IDENTIFIER, NUMBER, STRING,BOOL  "+", "-" ,"(" , "[" , "!" ', self.currentToken.position))

        return res.success(node)



    def statement(self):
        res = ParseResult()
        expressions = []
        position = self.currentToken.position.copy()

        while self.currentToken.type == TT_NL:
            res.registerGetNext()
            self.getNextToken()

        _expression = res.register(self.expression())
        if res.error : return res
        expressions.append(_expression)

        moreStatements = True

        while True:
            newLineCounter = 0
            while self.currentToken.type == TT_NL:
                res.registerGetNext()
                self.getNextToken()
                newLineCounter += 1

            if newLineCounter == 0: moreStatements = False
            if not moreStatements : break

            _expression = res.tryRegister(self.expression())

            if not _expression:
                self.reverse(res.reverseCount)
                moreStatements = False
                continue
            expressions.append(_expression)

        return res.success(ListNode(expressions,position))
            




    def binaryOperation(self,func,operations,func_2 = None):

        if not func_2:
            func_2 = func

        res = ParseResult()
        leftNode = res.register(func())

        if res.error : return res
        
        while self.currentToken.type in operations:
            operationToken = self.currentToken
            res.registerGetNext()
            self.getNextToken()
            rightNode = res.register(func_2())

            if res.error : return res
        
            leftNode  = BinaryOperationNode(leftNode, operationToken, rightNode)

        return res.success(leftNode)
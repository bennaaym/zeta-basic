from .Token import Token
from .constants import *
from zeta_basic.ERRORS.Error import IllegalCharError
from .Position import Position

class Lexer:

    def __init__(self,code):
        self.code = code
        self.currentChar = None
        self.position = Position(-1, 1, -1)
        self.getNextChar()

    def getNextChar(self):

        self.position.next(self.currentChar)
        self.currentChar = self.code[self.position.index] if self.position.index < len(self.code) else None

    
    def tokenize(self):
        tokens = []

        while self.currentChar != None:

            if self.currentChar in ' \t':
                self.getNextChar()

            elif self.currentChar in ';\n':
                tokens.append(Token(TT_NL,position=self.position))
                self.getNextChar()

            elif self.currentChar in  LETTERS:
                tokens.append(self.makeKeywordOrIdentifierOrBool())

            elif self.currentChar in DIGITS:
                tokens.append(self.makeNumber())
            
            elif  self.currentChar == '"':
                token ,error =self.makeString()
                if error : return [],error
                tokens.append(token)

            elif self.currentChar == '+':
                tokens.append(Token(TT_PLUS,position=self.position))
                self.getNextChar()

            elif self.currentChar == '-':
                tokens.append(Token(TT_MINUS,position=self.position))
                self.getNextChar()

            elif self.currentChar == '*':
                tokens.append(self.makeMulOrPow())

            elif self.currentChar == '/':
                tokens.append(self.makeDivOrFloorDiv())

            
            elif self.currentChar == '%':
                tokens.append(Token(TT_MOD,position=self.position))
                self.getNextChar()
            
            elif self.currentChar == '=':
                tokens.append(self.makeEqualOrAssign())

            elif self.currentChar == '(':
                tokens.append(Token(TT_LPAREN,position=self.position))
                self.getNextChar()

            elif self.currentChar == ')':
                tokens.append(Token(TT_RPAREN,position=self.position))
                self.getNextChar()

            elif self.currentChar == '[':
                tokens.append(Token(TT_LSQUARE,position=self.position))
                self.getNextChar()

            elif self.currentChar == ']':
                tokens.append(Token(TT_RSQUARE,position=self.position))
                self.getNextChar()
                
            elif self.currentChar == ',':
                tokens.append(Token(TT_COMMA,position=self.position))
                self.getNextChar()

            elif self.currentChar == '!':
                tokens.append(self.makeNotEqualOrNot())

            elif self.currentChar == '<':
                tokens.append(self.makeLtOrLe())

            elif self.currentChar == '>':
                tokens.append(self.makeGtOrGe())

            elif self.currentChar == '&':
                self.getNextChar()
                if self.currentChar !='&':
                    return [],IllegalCharError('expected " & "',self.position.copy())
                tokens.append(Token(TT_AND,position = self.position))
                self.getNextChar()

            
            elif self.currentChar == '|':
                self.getNextChar()
                if self.currentChar !='|':
                    return [],IllegalCharError('expected " | "',self.position.copy())
                tokens.append(Token(TT_OR,position = self.position))
                self.getNextChar()


            else:
                return [],IllegalCharError(f'unexpected character " {self.currentChar} "',self.position.copy())


        tokens.append(Token(TT_EOF,position=self.position))
        return tokens,None

    
    def makeNumber(self):       
        number = ''
        decPoint = 0
        position = self.position.copy()

        while self.currentChar != None and self.currentChar in DIGITS+'.':
            if self.currentChar == '.':
                if decPoint == 1 : break
                decPoint = 1
            
            number += self.currentChar
            self.getNextChar()
        
        return Token(TT_NUMBER,int(number),position) if decPoint == 0 else Token(TT_NUMBER,float(number),position)


    def makeString(self):
        string = ''
        position = self.position.copy()
        escapeChar = False
        escapeCharDict = {
            'n' : '\n',
            't' : '\t',
            'b' : '\b',
            'r' : '\r',
            'f' : '\f',
        }
        self.getNextChar()

        while self.currentChar != None and (self.currentChar != '"' or escapeChar):
            if escapeChar:
                string += escapeCharDict.get(self.currentChar,self.currentChar)
                escapeChar = False
    
            else:
                if self.currentChar == '\\':
                    escapeChar = True
                else:
                    string += self.currentChar

            self.getNextChar()

        if self.currentChar != '"':
            return None,IllegalCharError('expected " ', position = position)

        self.getNextChar()
        return Token(TT_STRING,string,position=position),None

    def makeMulOrPow(self):
        tokenType = TT_MULT
        position = self.position.copy()

        self.getNextChar()

        if self.currentChar == '*':
            tokenType = TT_POW
            self.getNextChar()

        return Token(tokenType,position=position)

    def makeDivOrFloorDiv(self):
        tokenType = TT_DIV
        position = self.position.copy()

        self.getNextChar()

        if self.currentChar == '/':
            tokenType = TT_FLOORDIV
            self.getNextChar()

        return Token(tokenType,position=position)

    def makeKeywordOrIdentifierOrBool(self):
        identifier = ''
        position = self.position.copy() 

        while self.currentChar != None and self.currentChar in LETTERS_DIGITS+'_':
            identifier += self.currentChar
            self.getNextChar()

        if identifier in KEYWORDS : return Token(TT_KEYWORD,identifier,position=position)
        elif identifier in (TRUE,FALSE) : return Token(TT_BOOL,identifier,position=position)
        return Token(TT_IDENTIFIER,identifier,position=position)


    def makeEqualOrAssign(self):
        tokenType = TT_EQ
        position = self.position.copy() 
        self.getNextChar()

        if self.currentChar == '=':
            tokenType = TT_EE
            self.getNextChar()

        return Token(tokenType,position = position)

    def makeNotEqualOrNot(self):
        tokenType = TT_NOT
        position = self.position.copy() 
        self.getNextChar()

        if self.currentChar == '=':
            tokenType = TT_NE
            self.getNextChar()

        return Token(tokenType,position = position)

    def makeGtOrGe(self):
        tokenType = TT_GT
        position = self.position.copy() 
        self.getNextChar()

        if self.currentChar == '=':
            tokenType = TT_GE
            self.getNextChar()

        return Token(tokenType,position = position)
    
    def makeLtOrLe(self):
        tokenType = TT_LT
        position = self.position.copy() 
        self.getNextChar()

        if self.currentChar == '=':
            tokenType = TT_LE
            self.getNextChar()

        return Token(tokenType,position = position)

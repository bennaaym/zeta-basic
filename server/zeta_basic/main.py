
from zeta_basic.LEXER.Lexer import Lexer
from zeta_basic.PARSER.Parser import Parser
from zeta_basic.INTERPRETER.Interpreter import Interpreter
from zeta_basic.INTERPRETER.Context import Context
from zeta_basic.INTERPRETER.SymbolTable import SymbolTable


def run(code):
    ## GLOBAL VARIABLES
    globalSymbolTable = SymbolTable()
    
    if code.strip() == '' : return None,None

    ## LEXING
    lexer = Lexer(code)
    tokens,error = lexer.tokenize()
    
    if error : 
        return None,error

    ## PARSING
    parser = Parser(tokens)
    ast = parser.parse()

    if ast.error :
        return None,ast.error
    
    ## INTERPRETING

    interpreter = Interpreter()
    context = Context("<main>",symbolTable=globalSymbolTable)
    result = interpreter.visit(ast.node,context)
    if result : 
        if result.error : return None,result.error
        elif result.value : return result.value,None



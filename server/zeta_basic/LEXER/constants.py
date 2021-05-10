import string

#############################
#         TOKENS            #
#############################
TT_KEYWORD       =   'KEYWORD'
TT_IDENTIFIER    =   'IDENTIFIER'

TT_BOOL          =   'BOOL'
TT_NUMBER        =   'NUMBER'
TT_STRING        =   'STRING'

TT_PLUS          =   'PLUS'
TT_MINUS         =   'MINUS'
TT_MULT          =   'MULT'
TT_DIV           =   'DIV'
TT_MOD           =   'MOD'
TT_POW           =   'POW'
TT_FLOORDIV      =   'FLOORDIV'
TT_LPAREN        =   'LPAREN'
TT_RPAREN        =   'RPAREN'

TT_COMMA         =   'COMMA'
TT_LSQUARE       =   'LSQUARE'
TT_RSQUARE       =   'RSQUARE'

TT_EQ            =   'EQ'

TT_EE            =   'EE'
TT_NE            =   'NE'
TT_GT            =   'GT'
TT_LT            =   'LT'
TT_GE            =   'GE'
TT_LE            =   'LE'

TT_AND           =   'AND'
TT_OR            =   'OR'
TT_NOT           =   'NOT' 

TT_NL            =   'NL'
TT_EOF           =   'EOF'

#############################
#         KEYWORDS          #
#############################
TRUE = 'TRUE'
FALSE = 'FALSE'

KEYWORDS = (
    'LET',
    'IF',
    'THEN',
    'ELSE',
    'FOR',
    'TO',
    'STEP',
    'WHILE',
    'DO',
    'PRINT',
    'END',
    'SUM',
    'STRINGIFY'
)


#############################
#         OTHER             #
#############################

DIGITS = '0123456789'
LETTERS =string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS

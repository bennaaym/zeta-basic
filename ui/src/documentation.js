export const datatypes = ['Bool','Number (int, float)','String','List']

export const documentation=[
    {
        name:'variables',
        description : [
            ['variables are defined using  "LET" keyword']
        ],
        exemples:[
            ['Syntax : LET var_name = datatype | expression ;'],
            ['LET a = TRUE ; LET b = FALSE ;','LET x = 5 ; LET y = 3.14 ;','LET z = [1,2,3] ;','LET s = "this is a String" ;'] 
        ]
    },
    {
        name:'arithmetic operators',
        description:[
            ['addition, subtraction, multiplication, division, modulo, floor division (//), and power(**) operators are available'],
            ['operations on List are inspired by the NumPy library ']
        ],
        exemples:[
            [   'Syntax :',
                '(+)    : (Number + Number) or (List + List) or (String + String) or (List + Number)',
                '(-)    : (Number - Number) or (List - List) or (List + Number)',
                '(*)    : (Number * Number) or (List * List) or (String * Number) or(List + Number)',
                '(/)    : (Number / Number) or (List / List) or (List / Number)',
                '(%)    : (Number % Number) ',
                '(//)   : (Number // Number) or (List // List) or (List // Number)',
                '(**)   : (Number * Number)',
                '-----------------------------------',
                'Otherwise :',
                'RunTimeError -> unsupported operand type(s)'  

            ]
        ]
    },
    {
        name:'comparison  operators',
        description:[
            ['equal, not equal, less than, greater than, less than or equal, and greater than or equal operators are available'],
        ],
        exemples:[
            ['Syntax :',
                '(==)   : (dataype == datatype)',
                '(!=)   : (datatype != datatype)',
                '(<)    : (Number < Number) or (String < String)',
                '(>)    : (Number > Number) or (String > String)',
                '(<=)    : (Number <= Number) or (String <= String)',
                '(>=)   : (Number >= Number) or (String >= String)',
                '-----------------------------------',
                'Otherwise :',
                'RunTimeError -> unsupported operand type(s)'
            ]
        ]

    },
    {
        name:'logical  operators',
        description:[
            ['not, and, or operetors are available'],
            ['value 0 ,empty String ,empty List  corresponds to "FALSE" any other value  corresponds to "TRUE"']
        ],
        exemples:[
            ['Syntax :',
                    '(!)    : (! datatype)',
                    '(&&)   : (datatype && datatype)',
                    '(||)    : (datatype || datatype)',
                ]
        ]
    },
    {
        name:'conditional Statements',
        description:[
            ['if-statement  returns a value thus it can be assigned to a variable']
        ],
        exemples:[
            ['Syntax : IF condition THEN expression ELSE expression'],
            ['LET x = 5;',
             'LET y = IF x < 5 THEN x ELSE x**2;',
             'PRINT y',
            ]
        ]
            
        
    },
    {
        name:'for loop',
        description:[
            ['for-loop  returns a List thus it can be assigned to a variable']
        ],
        exemples:[
            ['Syntax :',
                'FOR var_counter = start_value TO end_value DO expression ;',
                'or',
                'FOR var_counter = start_value TO end_value STEP step_value DO expression ;',
            ],
            ['LET x = FOR i =0 TO 10 DO i;',
             'PRINT x',

            ]
        ]
    },
    {
        name:'while loop',
        description:[
            ['while-loop  returns a List thus it can be assigned to a variable']
        ],
        exemples:[
            ['Syntax : WHILE condition DO expression ;'],
            ['LET i = 0;',
              'LET x = WHILE i < 10 DO LET i = i + 1;',
              'PRINT x'
          
            ]
        ]
    },
    {
        name:'built-in functions',
        description:[
            ['PRINT ,SUM, and STRINGIFY functions are available'],
            ['all built-in functions return a value thus they can be assigned to a variable']
        ],

        exemples:[
            ['Syntax:','PRINT expression ;','SUM List ;','STRINGIFY datatype ;'],
            
        ]
    }
    
]


export const codeExamples = [
    {
        name:'Hello world !',
        description:[],
        exemples:[
            ['PRINT "Hello world!";']
        ]
    },
    {
        name:'Find the area of a triangle',
        description:[],
        exemples:[
            ['LET first_side = 5;',
             'LET second_side = 4;',
             'LET third_side = 3;',
             'LET s = (first_side+second_side+third_side)/2;',
             'LET area = (s*(s-first_side)*(s-second_side)*(s-third_side)) ** 0.5 ;',
             'PRINT "the area of the triangle is: "+ STRINGIFY area']
        ]
    },
    {
        name:'Factorial n!',
        description:[],
        exemples:[
            [
                'LET n = 9;',
                'LET fact = 1;',
                'FOR i = 1 TO n + 1 DO LET fact = fact * i;',
                
                'PRINT STRINGIFY n +" factorial is : "+ STRINGIFY fact;',
            ]
        ]
    },
    {
        name:'Check Prime Number',
        description:[],
        exemples:[
            [
                'LET number = 97;', 
                'LET counter = 1;',
                'LET upper_value =  number //2 +1;',
                'LET is_prime = TRUE;',
                'LET i = 2;',
                'FOR i = 2 TO upper_value DO IF number % i == 0 THEN LET is_prime = FALSE;',
                'LET result = STRINGIFY number;',
                'LET result = result + IF is_prime THEN " is prime"  ELSE " is not prime";',

                'PRINT result;'
            ]
        ]
    },
    {
        name:'Print a triangle',
        description:[],
        exemples:[
            [
                'LET n = 10;',
                'LET triangle = FOR i =0 TO n DO PRINT "#" * i +"\n";',
            ]
        ]
    }
]
# Zeta-Basic

## About ζ basic

  - ζ basic basic is a small interpreted programming language based on python. Its syntax is mainly inspired by the BASIC language.
  
## ζ basic documentation
  
  #### datatypes

    ζ basic has 4 data types .

    Bool
    Number (int, float)
    String
    List
  
  #### variables
    
    Syntax :  LET var_name = datatype | expression ;
  
  #### arithmetic operators 
  addition, subtraction, multiplication, division, modulo, floor division (//), and power(**) operators are available . operations on List are inspired by the NumPy library .
  
    Syntax :

    (+)  : (Number + Number) or (List + List) or (String + String) or (List + Number)
    (-)  : (Number - Number) or (List - List) or (List + Number)
    (*)  : (Number * Number) or (List * List) or (String * Number) or(List + Number)
    (/)  : (Number / Number) or (List / List) or (List / Number)
    (%)  : (Number % Number)
    (//) : (Number // Number) or (List // List) or (List // Number)
    (**) : (Number * Number)
    
  #### comparison operators 
  equal, not equal, less than, greater than, less than or equal, and greater than or equal operators are available .
  
    Syntax :
    
    (==) : (dataype == datatype)
    (!=) : (datatype != datatype)
    (<) : (Number < Number) or (String < String)
    (>) : (Number > Number) or (String > String)
    (<=) : (Number <= Number) or (String <= String)
    (>=) : (Number >= Number) or (String >= String)
    
  #### logical operators
  not, and, or operetors are available .value 0 ,empty String ,empty List corresponds to "FALSE" any other value corresponds to "TRUE" .  
    
    Syntax :
    
    (!) : (! datatype)
    (&&) : (datatype && datatype)
    (||) : (datatype || datatype)
    
  #### conditional Statements
  if-statement returns a value thus it can be assigned to a variable .
    
    Syntex :  IF condition THEN expression ELSE expression
    
  #### for loop 
  for-loop returns a List thus it can be assigned to a variable .
    
    Syntax :

    FOR var_counter = start_value TO end_value DO expression ;
    FOR var_counter = start_value TO end_value STEP step_value DO expression ;
    
  #### while loop
  while-loop returns a List thus it can be assigned to a variable .
    
    Syntax : WHILE condition DO expression ;
  
  #### built-in functions 
  PRINT ,SUM, and STRINGIFY functions are available . all built-in functions return a value thus they can be assigned to a variable .
    
    Syntax:

    PRINT expression ;
    SUM List ;
    STRINGIFY datatype ;
    
## ζ basic code examples
  
  #### Hello world !
    
    PRINT "Hello world!";

  #### Find the area of a triangle
    
    LET first_side = 5;
    LET second_side = 4;
    LET third_side = 3;
    LET s = (first_side+second_side+third_side)/2;
    LET area = (s*(s-first_side)*(s-second_side)*(s-third_side)) ** 0.5 ;
    PRINT "the area of the triangle is: "+ STRINGIFY area
    
  #### Factorial n!
 
    LET n = 9;
    LET fact = 1;
    FOR i = 1 TO n + 1 DO LET fact = fact * i;
    PRINT STRINGIFY n +" factorial is : "+ STRINGIFY fact;
    
  #### Check Prime Number
    
    LET number = 97;
    LET counter = 1;
    LET upper_value = number //2 +1;
    LET is_prime = TRUE;
    LET i = 2;
    FOR i = 2 TO upper_value DO IF number % i == 0 THEN LET is_prime = FALSE;
    LET result = STRINGIFY number;
    LET result = result + IF is_prime THEN " is prime" ELSE " is not prime";
    PRINT result;


  #### Print a triangle
    
    LET n = 10;
    LET triangle = FOR i =0 TO n DO PRINT "#" * i +" ";

# ZETA BASIC

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#links">Links</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
    <li>
      <a href="#documentation">Documentation</a>
      <ul>
        <li><a href="#data-types">Data Types</a></li>
        <li><a href="#variables">Variables</a></li>
        <li><a href="#arithmetic-operators">Arithmetic Operators</a></li>
        <li><a href="#comparison-operators">Comparison Operators</a></li>
        <li><a href="#logical-operators">Logical Operators</a></li>
        <li><a href="#conditional-statements">Conditional Statements</a></li>
        <li><a href="#for-loop">For Loop</a></li>
        <li><a href="#while-loop">While Loop</a></li>
        <li><a href="#built-in-functions">Built-in Functions</a></li>
      </ul>
    </li>
    <li>
      <a href="#code-examples">Code Examples</a>
      <ul>
          <li><a href="#hello-world">Hello World</a></li>
          <li><a href="#find-the-area-of-a-triangle">Find The Area of a Triangle</a></li>
          <li><a href="#factorial-n">Factorial n!</a></li>
          <li><a href="#check-prime-number">Check Prime Number</a></li>
          <li><a href="#print-a-triangle">Print a Triangle</a></li>
      </ul>
    </li>
    <li><a href="#what-is-next">What is Next</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://zeta-basic.web.app/)

[ζ basic](https://zeta-basic.web.app/) is a small interpreted programming language based on python. Its syntax is mainly inspired by the BASIC language.

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Tailwindcss](https://tailwindcss.com/)
* [React.js](https://reactjs.org)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
* [Python](https://www.python.org/)
* [PIP](https://pypi.org/project/pip/)
* [Node.js](https://nodejs.org)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/bennaaym/zeta-basic.git
   ```
2. Install python packages 
   ```sh
   pip install -r requirements.txt
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
   
3. inside the ui directory create a `.env.local` file  and past the line below
   ```sh
   REACT_APP_INTERPRETER_API=http://127.0.0.1:5000/api/input
   
   ```


<!-- LICENSE -->
## License
[![MIT License][license-shield]][license-url]<br>
Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Links

* Project website : [https://zeta-basic.web.app/](https://zeta-basic.web.app/)
* Project repo: [https://github.com/bennaaym/zeta-basic.git](https://github.com/bennaaym/zeta-basic.git)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Heroku](https://dashboard.heroku.com/apps)
* [Firebase Hosting](https://www.firebase.com/)

## Documentation

  #### Data types

  - ζ basic has 4 data types .
    * Bool
    * Number (int, float)
    * String
    * List
  
  #### Variables
    
    Syntax :  LET var_name = datatype | expression ;
  
  #### Arithmetic Operators 
  addition, subtraction, multiplication, division, modulo, floor division (//), and power(**) operators are available . operations on List are inspired by the NumPy library .
  
    Syntax :
      (+)  : (Number + Number) or (List + List) or (String + String) or (List + Number)
      (-)  : (Number - Number) or (List - List) or (List + Number)
      (*)  : (Number * Number) or (List * List) or (String * Number) or(List + Number)
      (/)  : (Number / Number) or (List / List) or (List / Number)
      (%)  : (Number % Number)
      (//) : (Number // Number) or (List // List) or (List // Number)
      (**) : (Number * Number)
    
  #### Comparison Operators 
  equal, not equal, less than, greater than, less than or equal, and greater than or equal operators are available .
  
    Syntax :
    
    (==) : (dataype == datatype)
    (!=) : (datatype != datatype)
    (<) : (Number < Number) or (String < String)
    (>) : (Number > Number) or (String > String)
    (<=) : (Number <= Number) or (String <= String)
    (>=) : (Number >= Number) or (String >= String)
    
  #### Logical Operators
  not, and, or operetors are available .value 0 ,empty String ,empty List corresponds to "FALSE" any other value corresponds to "TRUE" .  
    
    Syntax :
    
    (!) : (! datatype)
    (&&) : (datatype && datatype)
    (||) : (datatype || datatype)
    
  #### Conditional Statements
  if-statement returns a value thus it can be assigned to a variable .
    
    Syntex :  IF condition THEN expression ELSE expression
    
  #### For Loop 
  for-loop returns a List thus it can be assigned to a variable .
    
    Syntax :

    FOR var_counter = start_value TO end_value DO expression ;
    FOR var_counter = start_value TO end_value STEP step_value DO expression ;
    
  #### While Loop
  while-loop returns a List thus it can be assigned to a variable .
    
    Syntax : WHILE condition DO expression ;
  
  #### Built-in Functions 
  PRINT ,SUM, and STRINGIFY functions are available . all built-in functions return a value thus they can be assigned to a variable .
    
    Syntax:

    PRINT expression ;
    SUM List ;
    STRINGIFY datatype ;
    
## Code Examples
  
  #### Hello World
    
    PRINT "Hello world!";

  #### Find The Area of a Triangle
    
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

## What is Next 
  * implementation of functions
  * implementation of multiline statements
  * multi-files support

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[product-screenshot]: https://i.ibb.co/7SRLf7V/screely-1626383144625.png

from zeta_basic.main import run

def process_input(input):
    
    ## find PRINT statements if any
    statements = input.split(';')
    print_indexes = []
    index = 0
    for statement in statements:
        if 'PRINT' in statement:
            print_indexes.append(index)
        
        index +=1

    ## pass code to the interpreter
    return_values,error = run(input)

    if error : return {'outputs':[{'value':str(error)}]}

    output = []
    counter = 0

    for index in print_indexes:
        output.append({f'value':str(return_values.value[index])})
        counter +=1

    return {'outputs':output}


    

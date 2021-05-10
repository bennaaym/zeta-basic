import main

while True:
    code = input('small basic > ')
    result ,error = main.run(code) 

    if error : print(error)
    elif result :print(result)
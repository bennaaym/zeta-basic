from flask import Flask,request
from flask_cors import CORS,cross_origin

from modules.modules import process_input

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*"})



@app.route('/api/input',methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])

def input():
    try:
        output = process_input(request.get_json()['input'])
    except Exception as exception:
        print(exception)
        output = {"outputs":[{"value":"code can't be executed"}]}
    return output


if __name__ == "__main__" :
    app.run()

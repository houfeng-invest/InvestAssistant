from flask import Flask
import flask_restful
from  flask_restful import Resource
app = Flask(__name__)
api = flask_restful.Api(app)

class Test(Resource):
    def get(self):
        return "InvestAssistant"

api.add_resource(Test,"/test")

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import tempfile
import pickle
import numpy as np

app = Flask(__name__)
app.logger.setLevel('INFO')

api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('sepal_length',
                    type=float,
                    required=True,
                    help='iris sepal length')
parser.add_argument('sepal_width',
                    type=float,
                    required=True,
                    help='iris sepal width')
parser.add_argument('petal_length',
                    type=float,
                    required=True,
                    help='iris petal length')
parser.add_argument('petal_width',
                    type=float,
                    required=True,
                    help='iris petal width')

def load_model(model_path):
    """Load model to return for future use."""
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model('./model.pickle')

class Iris(Resource):
    def post(self):
        args = parser.parse_args()
        input_array = np.array([[
            args['sepal_length'],
            args['sepal_width'],
            args['petal_length'],
            args['petal_width']]])
        
        # predict
        result = model.predict(input_array).tolist()
        # formatting the results as a JSON-serializable structure:
        output = {'iris_type': result}
        return jsonify(output)

api.add_resource(Iris, '/iris')

if __name__ == '__main__':
    app.run(debug=True, port=6006, use_reloader=True, threaded=True)
    # curl command for Iris interface:
    # curl http://127.0.0.1:6006/iris -d "sepal_length=1.5" -d "sepal_width=2.4" -d "petal_length=1.2" -d "petal_width=2.3" -X POST

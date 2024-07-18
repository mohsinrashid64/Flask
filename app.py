from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # To handle CORS issues







@app.route('/', methods=['GET'])
def test():

    return jsonify({'response': 'API IS RUNNING'})




@app.route('/send-string', methods=['POST'])
def receive_string():
    data = request.get_json()
    string_data = data.get('string')
    print(f"Received string: {string_data}")
    return jsonify({'message': 'String received', 'string': string_data})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, json
from flask_cors import CORS

from Service import generate_travel_plan

app = Flask(__name__)
CORS(app, origins='*')

@app.route('/generate_travel_plan', methods=['GET','POST'])
def handle_generate_travel_plan():
    user_input = request.json
    plan = generate_travel_plan(json.dumps(user_input))
    return jsonify({'plan': plan})

# @app.route('/test', methods= ['GET'])
# def test():
#     print("testing")
#     return "testing......."
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)




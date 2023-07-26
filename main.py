from flask import Flask, request, jsonify, json
from flask_cors import CORS
# from flasgger import Swagger
import os
from Service import generate_travel_plan



app = Flask(__name__)
CORS(app, origins='*')

@app.route('/generate_travel_plan', methods=['GET','POST'])
def handle_generate_travel_plan():
    # """
    #     Generate a travel plan based on user input.
    #
    #     ---
    #     parameters:
    #       - name: user_input
    #         in: body
    #         description: User input in JSON format.
    #         required: true
    #         schema:
    #           type: object
    #           properties:
    #             city:
    #               type: string
    #             duration:
    #               type: string
    #             preferences:
    #               type: array
    #               items:
    #                 type: string
    #     responses:
    #       200:
    #         description: Successfully generated a travel plan.
    #         schema:
    #           type: object
    #           properties:
    #             plan:
    #               type: string
    #               description: The generated travel plan.
    #     """
    user_input = request.json
    plan = generate_travel_plan(json.dumps(user_input))
    return jsonify({'plan': plan})

# app.config['SWAGGER'] = {
#     'title': 'Travel Plan API',
#     'description': 'API for generating travel plans using GPT-3.5-turbo model',
#     'uiversion': 3
# }

# swagger = Swagger(app)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)



# from flask import Flask, request, jsonify, json
# from flask_cors import CORS
#
# from Service import generate_travel_plan
#
# app = Flask(__name__)
# CORS(app, origins='*')
#
# @app.route('/generate_travel_plan', methods=['POST'])
# def handle_generate_travel_plan():
#     user_input = request.json
#     response = generate_travel_plan(json.dumps(user_input))
#     return jsonify({'response': response})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)






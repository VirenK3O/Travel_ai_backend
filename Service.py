# import json
# import openai
# import os
# from dotenv import load_dotenv
#
# load_dotenv()  # Load environment variables from .env file
# API_KEY='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'
# API_KEY = os.getenv("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")
# openai.api_key = API_KEY
import json
import openai

API_KEY = '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'
openai.api_key = API_KEY

model_id = 'gpt-3.5-turbo'



def generate_travel_plan(user_input):
    json_input = json.loads(user_input)

    city = json_input["city"]
    duration = json_input["duration"]

    preferences = json_input["preferences"]

    plan = f"I'm in {city} for {duration}\t"

    for preference in preferences:
        plan += f"I like {preference}, "

    conversation = [
        {"role": "system", "content": plan + "Generate a day wise travel plan in short."}
    ]

    response = openai.ChatCompletion.create(model=model_id, messages=conversation)#sending conversation list to openai's chat API

    content = response['choices'][0]['message']['content']
    formatted_content = content.replace("\n", " ")

    print(formatted_content)
    return formatted_content
# def generate_travel_plan(user_input):
#     json_input = json.loads(user_input)
#
#     city = json_input["city"]
#     duration = json_input["duration"]
#
#     preferences = json_input["preferences"]
#
#     plan = f"I'm in {city} for {duration}\t"
#
#     for preference in preferences:
#         plan += f"I like {preference}, "
#
#     conversation = [
#         {"role": "system", "content": plan + "Generate a day wise travel plan in short."}
#     ]
#
#     response = openai.ChatCompletion.create(model=model_id, messages=conversation) # sending conversation list to OpenAI's chat API
#
#     content = response['choices'][0]['message']['content']
#     formatted_content = content.replace("\n", " ")
#
#     # Split the content into individual days based on the "Day" pattern
#     days = formatted_content.split("Day ")
#
#     # Remove empty strings from the list
#     days = [day.strip() for day in days if day.strip()]
#
#     return days

# def generate_travel_plan(user_input):
#     json_input = json.loads(user_input)
#
#     city = json_input["city"]
#     duration = json_input["duration"]
#
#     preferences = json_input["preferences"]
#     # avoidances = json_input["avoidances"]
#
#     plan = f"I'm in {city} for {duration}\t"
#
#     for preference in preferences:
#         plan += f"I like {preference}, "
#
#     # for avoidance in avoidances:
#     #     plan += f"I wish to avoid {avoidance}, "
#
#     conversation = [
#         {"role": "system", "content": plan + "Generate a travel plan."}
#     ]
#
#     response = openai.ChatCompletion.create(model=model_id, messages=conversation)
#
#     generated_response = response['choices'][0]['message']['content']
#     return generated_response


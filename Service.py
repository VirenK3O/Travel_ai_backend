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


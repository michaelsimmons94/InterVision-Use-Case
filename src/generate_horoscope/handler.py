import traceback
import sys
import boto3
import json
sys.path.append("..")
from connect_event import get_parameters


client = boto3.client('bedrock-runtime')

def generate_prompt(question, zodiacSign):
    return f"Pretend you're an astrologer, I am a {zodiacSign}. Give me a short horoscope without an introduction, answering the question \"{question}\""

def get_horoscope_message(prompt):
    body = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }
    response = client.invoke_model(
        body=json.dumps(body),
        modelId='meta.llama2-70b-chat-v1'
        )
    textResponse = response['body'].read().decode('utf-8')
    rawMessage = json.loads(textResponse).get("generation")
    message = rawMessage.replace("\n", " ").strip()[1:-1]
    return message

def handler(event, _context):
    parameters  = get_parameters(event)
    try:
        question = parameters["question"]
        sign = parameters["sign"]
        prompt = generate_prompt(question, sign)
        message = get_horoscope_message(prompt)
        return {"message": message}
    except Exception as e:
        print(e)
        traceback.print_exc()
        raise Exception("Failed to generate horoscope prompt")
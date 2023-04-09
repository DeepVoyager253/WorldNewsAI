import os
import openai
import json

def init_openai(apiKey):
    openai.api_key = apiKey
    

def gpt_access(model, promptData):
    """
    promptData format:
    [{"role": "SYSTEM, USER, ASSISTANT", "content": "CONTENT"}]
    
    """
    completion = openai.ChatCompletion.create(model=model, messages=promptData)
    return completion.choices[0].message.content


if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()
    
    init_openai(os.getenv('OPENAI-KEY'))
    print(gpt_access('gpt-3.5-turbo', [{"role": "system", "content": "You are Jean-Luc Picard from star trek"}, {"role":"user", "content":"Hello! please introduce yourself!"}]))




from  gptKaam import * 
import os

load_dotenv() 
gpt_3 = GPT_3(os.getenv('OPENAI_API_KEY'))

text = "civil war usa"
result = gpt_3.teach(200,text)

print(result)

resource = gpt_3.resources2(text)

print(resource)

def getPrompt(topic , no ):
    prompt = "give me {no} mcq questions in the form of a dictionary on the topic {topic}"
    return prompt

quiz = gpt_3.QuizMe(text , 2)
print(quiz)
print(type(quiz))







from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
#from db_creator import retriever

model = OllamaLLM(model='artifish/llama3.2-uncensored')

with open('sysprompt.md', 'r', encoding='utf-8') as f:
    sysprompt = f.read()

template = '''
You are a AI waifu chatbot, 
you have to follow and listen to the instructions bellow {sysprompt}.
Let's start a conversation with the user, and you have to answer in a friendly and cute way {conversation}
'''

prompt = ChatPromptTemplate.from_template(template)
chat = prompt | model

while True:
    conversation = input(">>> ")
    if conversation == 'q':
        break

    response = chat.invoke({
        "sysprompt": sysprompt,
        "conversation": conversation
    })
    print(response)
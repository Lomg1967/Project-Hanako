from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
#from csv_embeder import retriever
from datetime import datetime
import re
from pathlib import Path
import os
#from ustut 

model = OllamaLLM(model='artifish/llama3.2-uncensored')
num = 0
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dateNOtime = datetime.now().strftime("%Y-%m-%d")
timeNOdate = datetime.now().strftime("%H:%M:%S")

with open('sysprompt.md', 'r', encoding='utf-8') as f:
    sysprompt = f.read()

def memread():
    with open('memory.txt', 'r', encoding='utf-8') as f:
        f = f.read()
    return f
            
#re
def make_log_name(mkname):
    mkname = mkname.strip()
    mkname = re.sub(r'[<>:"/\\|?*]', '', mkname)
    mkname = mkname[:50]  
    return mkname
#re
#pathlib
log_dir = Path('chatlogs')
log_dir.mkdir(exist_ok=True)
chatlogs = None

template = '''
You are a AI waifu chatbot, 
you have to follow and listen to the instructions bellow {sysprompt}.
You should read the conversation history and remember things in the conversation {memory}
Let's start a conversation with the user, and you have to answer in a friendly and cute way {conversation}
'''

prompt = ChatPromptTemplate.from_template(template)
chat = prompt | model

while True:
    conversation = input(">>> ")

    if conversation == 'q':
        os.truncate('memory.txt', 0)
        break

    response = chat.invoke({
        "sysprompt": sysprompt,
        "memory": memread(),
        "conversation": conversation
    })
    print(response)

    #logging
    resp4log = f"{time}\n- User: {conversation}\n- AI: {response}\n"
    if chatlogs is None:
        log_name = make_log_name(timeNOdate)
        chatlogs = log_dir / f"{log_name}.log"

    with open(chatlogs, 'a', encoding='utf-8') as f:
        f.write(resp4log)
    #logging
    #memory
    resp4mem =  f"- User: {conversation}\n- AI: {response}\n"
    num = num + 1
    with open('memory.txt', 'a', encoding='utf-8') as f:
        f.write(f'{(num)}:\n {resp4mem}')
    #memory


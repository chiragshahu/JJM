import chainlit as cl
from crew import JJMCrew

__import__('pysqlite3')
import sys

sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

@cl.on_message
async def main(message: cl.Message):
    
    query = message.content
    print("******Agent Started Working**********")

    response = JJMCrew(query)
    answer = response.run()

    print("******Agent finished Task************")

    msg = cl.Message(content = answer)
    await msg.send()
from crewai import Crew
from textwrap import dedent

from dotenv import load_dotenv
load_dotenv()

from Tasks import JJMTasks
from Agents import JJMAgents

class JJMCrew():

    def __init__(self,query):
        self.query = query

    def run(self):

        agents = JJMAgents()
        tasks = JJMTasks()

        admin = agents.AdminAgent()
        task = tasks.AnswerTheQuery(self.query)

        crew = Crew(
            agents=[admin], tasks=[task],verbose=True
        )

        result = crew.kickoff()
        return result
    
# if __name__ == "__main__":
#     # query = input(dedent("What you want to ask? : "))
#     query = "How prof gopal naik is related with Jal Jeevan Mission?"
#     answer = JJMCrew(query)
#     result = answer.run()

#     print('\n')
#     print(result)
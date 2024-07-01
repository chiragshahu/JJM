from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from tools.search_tools import SerachTools
from tools.rag_tool import RAGTool
from tools.translation_tool import TranslationTools

llm = ChatGroq(model="llama3-70b-8192")
# llm = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0.3)

class JJMAgents():

    # def Translator(self):
    #     Translator = Agent(
    #         role = "Language expert who is traned in language barrier handling",
    #         goal = "Handling of the language barrier",
    #         backstory = """You are a language expert proficient in Indian languages 
    #         your work is to handle the language of query provided by user as user is indian
    #         citizen from rural area he may ask queries in indian or english plus indian language
    #         your work is to translate it in english and provide it to other agents for detailed 
    #         search and at the end provide answer in english if query is only in english or in 
    #         respective indian language in case query has indian language element. If in query user 
    #         has mentioned the language of answer then provide answer in that language.""",
    #         verbose=True,
    #         function_calling_llm=llm,
    #         allow_delegation=True
    #     )


    def AdminAgent(self):
        Admin = Agent(
            role = "Jal Jeevan Mission Assistant",
            goal = "Providing accurate infirmation related to Jal Jeevan Mission.",
            backstory = """You are appointed by government of india to assist team 
            working on making tape water available to the last rural area of the 
            country""",
            verbose=True,
            llm=llm,
            function_calling_llm=llm,
            allow_delegation=True,
            tools=[SerachTools.search_internet, RAGTool.rag_search_tool, TranslationTools.handle_translation])
        
        # print("Agent Loaded Successfully")
        return Admin

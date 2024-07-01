import os
import json
import requests
from langchain.tools import tool

import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader

import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.chains import LLMChain

class TranslationTools():
    @tool("Handle Translation for indian languages")
    def handle_translation(query):
        'To handle the translation during chat'
        
        def get_translation_chain(query):
            prompt_template = """
            Translate this sentence from indian language to english or viceversa\n\n
            Sentence:\n {query}?\n
            """
            llm = ChatGoogleGenerativeAI(model="gemini-pro")

            prompt = PromptTemplate(template = prompt_template, input_variables = ["query"])
            chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

            return chain
        
        chain = get_translation_chain(query)

        response = chain.run(query=query)
        return response
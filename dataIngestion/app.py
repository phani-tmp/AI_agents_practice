import os 
 
from dotenv import load_dotenv 

from langchain_community.llms import Ollama  
import streamlit as st
load_dotenv()
os.environ["LANGCHAIN_API_KEY"]=os.getenv("Langchain_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("Langchain_Project") 

# from langchain_text_splitters import RecursiveCharacterTextSplitter 
# from langchain_community.document_loaders import PyPDFLoader 
# text_splitter = RecursiveCharacterTextSplitter(
#     # Set a really small chunk size, just to show.
#     chunk_size=1000,
#     chunk_overlap=20,
#     length_function=len,
#     is_separator_regex=False,separators=[
#         "\n\n",
#         "\n",
#         " ",
#         ".",
#         ",",
#         "\u200b",  # Zero-width space
#         "\uff0c",  # Fullwidth comma
#         "\u3001",  # Ideographic comma
#         "\uff0e",  # Fullwidth full stop
#         "\u3002",  # Ideographic full stop
#         "",
#     ],
# ) 
# from langchain_ollama import OllamaEmbeddings

# embeddings = OllamaEmbeddings(model="deepseek-r1") 
# from langchain_community.vectorstores import FAISS

# db = FAISS.from_documents(texts, embeddings)


llm = Ollama(model="deepseek-r1")  
print(llm)
from langchain.prompts import ChatPromptTemplate  

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an intelligent AI assistant,give answers accordingly"""),
    
    ("human", "{resume_text}")
]) 

from langchain_core.output_parsers import StrOutputParser 
output_parse=StrOutputParser
chain=prompt|llm|output_parse
response=chain.invoke({"human","Hey how should our resume looks like "})
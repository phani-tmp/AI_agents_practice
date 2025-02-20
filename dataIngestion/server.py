from fastapi import FastAPI 
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from langchain_groq import ChatGroq 
import os 
from langserve import add_routes 
from dotenv import load_dotenv 
load_dotenv() 
groq_api_key=os.getenv("GROQ_API_KEY")
model=ChatGroq(model="Qwen-2.5-32b",groq_api_key=groq_api_key)

system_template="Translate the following into {language}"
prompt_template=ChatPromptTemplate.from_messages([
    ('system',system_template),
    ('human','{text}')
])

parser=StrOutputParser() 
chain=prompt_template|model|parser 
app=FastAPI(title='server_test',version="1.0",description='Test chey ra puka') 

add_routes(app,chain,path="/phani") 
@app.post("/translate")
def translate(text: str, language: str):
    """Custom API route instead of `/chain/invoke`"""
    result = chain.invoke({"text": text, "language": language})
    return {"output": result}

if __name__=="__main__":
    import uvicorn 
    uvicorn.run(app,host="localhost",port=8006)
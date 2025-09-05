from langchain_openai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model=ChatGoogleGenerativeAI(model='gpt-4',temperature=0.0,max_completion_tokens=10)
result=model.invoke("what is the capital of india?")
print(result.content)


# factual answer(math, code, facts)-0.0-0.3
# balanced response (gen qa, explanation)
# creating writing, storytelling, jokes-0.0-1.2
# max randomness (wild ideas-barnstorming)-1.5+
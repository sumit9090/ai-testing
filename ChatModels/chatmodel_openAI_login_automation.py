# test_case_generator.py
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load .env if running locally
load_dotenv()

# Get API key from environment (works for both .env and GitHub Secrets)
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ OPENAI_API_KEY not found. Make sure it's set in .env or GitHub Secrets.")

# Connect LLM
openai_llm = ChatOpenAI(model="gpt-4", api_key=api_key)

def generate_test_cases(feature: str):
    query = f"""
    Generate 5 positive and 5 negative test cases for {feature}.
    Format: Test Case ID | Description | Expected Result
    """
    openai_output = openai_llm.invoke(query).content
    
    return {
        "OpenAI": openai_output
    }

if __name__ == "__main__":
    feature = "Login functionality"
    results = generate_test_cases(feature)
    print("=== OpenAI Output ===\n", results["OpenAI"])

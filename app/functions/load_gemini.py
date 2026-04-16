import os
from dotenv import load_dotenv
from google import genai


load_dotenv()

def load_gemini():
    
    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        if(api_key == None):
            raise Exception("API key not found. Please set the GEMINI_API_KEY environment variable.")
    except Exception as e:
        print(e)
        exit(1)

    return genai.Client(api_key=api_key)

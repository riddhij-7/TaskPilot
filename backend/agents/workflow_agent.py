import google.generativeai as genai
from db import write_pattern
import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL = "models/gemini-1.5-flash"  # replace with yours

def detect_workflows(emails):
    prompt = f"""
    You are an AI Workflow Detector.

    Analyze these emails:
    {emails}

    Extract:
    - repeated tasks
    - routines
    - daily/weekly patterns

    Return only clean bullet points as a JSON list.
    """

    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(prompt)
    return response.text

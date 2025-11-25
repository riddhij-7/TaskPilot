import google.generativeai as genai
import os


from db import load_patterns, load_meeting_tasks

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "models/gemini-1.5-flash"

def suggest_automations():
    patterns = load_patterns()
    meetings = load_meeting_tasks()

    prompt = f"""
    Based on user workflows:
    {patterns}

    And meeting action items:
    {meetings}

    Suggest 3-5 automations in JSON:
    {{
      "suggestions": []
    }}
    """

    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(prompt)
    return response.text

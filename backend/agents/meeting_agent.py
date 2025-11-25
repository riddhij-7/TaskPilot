import google.generativeai as genai
import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL = "models/gemini-1.5-flash"

def summarize_meeting(transcript):
    prompt = f"""
    Summarize this meeting in JSON with the structure:
    {{
      "summary": "...",
      "action_items": [],
      "owners": [],
      "deadlines": [],
      "decisions": []
    }}

    Transcript:
    {transcript}
    """

    model = genai.GenerativeModel(MODEL)
    response = model.generate_content(prompt)
    return response.text

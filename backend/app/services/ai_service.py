import os
import requests
import json

def invoke_gemini(prompt: str, json_schema=None):
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError("Backend missing GEMINI_API_KEY configuration.")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {}
    }

    if json_schema:
        body["generationConfig"]["responseMimeType"] = "application/json"
        body["generationConfig"]["responseSchema"] = json_schema

    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, headers=headers, json=body)
    
    if response.status_code != 200:
        raise Exception(f"Gemini API Error: {response.text}")
        
    data = response.json()
    
    try:
        text_content = data['candidates'][0]['content']['parts'][0]['text']
    except (KeyError, IndexError):
        raise Exception("Invalid response structure from Gemini")
        
    if json_schema:
        try:
            return json.loads(text_content)
        except json.JSONDecodeError:
            raise Exception("Gemini did not return valid JSON")
            
    return text_content

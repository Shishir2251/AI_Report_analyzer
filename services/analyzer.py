from openai import OpenAI
from app.config import settings

client = OpenAI()


def analyze_report(text: str):
    prompt = f"""
You are a professional report auditor.

Tasks:
1.Detect report structure (Title, Introduction, Body, Conclusion)
2.Identify missing or weak sections
3.Detect formatting or logical issues
4.Classify overall risk: low/ Moderate/ High
5.Return a JSON response 

Report:
{text}
"""
    
    response= client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
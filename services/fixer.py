from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def fix_report(original_text: str, analysis: dict) -> str:
    prompt = f"""
You are an expert report editor.

Issues detected:
{analysis}

Original report:
{original_text}

Return a corrected, well-structured version of the report.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content

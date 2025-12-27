def compare_reports(reference: str, new_report: str):
    prompt = f"""
Compare Report A with Report B.

Tasks:
1. Detect structural differences
2. Detect missing sections
3. Score similarity (0-100)
4. Highlight critical deviations

Report A (Reference):
{reference}

Report B (New Upload):
{new_report}
"""


    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content
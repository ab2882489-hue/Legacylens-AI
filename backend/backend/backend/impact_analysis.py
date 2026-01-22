from gemini_client import model

def impact_analysis(target_file: str, files: dict) -> str:
    """
    target_file = file to hypothetically change
    files = all files in the codebase {filename: content}
    """

    combined_code = ""
    for name, content in files.items():
        combined_code += f"\n\n--- FILE: {name} ---\n{content}"

    prompt = f"""
You are a senior software architect performing impact analysis.

If the file '{target_file}' is changed, explain:
1. Which other files/functions may break
2. Potential risks and dependencies
3. Suggestions to safely modify

Codebase:
{combined_code}
"""

    response = model.generate_content(prompt)
    return response.text

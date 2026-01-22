from gemini_client import model

def explain_code_file(file_name: str, file_content: str) -> str:
    prompt = f"""
You are a senior software architect.

Explain the following code file in simple but professional terms.
Cover:
1. Purpose of the file
2. Key responsibilities
3. Important risks or dependencies

File name:
{file_name}

Code:
{file_content}
"""

    response = model.generate_content(prompt)
    return response.text

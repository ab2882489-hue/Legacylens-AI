from gemini_client import model

def analyze_multiple_files(files: dict) -> str:
    """
    files = {
        "file1.py": "code...",
        "file2.py": "code..."
    }
    """

    combined_code = ""
    for name, content in files.items():
        combined_code += f"\n\n--- FILE: {name} ---\n{content}"

    prompt = f"""
You are a principal software architect analyzing a legacy system.

Analyze the following files together and explain:
1. Overall system purpose
2. How the files interact
3. Key dependencies
4. Potential risk areas

Codebase:
{combined_code}
"""

    response = model.generate_content(prompt)
    return response.text

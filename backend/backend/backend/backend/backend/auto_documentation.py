import json

def generate_technical_documentation(files: dict) -> str:
    """
    Sends project source code to Gemini to generate comprehensive
    technical documentation for the provided system.
    """

    # Format the file contents into a structured prompt for the model
    files_context = "\n\n".join([f"--- FILE: {name} ---\n{content}" for name, content in files.items()])

    prompt = f"""
    You are a senior software architect. Analyze the following source code and provide 
    comprehensive professional technical documentation.
    
    Source Code:
    {files_context}
    
    The documentation must include the following sections:
    1. System Overview: High-level purpose of the project.
    2. Architecture Explanation: Patterns, design choices, and structural organization.
    3. File Responsibilities: A breakdown of what each individual file does.
    4. Data Flow: Description of how information moves through the system.
    5. Risk Areas: Potential bottlenecks, security concerns, or technical debt.
    
    Output Format: Use clear, hierarchical Markdown.
    """

    try:
        # Utilizing the pre-configured 'model' object
        response = model.generate_content(prompt)
        
        if hasattr(response, 'text'):
            return response.text
        else:
            return "Error: Model response did not contain text content."
            
    except Exception as e:
        return f"An error occurred during documentation generation: {str(e)}"

# Example usage (commented out):
# documentation = generate_technical_documentation({
#     "main.py": "print('hello world')",
#     "utils.py": "def helper(): pass"
# })
# print(documentation)

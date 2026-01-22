import json

def answer_repo_question(question: str, files: dict) -> str:
    """
    Analyzes a codebase and provides architectural-level answers to specific questions
    using the Gemini model.
    """

    # Serialize files into a format that preserves path context
    code_context = ""
    for path, content in files.items():
        code_context += f"\nFILE: {path}\n```\n{content}\n```\n"

    prompt = f"""
    You are a Principal Software Architect. Review the provided codebase and answer the question 
    with high technical density, focusing on system design, patterns, and trade-offs. 
    Do not provide introductory or tutorial-style explanations. 

    CODEBASE CONTEXT:
    {code_context}

    QUESTION:
    {question}

    INSTRUCTIONS:
    - Respond with architectural precision.
    - Reference specific files or modules where applicable.
    - If the answer is not present in the code, state that clearly based on your structural analysis.
    - Use professional, concise language.
    """

    try:
        response = model.generate_content(prompt)
        
        if hasattr(response, 'text'):
            return response.text
        else:
            return "Architecture Analysis Error: The model failed to generate a textual response."
            
    except Exception as e:
        return f"System Fault: Failed to process repository query. Details: {str(e)}"

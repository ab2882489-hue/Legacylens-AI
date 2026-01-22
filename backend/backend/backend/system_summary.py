import json

def generate_system_summary(files: dict) -> str:
    """
    Analyzes the provided source files to generate a high-level executive summary 
    of the system architecture, components, and health.
    """

    # Consolidate file map into a context block for the LLM
    source_context = ""
    for filepath, content in files.items():
        source_context += f"File Path: {filepath}\nContent:\n{content}\n\n"

    prompt = f"""
    You are a Principal Software Architect. Provide an executive-level summary of the following system.
    
    SOURCE CODE CONTEXT:
    {source_context}

    Your summary must be concise and structured with the following sections:
    1. High-Level System Purpose: What is the core business/technical value of this codebase?
    2. Main Components/Modules: Identify the primary functional blocks and their roles.
    3. Overall Architecture Style: (e.g., Microservices, Monolithic, Event-Driven, Layered, etc.)
    4. Key Risks and Strengths: A balanced view of technical debt vs. architectural robustness.

    TONE: Executive, professional, and direct. Avoid jargon where a business outcome description is clearer.
    """

    try:
        # Utilizing the pre-configured 'model' object available in the environment
        response = model.generate_content(prompt)
        
        if hasattr(response, 'text'):
            return response.text
        else:
            return "Error: The model was unable to generate a text-based summary."
            
    except Exception as e:
        return f"System Summary Generation Failed: {str(e)}"

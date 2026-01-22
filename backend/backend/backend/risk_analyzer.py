import json

def analyze_system_risks(files: dict) -> str:
    """
    Evaluates the provided codebase for architectural risks, technical debt, 
    and maintainability issues using the Gemini model.
    """

    # Aggregating codebase into a structured prompt context
    system_manifest = ""
    for filename, content in files.items():
        system_manifest += f"\n--- SOURCE START: {filename} ---\n{content}\n--- SOURCE END ---\n"

    prompt = f"""
    You are a Senior Software Architect specializing in legacy systems and risk mitigation. 
    Perform a deep-dive structural analysis on the following codebase to identify critical vulnerabilities 
    and technical debt.

    CODEBASE:
    {system_manifest}

    ANALYSIS REQUIREMENTS:
    Provide a professional, structured report covering:
    1. High-Risk Files: Identify files with excessive complexity or critical failure points.
    2. Tight Coupling Areas: Locate modules that are overly interdependent, hindering modularity.
    3. Maintainability Concerns: Highlight areas with poor readability, lack of abstraction, or "spaghetti" logic.
    4. Refactoring Suggestions: Provide prioritized, actionable strategies to improve system health.

    Tone: Objective, authoritative, and focused on long-term system stability.
    Format: Clear Markdown headers with bulleted technical insights.
    """

    try:
        response = model.generate_content(prompt)
        
        if hasattr(response, 'text'):
            return response.text
        else:
            return "Risk Analysis Failure: Model returned no readable text."
            
    except Exception as e:
        return f"Architectural Audit Interrupted: {str(e)}"

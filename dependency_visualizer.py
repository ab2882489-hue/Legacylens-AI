from gemini_client import model

def generate_dependency_graph(files: dict) -> dict:
    """
    files = { "file1.py": "code...", "file2.py": "code..." }
    Returns a dependency graph in JSON format:
    {
        "nodes": ["file1.py", "file2.py"],
        "edges": [["file1.py", "file2.py"], ...]
    }
    """

    combined_code = ""
    for name, content in files.items():
        combined_code += f"\n\n--- FILE: {name} ---\n{content}"

    prompt = f"""
You are a senior software architect.

From the following files, generate a dependency graph showing:
- Nodes: each file
- Edges: if one file depends on another
Return the result in strict JSON format with "nodes" and "edges" keys.

Files:
{combined_code}
"""

    response = model.generate_content(prompt)

    # Parse JSON safely
    import json
    try:
        graph = json.loads(response.text)
    except:
        graph = {"nodes": list(files.keys()), "edges": []}

    return graph

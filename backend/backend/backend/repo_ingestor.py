import os
from pathlib import Path

def ingest_repository(root_dir: str, max_file_size_kb: int = 512) -> dict[str, str]:
    """
    Recursively reads text-based files from a directory, skipping binaries and large files.
    
    Args:
        root_dir: Path to the repository root.
        max_file_size_kb: Threshold to skip large files (default 512KB).

    Returns:
        Dictionary mapping relative file paths to their string content.
    """
    repo_data = {}
    base_path = Path(root_dir).resolve()

    if not base_path.exists() or not base_path.is_dir():
        raise ValueError(f"Invalid directory path: {root_dir}")

    # Common directories and extensions to ignore
    ignore_list = {'.git', '.venv', '__pycache__', 'node_modules', '.DS_Store', '.idea', '.vscode'}
    binary_extensions = {'.pyc', '.exe', '.dll', '.so', '.o', '.bin', '.jpg', '.png', '.gif', '.pdf', '.zip', '.tar', '.gz'}

    for root, dirs, files in os.walk(base_path):
        # In-place modification of dirs to skip ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_list]

        for file in files:
            file_path = Path(root) / file
            
            # Skip by extension
            if file_path.suffix.lower() in binary_extensions:
                continue

            try:
                # Skip by size
                if file_path.stat().st_size > (max_file_size_kb * 1024):
                    continue

                # Read content
                # relative_to handles the mapping for the dictionary key
                rel_path = str(file_path.relative_to(base_path))
                
                with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                    content = f.read()
                    repo_data[rel_path] = content

            except (PermissionError, OSError) as e:
                print(f"Warning: Could not read {file_path}. Error: {e}")
                continue

    return repo_data

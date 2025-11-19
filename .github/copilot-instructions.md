# Copilot Instructions for HeidyDB-Ejercicios-de-Codewar-med

## Project Overview
This repository contains a collection of Python scripts, each solving a distinct coding challenge, primarily from Codewars. There is no central application or shared architecture; each file is self-contained and named to reflect the problem it solves.

## File Structure & Naming
- Each `.py` file in the root directory corresponds to a single exercise.
- Filenames use a pattern: `[number]_[short_problem_description].py` (e.g., `25_hamming_numb.py`).
- There is no main entry point or shared module structure.

## Developer Workflow
- **No build process**: Scripts are plain Python and can be run directly.
- **Testing**: There are no formal test files or frameworks. To test a solution, run the script manually and inspect output.
- **Debugging**: Use print statements or Python debuggers (`pdb`) within individual scripts.
- **Dependencies**: No external packages are required; all scripts use only the Python standard library.

## Coding Patterns & Conventions
- Each script is standalone; avoid cross-file imports.
- Functions are usually defined at the top level, with problem-specific names.
- Input/output is handled via function arguments and return values, not user input.
- Scripts are intended for educational purposes and may prioritize clarity over performance.

## Example
File: `25_hamming_numb.py`
```python
# Returns the nth Hamming number
def hamming(n):
    # ...implementation...
    return result
```

## Key Directories & Files
- All important code is in the root directory as `.py` files.
- No configuration, requirements, or documentation files are present by default.

## Guidance for AI Agents
- When adding new exercises, follow the existing filename pattern and keep solutions self-contained.
- Do not introduce dependencies or shared modules unless explicitly requested.
- Document the function with a brief comment describing its purpose.
- If updating an existing file, preserve the standalone nature and naming conventions.

---
If any section is unclear or missing, please provide feedback to improve these instructions.

# Copilot Instructions for AI Agents

## Project Overview
This codebase is organized into two main directories:
- `binaries/`: Contains utility scripts, e.g., `hamara`, which performs custom binary manipulations and bitwise operations.
- `password/`: Contains password-related logic, e.g., `password_cheack.py` (note: spelling is project-specific).

## Key Patterns & Conventions
- **Custom Binary Manipulation**: The script `binaries/hamara` demonstrates a unique approach to binary conversion and bitwise operations, including:
  - Manual conversion of integers to binary strings with a fixed bit length.
  - Bitwise inversion using string replacement (e.g., '1'→'0', '0'→'1').
  - Custom binary addition (add one) implemented via string manipulation.
- **Error Handling**: Instead of exceptions, error states are returned as strings (e.g., "Error: number too large for given bit length").
- **Naming**: Some filenames and function names use non-standard or project-specific spelling (e.g., `password_cheack.py`, `memir_le_binar`).

## Developer Workflows
- **Running Scripts**: Scripts are intended to be run directly (e.g., `python binaries/hamara`), and expect interactive input from the user.
- **No Standard Build/Test**: There are no build systems, test frameworks, or automation scripts present. Manual execution and inspection are the primary workflow.
- **Windows Environment**: The project is developed for Windows, with PowerShell as the default shell.

## Integration & Dependencies
- **No External Dependencies**: All logic is implemented in pure Python, with no third-party packages or requirements files.
- **No Cross-Component Communication**: Each script is standalone; there is no inter-process or inter-script communication.

## Examples
- To convert a number to binary with a custom bit length:
  ```python
  memir_le_binar(5, 8)  # returns '00000101'
  ```
- To invert a binary string:
  ```python
  binary_numtemp = binary_numog.replace('1', '5').replace('0', '1').replace('5', '0')
  ```

## Recommendations for AI Agents
- Respect project-specific naming and error handling conventions.
- When adding new scripts, follow the standalone pattern and avoid introducing external dependencies unless necessary.
- Document any new workflows or conventions in this file for future agents.

---
_Last updated: 2025-11-18_

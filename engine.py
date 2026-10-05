import re
import ollama
import sys

SYSTEM_PROMPT = """You are an expert Competitive Programming Socratic Mentor.
Your goal is to help students solve algorithmic problems (e.g., Dynamic Programming, Graphs) by guiding them to the solution.
You MUST NEVER write any C++, Java, Python, or any other code implementations for the user.
Instead, analyze constraints, suggest data structures, ask guiding questions, and explain algorithms conceptually.
If the user asks for code, strictly refuse and offer to explain the logic instead."""

def parse_constraints(problem_statement):
    """
    Parses constraints from the problem description and suggests a target time complexity.
    """
    # Normalize string to make regex easier (lowercase, remove commas)
    text = problem_statement.lower().replace(",", "")
    
    # Regex-based heuristics for constraints
    if re.search(r'(10\^8|10\^7|10000000)', text):
        return "O(N)"
    elif re.search(r'(10\^5|10\^6|100000)', text):
        return "O(N log N) or O(N)"
    elif re.search(r'(10\^4|10000)', text):
        return "O(N^1.5) or O(N log N)"
    elif re.search(r'(10\^3|1000)', text):
        return "O(N^2)"
    elif re.search(r'(<= 500|<= 100\b)', text):
        return "O(N^3)"
    elif re.search(r'(<= 20|<= 25)', text):
        return "O(2^N) or O(N!)"
    
    return "Unknown (analyze the constraints carefully to determine the required time complexity)"

def harness_interceptor(text):
    """
    Inspects the LLM's response for markdown code blocks and replaces them.
    """
    # Regex to match markdown code blocks (```...```)
    pattern = r'```[\s\S]*?```'
    replacement = "> [Harness Intercept: Code generation blocked to preserve learning]"
    return re.sub(pattern, replacement, text)

def get_multiline_input(prompt_text):
    """Helper to get multi-line input from the user."""
    print(prompt_text)
    lines = []
    while True:
        try:
            line = input()
            if not line.strip():
                break
            if line.strip().lower() in ['exit', 'quit']:
                sys.exit(0)
            lines.append(line)
        except EOFError:
            break
    return "\n".join(lines)

def main():
    print("=====================================================")
    print("   Competitive Programming Hint Engine (AI Mentor)   ")
    print("=====================================================")
    print("Type 'exit' or 'quit' at any prompt to stop.\n")
    
    # We will use gemma2:2b by default, but it can be changed to llama3.2:1b
    MODEL_NAME = 'gemma2:2b'
    
    while True:
        print("-" * 50)
        problem_statement = get_multiline_input("Please paste the Problem Statement (Enter an empty line to finish, or type 'exit'):")
        if not problem_statement.strip():
            continue
            
        stuck_state = get_multiline_input("\nWhere are you stuck? What have you tried so far? (Enter an empty line to finish):")
        
        print("\n[Engine] Analyzing constraints...")
        target_complexity = parse_constraints(problem_statement)
        print(f"[Engine] Suggested Target Time Complexity based on constraints: {target_complexity}\n")
        
        # Construct the user message
        user_message = f"Problem Statement:\n{problem_statement}\n\nConstraints Time Complexity Hint: {target_complexity}\n\nUser is stuck at:\n{stuck_state}\n\nPlease provide a Socratic hint."
        
        print(f"[Engine] Asking local AI mentor ({MODEL_NAME}) - this may take a moment...\n")
        
        try:
            response = ollama.chat(
                model=MODEL_NAME,
                messages=[
                    {'role': 'system', 'content': SYSTEM_PROMPT},
                    {'role': 'user', 'content': user_message}
                ]
            )
            
            raw_output = response['message']['content']
            safe_output = harness_interceptor(raw_output)
            
            print("=== MENTOR RESPONSE ===")
            print(safe_output)
            print("=======================\n")
            
        except Exception as e:
            print(f"[Engine Error] Could not communicate with Ollama.")
            print(f"Make sure the Ollama server is running and the model '{MODEL_NAME}' is pulled.")
            print(f"Error details: {e}\n")

if __name__ == "__main__":
    main()

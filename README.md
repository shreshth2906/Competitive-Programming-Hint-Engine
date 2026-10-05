# 🧠 Competitive Programming Hint Engine

> A strictly Socratic, 100% local AI mentor designed to help students master Data Structures and Algorithms without the temptation of copy-pasting code.

## 🌟 The "Why"

This project was built for the **Hacktoberfest 2026 Weekend Challenge** under the theme **"Build for a Friend"**. 
When preparing for technical placements, the biggest trap students fall into is relying on AI to write the code for them. True learning happens when you struggle with the logic, not when you copy-paste the syntax. I built this tool for a friend to provide guidance, suggest data structures, and analyze time complexities—all while strictly refusing to write the actual implementation. 

## ✨ Key Features

- **Socratic Mentorship**: Analyzes your approach and asks guiding questions instead of spoon-feeding answers.
- **Constraint Pre-Parser**: Automatically reads problem constraints (e.g., $10^5$) and suggests the target time complexity before passing context to the AI.
- **Regex Interceptor**: A strict harness that actively blocks the AI from outputting any markdown code blocks (C++, Java, Python, etc.), forcing conceptual learning.
- **100% Offline & Private**: Powered by local open-weight models (`gemma2:2b` or `llama3.2:1b`), ensuring zero internet dependency, zero API costs, and complete privacy.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.x**
- **Ollama**: Download and install from [ollama.com](https://ollama.com/download)

## 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shreshth2906/Competitive-Programming-Hint-Engine.git
   cd Competitive-Programming-Hint-Engine
   ```

2. **Install the required Python library**:
   ```bash
   python -m pip install -r requirements.txt
   ```

3. **Pull the local AI model via Ollama**:
   *Make sure the Ollama application is running in the background.*
   ```bash
   ollama pull gemma2:2b
   ```

4. **Run the Hint Engine**:
   ```bash
   python engine.py
   ```

## 💻 Example Usage

```text
=====================================================
   Competitive Programming Hint Engine (AI Mentor)   
=====================================================
Type 'exit' or 'quit' at any prompt to stop.

--------------------------------------------------
Please paste the Problem Statement (Enter an empty line to finish, or type 'exit'):
> Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. Constraints: 2 <= nums.length <= 10^4

Where are you stuck? What have you tried so far? (Enter an empty line to finish):
> I tried a nested loop but it gives Time Limit Exceeded.

[Engine] Analyzing constraints...
[Engine] Suggested Target Time Complexity based on constraints: O(N^1.5) or O(N log N)

[Engine] Asking local AI mentor (gemma2:2b) - this may take a moment...

=== MENTOR RESPONSE ===
It looks like your O(N^2) brute-force solution is too slow for N = 10^4. We need to optimize this.

Instead of iterating through all pairs, what if we could look up the required complement (i.e., `target - current_number`) instantly? 

Is there a data structure that allows for near O(1) lookups? Think about how you could store the numbers you've seen so far.
=======================
```

*(Note: If the AI ever attempts to output code, it is immediately replaced with `> [Harness Intercept: Code generation blocked to preserve learning]`)*

## 📄 License

This project is licensed under the MIT License.

# Terminal-Based Quiz Application (Python)

An interactive, command-line quiz application built in Python that presents multiple-choice questions (MCQs), handles user inputs dynamically, tracks scores, and evaluates performance.

This project focuses on core programming concepts such as collection data structures, dictionary parsing, string sanitization, and index-based logic evaluation.


## Features & Technical Highlights

* Structured Data Storage: Questions, multiple-choice options, and correct answers are cleanly organized inside a list of nested dictionaries.
* Index Tracking with enumerate(): Uses Python's built-in enumerate() function to simultaneously extract the loop index and object values, allowing dynamic question numbering.
* Robust Input Validation: Implements string sanitization methods like .strip().upper() to ensure trailing spaces or lowercase entries from users don't break the validation logic.
* Score Evaluation Matrix: Dynamically calculates the final score relative to the total number of questions processed at runtime.


## How To Run Locally

1. Clone the Project:
git clone https://github.com/iaryaguptaa/quiz-application-python.git

2. Navigate and Run:
cd quiz-application-python
python main.py

3. Play: Read the question, type your option (A, B, C, or D), and check your final score at the end of the game!


## Key Learnings
* Iterating through complex, nested data structures (List of Dictionaries).
* Utilizing enumerate() for generating clean user-facing index counters.
* Handling conditional string cleaning to prevent input evaluation bugs.
* Iterating through complex, nested data structures (List of Dictionaries).
* Utilizing enumerate() for generating clean user-facing index counters.
* Handling conditional string cleaning to prevent input evaluation bugs.

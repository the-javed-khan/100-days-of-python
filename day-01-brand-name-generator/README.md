# Day 01 – Python Basics

---------------------------------------------------------------------------

## Task 01 – Printing

### Description
Use what you learnt to print out the words "Hello world!" with Python code.

### What I Fixed / Learned in Practice
- `print()` must be written exactly (case-sensitive).
- Text must be inside quotes.
- Parentheses are required: `print("text")`.
- Even a missing quote causes a SyntaxError.

---------------------------------------------------------------------------

## Task 02 – Printing Multiple Lines

### Description
Add `print(` in front of each line.
Add `)` at the end of each line.
Add double quotes around the text.
Do not change anything inside the text.

### What I Fixed / Learned in Practice
- Python does not automatically print text — every line needs `print()`.
- Strings must start and end with double quotes.
- Parentheses must match properly.
- Indentation matters (extra spaces can cause errors).
- Python is strict — small syntax mistakes break execution.

---------------------------------------------------------------------------

## Task 03 – Inputs

### Description
Learn to use the `input()` function to collect user input and use it within a print statement.
Update the code to add an exclamation mark so the output becomes:

Hello Name!

Example:
Hello Angela!

### What I Fixed / Learned in Practice
- `input()` collects user input as a string.
- The value returned by `input()` can be concatenated with other strings.
- String concatenation requires explicit spaces (" ").
- Variables help store input for reuse.
- Without adding `"!"` explicitly, Python will not add it automatically.
- Order of concatenation affects final output formatting.

---------------------------------------------------------------------------

## Task 04 – Variables and Length

### Description
Use the `len()` function to print the number of characters in the user’s input.
Then split the logic into variables.

### What I Fixed / Learned in Practice
- `len()` returns the number of characters in a string.
- `input()` always returns a string.
- Everything can be written in one line, but readability improves with variables.
- Variables store values for reuse.
- Variable names must be meaningful.
- Order of execution matters when assigning and printing values.

### Additional Challenge – Variable Swapping

### Description
Swap the contents of two variables without directly typing their values.

### What I Fixed / Learned in Practice
- Variables store references to values.
- A temporary variable is needed to avoid losing data.
- Order of reassignment is critical.
- If values are overwritten without a temporary variable, data is lost.

---------------------------------------------------------------------------

## Variable Naming

### What I Learned in Practice
- Variable names must not contain spaces.
- Variable names cannot start with numbers.
- Reserved keywords like `print` or `input` cannot be used as variable names.
- Descriptive names improve readability.
- Using simple and clear names reduces errors.

---------------------------------------------------------------------------

## Mini Project – Band Name Generator

### Description
Create a program that:
- Greets the user.
- Collects two inputs.
- Combines them into a final output string.

### What I Fixed / Learned in Practice
- How to store input in variables.
- How to combine multiple variables in one print statement.
- Importance of spacing when concatenating strings.
- Using \n improves input formatting.
- Order of statements affects user experience.
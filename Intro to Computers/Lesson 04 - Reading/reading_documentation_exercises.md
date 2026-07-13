# Reading Online Documentation

Hands-On exercises for learning to navigate and extract information from online technical documentation.

- [Reading Online Documentation](#reading-online-documentation)
  - [Hands-On #2: Navigating Technical Documentation](#hands-on-2-navigating-technical-documentation)
    - [Prerequisites](#prerequisites)
    - [Exercise 1: Understanding Documentation Structure](#exercise-1-understanding-documentation-structure)
    - [Exercise 2: Scavenger Hunt - Python Official Docs](#exercise-2-scavenger-hunt---python-official-docs)
    - [Exercise 3: Comparing Documentation Styles](#exercise-3-comparing-documentation-styles)
    - [Exercise 4: Library Documentation Deep Dive](#exercise-4-library-documentation-deep-dive)
    - [Exercise 5: Reading API Documentation](#exercise-5-reading-api-documentation)
    - [Exercise 6: Finding Version-Specific Information](#exercise-6-finding-version-specific-information)
    - [Exercise 7: Using Search Effectively](#exercise-7-using-search-effectively)
    - [Exercise 8: Understanding Code Examples](#exercise-8-understanding-code-examples)
    - [Exercise 9: Research Challenge](#exercise-9-research-challenge)
    - [Stretch: Cross-Language Documentation Comparison](#stretch-cross-language-documentation-comparison)
  - [Summary](#summary)


## Hands-On #2: Navigating Technical Documentation

**Goal**: Learn to navigate online documentation websites, find specific information quickly, and extract the knowledge needed to solve programming problems.

Reading documentation is like using a reference library - you need to know where to look, how to search, and how to interpret what you find. This skill is essential for working with any programming language or library.

### Prerequisites

You'll need:
- A web browser
- Internet connection
- A text editor or notebook to record your answers

**Create a document to track your findings:**

```bash
mkdir reading_docs
cd reading_docs
```

Create a file called `documentation_notes.md` or `documentation_notes.txt` to record your answers.

---

### Exercise 1: Understanding Documentation Structure

**Goal**: Recognize the common structure of technical documentation sites.

**Visit these three documentation sites:**

1. **Python Official Docs**: https://docs.python.org/3/
2. **Requests Library**: https://requests.readthedocs.io/
3. **FastAPI**: https://fastapi.tiangolo.com/

**For each site, identify and document:**

**Documentation Components:**

1. **Navigation/Table of Contents** - Where is it? (Left sidebar, top menu, etc.)
2. **Search Bar** - Where is it located?
3. **Main Sections** - What are the top-level categories? (e.g., Tutorial, API Reference, Guide)
4. **Version Selector** - Can you change which version of the docs you're viewing?
5. **Code Examples** - Are there syntax-highlighted code blocks?
6. **"See Also" or Related Links** - Do pages link to related topics?

**Complete this table in your notes:**

```
| Feature           | Python Docs | Requests Docs | FastAPI Docs |
| ----------------- | ----------- | ------------- | ------------ |
| Nav Location      |             |               |              |
| Search Location   |             |               |              |
| Has Tutorial?     |             |               |              |
| Has API Ref?      |             |               |              |
| Version Selector? |             |               |              |
```

**Questions to answer:**

1. Which documentation site do you find easiest to navigate? Why?
2. What elements do all three sites have in common?
3. Which site has the most code examples on the homepage?

✅ *Check*: You can identify the key navigation elements of any documentation site.

**Hint**: Most documentation follows a pattern: Tutorial/Guide → User Guide → API Reference → Examples.

---

### Exercise 2: Scavenger Hunt - Python Official Docs

**Goal**: Practice finding specific information quickly in large documentation sites.

**Visit**: https://docs.python.org/3/

**Find the answers to these questions using ONLY the official documentation:**

1. **Library Reference Hunt:**
   - Navigate to the Library Reference
   - Find the `json` module documentation
   - What function converts a Python object to a JSON string?
   - What parameter controls indentation in the output?

2. **Function Signature Hunt:**
   - Find the documentation for the built-in `sorted()` function
   - What page is it on? (Tutorial, Library Reference, etc.)
   - How many parameters does it have?
   - What is the default value of the `reverse` parameter?

3. **String Methods Hunt:**
   - Find the string methods documentation
   - Which method removes whitespace from both ends of a string?
   - Which method checks if a string starts with a specific prefix?
   - Can you find an example showing how to use `str.split()`?

4. **Exception Hunt:**
   - Find the list of built-in exceptions
   - What exception is raised when you divide by zero?
   - What's the difference between `ValueError` and `TypeError`?

5. **Tutorial Navigation:**
   - Find the Python Tutorial section
   - Which section covers "Data Structures"?
   - Can you find information about list comprehensions?

**Document your findings:**

```
Exercise 2 - Scavenger Hunt Answers:

1. JSON module:
   - Function to convert to JSON: 
   - Indentation parameter: 
   
2. sorted() function:
   - Found on page: 
   - Number of parameters: 
   - Default for reverse: 

... (continue for all questions)
```

**Time yourself**: How long did it take to find all answers?

✅ *Check*: You found all answers using only docs.python.org (no Google!).

**Hint**: Use the search bar when you can't find something in the table of contents. Try searching for the exact function or module name.

---

### Exercise 3: Comparing Documentation Styles

**Goal**: Understand that different projects document differently, but you can extract the same information.

**Compare how these libraries document the same concept: making HTTP requests.**

**Visit and compare:**

1. **Python's urllib**: https://docs.python.org/3/library/urllib.request.html
2. **Requests library**: https://requests.readthedocs.io/
3. **httpx library**: https://www.python-httpx.org/

**For each library, find:**

**Making a Simple GET Request:**

1. Find an example of making a basic GET request
2. Copy the minimal code example
3. How many lines of code is the example?
4. Is there a "Quick Start" or "Getting Started" section?

**Documentation Quality Comparison:**

```
| Aspect                     | urllib | Requests | httpx |
| -------------------------- | ------ | -------- | ----- |
| Quick Start exists?        |        |          |       |
| Simple GET example lines   |        |          |       |
| Code examples highlighted? |        |          |       |
| Explains response object?  |        |          |       |
| Has tutorial section?      |        |          |       |
```

**Answer these questions:**

1. Which library has the simplest/shortest example for making a GET request?
2. Which documentation explains concepts the most clearly?
3. Which documentation has the most code examples?
4. If you were a beginner, which documentation would you prefer? Why?

**Real-world skill**: When choosing between libraries, documentation quality matters!

✅ *Check*: You can compare documentation across different libraries and identify which is more user-friendly.

**Hint**: Good documentation often has a "Quick Start" that gets you coding within minutes. Look for this first!

---

### Exercise 4: Library Documentation Deep Dive

**Goal**: Learn to extract comprehensive information about a specific function or class from library documentation.

**Choose the Requests library**: https://requests.readthedocs.io/

**Task: Learn everything about `requests.get()` from the documentation alone.**

**Navigate and answer:**

1. **Finding the Function:**
   - Use the search or navigation to find `requests.get()`
   - What section is it in? (API, User Guide, etc.)

2. **Function Signature:**
   - What parameters does `requests.get()` accept?
   - Which parameters are required?
   - Which are optional?

3. **Return Value:**
   - What object does it return?
   - What attributes/methods does the response object have?
   - How do you get the response body as text?
   - How do you get the HTTP status code?

4. **Examples:**
   - Find at least 2 different examples of using `requests.get()`
   - What's an example showing how to pass query parameters?
   - What's an example showing how to handle authentication?

5. **Related Information:**
   - What other HTTP methods are available? (POST, PUT, etc.)
   - Can you find information about handling errors/exceptions?
   - Is there a section about timeouts?

**Write a summary:**

```
requests.get() Documentation Summary:

Location in docs: 
Required parameters: 
Optional parameters: 
Returns: 
Common use cases:
Related functions:
```

**Practical Application:**

Using ONLY the information from the documentation, write code that:
- Makes a GET request to `https://api.github.com/users/github`
- Prints the status code
- Prints the response as JSON

✅ *Check*: You could use `requests.get()` effectively without any prior experience, just from reading the docs.

**Hint**: Look for both the API reference (detailed parameter info) AND the user guide (examples and explanations).

---

### Exercise 5: Reading API Documentation

**Goal**: Learn to read REST API documentation and understand how to make API calls.

**Visit a public API documentation site:**

**Choose one:**
- **JSONPlaceholder**: https://jsonplaceholder.typicode.com/
- **OpenWeather API**: https://openweathermap.org/api
- **GitHub API**: https://docs.github.com/en/rest

**For your chosen API, answer:**

**API Structure:**

1. **Base URL**: What is the base URL for API requests?
2. **Endpoints**: List 3 available endpoints
3. **Authentication**: Does the API require authentication? How?

**Specific Endpoint Analysis:**

Pick one endpoint and document:

```
Endpoint: 
HTTP Method: (GET, POST, etc.)
Full URL: 
Required Parameters:
Optional Parameters:
Response Format: (JSON, XML, etc.)
Example Response:
```

**Making a Request:**

1. Can you find an example of a complete API request?
2. What headers are required?
3. What does a successful response look like?
4. What status code indicates success?

**Error Handling:**

1. What status codes indicate errors?
2. What does a 404 error mean for this API?
3. Is there information about rate limiting?

**Practical Task:**

Using the documentation, write the URL you would visit in a browser to:
- Get a specific resource (user, post, weather data, etc.)
- Include any required query parameters

Example:
```
API: JSONPlaceholder
Task: Get post with ID 1
URL: https://jsonplaceholder.typicode.com/posts/1
```

✅ *Check*: You can read API documentation and construct valid API requests.

**Hint**: API docs usually have a "Try It" or "Example" section - these are gold for understanding the expected format!

---

### Exercise 6: Finding Version-Specific Information

**Goal**: Learn to navigate version changes and find information for specific versions.

**Visit Python Docs**: https://docs.python.org/3/

**Version Navigation:**

1. **Current Version**: What version of Python does the documentation default to?
2. **Version Selector**: Where can you change the version? (Usually top-left or in URL)
3. **Change Version**: Switch to Python 3.8 documentation (or an older version)

**Find Version-Specific Features:**

**Task 1: F-strings**
- When were f-strings introduced to Python?
- Search the "What's New" section
- Which Python version added f-strings?

**Task 2: The Walrus Operator (:=)**
- What Python version introduced the walrus operator?
- Find it in the "What's New in Python X.X" section
- What is its official name?

**Task 3: Type Hints**
- When were type hints introduced?
- Find an example of type hint syntax
- Have they changed between versions?

**Comparing Versions:**

Compare the `dict.update()` documentation between Python 3.8 and Python 3.11:
- Is the functionality the same?
- Are there any new features or parameters?
- Do the examples differ?

**Document your findings:**

```
Version-Specific Features:

F-strings introduced in: Python X.X
Walrus operator introduced in: Python X.X
Type hints introduced in: Python X.X

Why this matters:
```

✅ *Check*: You can identify which Python version introduced a feature and navigate version-specific documentation.

**Hint**: The "What's New in Python X.X" section is your best friend for understanding version changes!

---

### Exercise 7: Using Search Effectively

**Goal**: Master documentation search features to find information quickly.

**Practice on**: https://docs.python.org/3/

**Search Exercises:**

**1. Search for a Function:**
- Search for: `enumerate`
- How many results appear?
- Which result is the official function documentation?
- Which other pages mention enumerate?

**2. Search for a Concept:**
- Search for: `list comprehension`
- What tutorial page covers this?
- Are there examples in the search results?

**3. Search for Error Messages:**
- Search for: `KeyError`
- Where is the official exception documentation?
- Can you find examples of when it's raised?

**4. Ambiguous Searches:**
- Search for: `format`
- How many different things relate to "format"?
  - String formatting?
  - The `format()` function?
  - Format specifications?
- How do you narrow down to what you want?

**Search Strategy Comparison:**

Try finding information about "how to sort a list" using these strategies:

**Strategy A: Browse** (navigate through table of contents)
- Where did you look?
- How many clicks?
- Time taken:

**Strategy B: Search** (use search bar)
- Search term used:
- First result relevant?
- Time taken:

**Strategy C: External** (Google: "python sort list")
- First result quality:
- Led to official docs?
- Time taken:

**Questions:**

1. Which strategy was fastest?
2. Which strategy gave you the most authoritative answer?
3. When would you use each strategy?

✅ *Check*: You have a strategy for finding information quickly and efficiently.

**Hint**: Use specific terms (function names, error types) for searches. Use browsing for learning concepts.

---

### Exercise 8: Understanding Code Examples

**Goal**: Learn to read and interpret code examples in documentation.

**Visit FastAPI docs**: https://fastapi.tiangolo.com/

**Find the "First Steps" tutorial and answer:**

**Anatomy of Documentation Code Examples:**

```python
# Example from docs (simplified):
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

**For this example, identify:**

1. **Imports**: What is being imported?
2. **Setup/Configuration**: How is the app initialized?
3. **Main Logic**: What does the core function do?
4. **Return Value**: What does it return?

**Understanding Example Context:**

Documentation examples can be:

**Type A: Complete/Runnable**
- Can be copied and run immediately
- Includes all imports
- Has a complete setup

**Type B: Snippet/Partial**
- Shows only the relevant part
- Assumes existing setup
- Requires context from earlier examples

**Exercise: Categorize these examples**

Visit https://requests.readthedocs.io/ and find 3 code examples:

1. Classify each as Complete or Snippet
2. If it's a snippet, what's missing?
3. Could you run it as-is?

**Reading Between the Lines:**

Good documentation examples include:

```python
# 1. Comments explaining WHY
# Download a large file in chunks to save memory
response = requests.get(url, stream=True)

# 2. Error handling (sometimes)
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"Error: {e}")

# 3. Best practices
# Always close your connection
with requests.get(url) as response:
    data = response.json()
```

**Find examples in documentation that show:**
- Error handling
- Best practices
- Common pitfalls to avoid

✅ *Check*: You can distinguish between complete examples and snippets, and understand what's implied.

**Hint**: If an example doesn't have imports, it's probably a snippet showing only the changed part!

---

### Exercise 9: Research Challenge

**Goal**: Combine all documentation reading skills to solve a real problem.

**Scenario**: You need to build a small Python script that:
1. Fetches data from a public API (JSONPlaceholder)
2. Parses the JSON response
3. Saves specific fields to a file
4. Handles errors gracefully

**Your Task**: Using ONLY official documentation, research and answer:

**Research Questions:**

**Part 1: Making HTTP Requests**
- Which library should you use? (Built-in urllib or third-party requests?)
- How do you make a GET request?
- How do you handle connection errors?

Documentation to check:
- https://docs.python.org/3/library/urllib.request.html
- https://requests.readthedocs.io/ (if you decide to use it)

**Part 2: Parsing JSON**
- What built-in Python module handles JSON?
- How do you convert JSON text to a Python dictionary?
- How do you handle invalid JSON?

Documentation to check:
- https://docs.python.org/3/library/json.html

**Part 3: File Operations**
- How do you write text to a file in Python?
- What's the best way to ensure files are closed properly?
- How do you handle file write errors?

Documentation to check:
- https://docs.python.org/3/tutorial/inputoutput.html

**Part 4: Error Handling**
- What's the syntax for try/except in Python?
- What exceptions should you catch for network requests?
- What exceptions should you catch for file operations?

Documentation to check:
- https://docs.python.org/3/tutorial/errors.html

**Create a research document:**

```markdown
# API Data Fetcher - Research Notes

## Problem: Fetch data from API and save to file

### Research Findings:

1. HTTP Requests:
   - Library choice: 
   - Function to use: 
   - Error exceptions to handle: 

2. JSON Parsing:
   - Module: 
   - Function to parse: 
   - Error exceptions to handle: 

3. File Writing:
   - Best practice syntax: 
   - Error exceptions to handle: 

4. Error Handling:
   - try/except syntax: 
   - Specific exceptions to catch: 

### Documentation Pages Used:
- 
- 
- 

### Time Spent: ___ minutes
```

**Bonus Challenge:**

Using only your research notes, write the actual code! Can you do it without running it first?

✅ *Check*: You can research a multi-step problem using only official documentation.

**Hint**: This is how professional developers work - research in docs, plan, then code!

---

### Stretch: Cross-Language Documentation Comparison

**Goal**: Recognize that documentation patterns transfer across programming languages.

**Compare documentation for similar concepts across languages:**

**Task: Find how to read a file in different languages**

**Python**: https://docs.python.org/3/
**JavaScript/Node.js**: https://nodejs.org/docs/
**Java**: https://docs.oracle.com/javase/tutorial/

**For each language, find:**

1. Where is file I/O documented?
2. How complex is the basic example?
3. How is the documentation structured?
4. Are there clear examples?

**Document comparison:**

```
| Aspect              | Python | JavaScript | Java |
| ------------------- | ------ | ---------- | ---- |
| Easy to find?       |        |            |      |
| Example complexity  |        |            |      |
| Explanation quality |        |            |      |
| Number of examples  |        |            |      |
```

**Reflection Questions:**

1. Which language has the most beginner-friendly documentation?
2. What makes documentation "good" vs "bad"?
3. Do all documentation sites share common patterns?
4. Can you navigate unfamiliar documentation using skills from this exercise?

✅ *Check*: You recognize that documentation reading is a transferable skill across technologies.

**Hint**: Good documentation is language-agnostic in structure: Tutorial → Guide → Reference.

---

## Summary

You've learned to navigate and extract information from online documentation:

**Key Skills Acquired:**

✅ **Structure Recognition**: Identify common documentation patterns  
✅ **Effective Search**: Find information quickly using search and navigation  
✅ **Version Awareness**: Understand version-specific features and changes  
✅ **Example Interpretation**: Read and understand code examples  
✅ **Comparison Skills**: Evaluate documentation quality across libraries  
✅ **API Documentation**: Read REST API docs and construct requests  
✅ **Research Skills**: Combine multiple documentation sources to solve problems  

**Documentation Reading Strategy:**

1. **Start with structure**: Understand how the docs are organized
2. **Use search wisely**: Specific terms for functions, browsing for concepts
3. **Examples first**: See it in action before reading detailed explanations
4. **Check versions**: Make sure you're reading docs for your version
5. **Multiple sources**: API reference + User guide + Examples = complete picture
6. **Verify with code**: Test what you learned by writing actual code

**Common Documentation Sections:**

- **Getting Started / Quick Start**: Fastest way to get running
- **Tutorial**: Learn by building something
- **User Guide**: Explains concepts and common use cases
- **API Reference**: Detailed function/class documentation
- **Examples / Cookbook**: Common patterns and solutions
- **FAQ**: Frequently asked questions
- **Changelog / What's New**: Version-specific changes

**Best Practices:**

✅ Always check the official documentation first  
✅ Bookmark documentation sites you use frequently  
✅ Read examples to understand usage patterns  
✅ Pay attention to version numbers  
✅ Use search for specific items, browse for learning  
✅ Compare multiple examples to understand edge cases  
✅ Note what you learn for future reference  

**Next Steps:**

- Bookmark key documentation sites (docs.python.org, etc.)
- Practice reading docs BEFORE writing code
- When you get stuck, check docs before Stack Overflow
- Read the "What's New" for each Python version you use
- Explore documentation for libraries you're interested in learning

**Remember**: Good documentation reading is like learning to use a library. The better you know where things are, the faster you can find what you need!

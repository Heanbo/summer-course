# Debugging Techniques

This repository provides a comprehensive overview of common bug types and effective strategies for identifying, isolating, and fixing software errors. 


## 🎯 Lesson Objectives

* Identify and categorize the main families of **software bugs**. 
* Explore various **debugging techniques**, from print statements to interactive tools. 
* Implement **core strategies** to systematically narrow down and resolve issues. 


## 🐞 Common Bug Types

Bugs are often categorized by when they appear and how they affect the program. 

| Bug Category | Description | Examples |
| --- | --- | --- |
| **Syntax / Compile-Time** | Errors that prevent code from running or building. 
| Missing semicolons, bad imports, typos. 
| **Runtime** | Errors that occur during execution, often causing crashes. 
| NullReference, IndexError, memory leaks. 
| **Logic** | The program runs but produces the wrong output. 
| Off-by-one errors, improper branching, business rule mistakes. 


## 🛠️ Debugging Techniques


### 1. Print and Interactive Debugging

- **Print Statements:** Adding logs to see state changes and variable values over time. 
- **Interactive Debugging:** Using breakpoints and watch expressions in an IDE to pause and inspect code. 


### 2. Testing and Isolation

- **Test-Driven Isolation:** Writing a failing test case that reproduces the bug before attempting to fix it. 
- **Minimal Reproducible Examples:** Creating a small, clear snippet of code that demonstrates the issue in isolation. 


### 3. Profiling and Logs

- **Profilers:** Monitoring CPU, memory, and I/O to find performance hotspots or leaks. 
- **Structured Logs:** Centralizing logs and adding IDs or timestamps to correlate events across a system. 


## 🧠 Core Debugging Strategies

Effective debugging requires a systematic approach rather than guesswork. 

1. **RTFE (Read The First Error):** Always carefully read the error message and stack trace first to understand the context. 
2. **Divide-and-Conquer:** Narrow the search space by cutting out sections of code or input until the problem is isolated. 
3. **Hypothesis Testing:** Form a simple theory about what is wrong and run a targeted test to prove or disprove it. 
4. **Validate Rules:** For logic bugs, double-check the intended "business rules" or requirements with stakeholders. 


## 📂 Summary of Tools

- **Linters and Static Analyzers:** For catching syntax and compile-time issues early. 
- **Sanitizers and Lock Timeouts:** For detecting memory problems and concurrency issues like deadlocks. 

# Python File I/O

This repository covers the techniques for interacting with the file system using Python, focusing on the `os` and `pathlib` modules to navigate directories and manipulate file contents. 


## 🎯 Lesson Objectives

* Utilize the **`os` and `pathlib.Path` modules** to navigate a filesystem. 
* Utilize standard Python functions to **manipulate and edit files**. 


## 📂 Navigating the Filesystem

Python provides two primary modules for interacting with the operating system's file structure.


### The `os` Module

The `os` module provides a way to use operating system-dependent functionality like reading or writing to the file system. Many of its functions directly correspond to common Linux terminal commands. 

| Python Function | Linux Equivalent | Description |
| --- | --- | --- |
| `os.getcwd()` | `pwd` | Returns the current working directory. 
| `os.chdir(path)` | `cd path` | Changes the current working directory. 
| `os.listdir('.')` | `ls` | Lists files and directories in the given path. 
| `os.mkdir(path)` | `mkdir path` | Creates a single directory. 
| `os.makedirs(path)` | `mkdir -p path` | Creates nested directories recursively. 
| `os.remove(path)` | `rm path` | Deletes a specific file. 
| `os.rename(src, dst)` | `mv src dst` | Renames or moves a file or directory. 


### The `pathlib` Module

`pathlib` offers an object-oriented approach to handling filesystem paths. It is often considered more intuitive for modern Python development. 

- **Path Joining:** `Path('folder') / 'file.txt'` 
- **Existence Checks:** `p.exists()`, `p.is_file()`, `p.is_dir()` 
- **File Search:** `Path('logs').glob('*.txt')` 


## 📝 Manipulating Files

To read or write data, Python uses a built-in file object created with the `open()` function. 


### Common Actions

- **Opening Files:** It is best practice to use the `with` statement (`with open('file.txt', 'r') as f:`) as it automatically closes the file once the block is finished. 
- **Reading:**
  - `f.read()`: Reads the entire file as a single string. 
  - `f.readlines()`: Reads the file into a list where each element is a line. 
  - **Looping:** You can loop through a file line by line (`for line in f:`) to save memory with large files. 
- **Writing:** `with open('file.txt', 'w') as f: f.write('text')` prepares a file for writing (overwriting existing content). 


## 🛠️ Hands-On Exercises

- **Navigation:** Practice moving through directory structures and listing contents using Python scripts. 
- **File Management:** Create, rename, and delete files and directories programmatically. 

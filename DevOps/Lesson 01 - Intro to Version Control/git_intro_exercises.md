
# Intro to Version Control

- [Intro to Version Control](#intro-to-version-control)
  - [Hands-On #1 Exercises](#hands-on-1-exercises)
    - [Exercise 0:](#exercise-0)
    - [Exercise 1: Initialize a Git Repository](#exercise-1-initialize-a-git-repository)
    - [Exercise 2: Create and Modify a File](#exercise-2-create-and-modify-a-file)
    - [Exercise 3: Stage the File](#exercise-3-stage-the-file)
    - [Exercise 4: Commit the File](#exercise-4-commit-the-file)
    - [Exercise 5: Make a Change and Commit Again](#exercise-5-make-a-change-and-commit-again)
    - [Exercise 6: Commit a Second File](#exercise-6-commit-a-second-file)
  - [Hands-On #2 Exercises](#hands-on-2-exercises)
    - [Exercise 7: View History and Changes](#exercise-7-view-history-and-changes)
    - [Exercise 8: View a Specific Commit](#exercise-8-view-a-specific-commit)
    - [Exercise 9: View Differences Between Commits](#exercise-9-view-differences-between-commits)
    - [Exercise 10: See File History](#exercise-10-see-file-history)
    - [Exercise 11: Check What Changed Before Staging](#exercise-11-check-what-changed-before-staging)
    - [Exercise 12: Check What is Staged](#exercise-12-check-what-is-staged)
  - [Stretch Goals](#stretch-goals)


## Hands-On #1 Exercises

This guide walks you through the basic Git workflow: initializing a repository, making changes, staging, committing, and viewing history.  This uses a series of Linux commands to manipulate the files.  If you are not familiar with Linux commands, you may want to seek out a Linux primer or cheatsheet.  (Example:  https://linuxjourney.com/)

---
### Exercise 0:

**Goal**: Get a working environment for git

1. Open a WSL terminal
2. Verify that `git` is installed by running the command `git --version`
3. If `git` is not installed, install it by running `apt install git -y`


### Exercise 1: Initialize a Git Repository

**Goal**: Create a new directory and initialize it as a Git repository.

**Hint**: Make this directory from inside of your home directory (e.g. `~/git_intro`).

✅ *Check*: Run `ls -la` to verify that a `.git` directory was created.  Git stores all of its tracking information in a series of files in the `.git` directory.

---

### Exercise 2: Create and Modify a File

**Goal**: Create a file and add some content.


✅ *Check*: Run 'ls' to see the created file in your directory. Run `git status` to see the untracked file.  Read the output carefully.  Which branch are you on?  What are "untracked" files?  
INFO: Line 1 Creates the hello.txt file and adds the line "Hello, Git!"  
INFO: Line 2 'cat' is short for concatenate, it chains files together into a single output, in this example, your screen is the default output

---

### Exercise 3: Stage the File

**Goal**: Add the file to the staging area.


✅ *Check*: Run `git status` again and verify that the change is staged.  How is the output of `git status` different than the previous step? You can specify a directory to stage all changes in that directory at once.

---

### Exercise 4: Commit the File

**Goal**: Commit the staged file with a message.

Git keeps a log of all your commits.  Before we make any commits, let's see what the history says.

What does the output show?  Now commit your staged change with a descriptive message.


✅ *Check*: Run `git status` to see the new status, run `git log` to see your first commit.

---

### Exercise 5: Make a Change and Commit Again

**Goal**: Modify the file, stage, and commit the changes.


✅ *Check*: Use `git log` and `cat hello.txt` to verify your commit and file contents.

---

### Exercise 6: Commit a Second File

**Goal**: Check what happens with unstaged files (no commands for you this time!)

Create a second and third file, but only stage and commit the second file.


✅ *Check*: Run `git status` (should show nothing to commit), and `git log --oneline` to see a summary of commits.

---

## Hands-On #2 Exercises

### Exercise 7: View History and Changes

**Goal**: Explore the commit history and file diffs.


✅ *Try*: Use `git show <commit-hash>` to view the details of a specific commit. 

### Exercise 8: View a Specific Commit

**Goal**: Use `git show` to view details of a specific commit.


✅ *Tip*: Replace `<commit-hash>` (it should be 7 characters on the left side) with the short hash from `git log --oneline`.

---

### Exercise 9: View Differences Between Commits

**Goal**: Compare two commits.


✅ *Example*: Compare two specific commits to see what changed between them.

---

### Exercise 10: See File History

**Goal**: View the commit history for a single file.


✅ *Try*: Add `-p` to view diffs in each commit:


---

### Exercise 11: Check What Changed Before Staging

**Goal**: View changes to files before staging.


✅ *Check*: The output will show changes that are unstaged.

---

### Exercise 12: Check What is Staged

**Goal**: View what has been staged before committing.


✅ *Check*: This shows differences between the index (staged area) and the last commit.

---

## Stretch Goals

**Goal**:  Try to recover after a bad change or commit.

Sometimes people do things they don't mean to and commit bad changes.  Try to revert one of your changes and go back to an old commit.

For extra double bonus points, start making changes off of that old commit and see what happens with things like `git log`.
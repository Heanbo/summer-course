# Pair Collaboration Exercise: Git Workflow with Pull Requests
- [Pair Collaboration Exercise: Git Workflow with Pull Requests](#pair-collaboration-exercise-git-workflow-with-pull-requests)
  - [Overview](#overview)
  - [Prerequisites](#prerequisites)
  - [Team Roles](#team-roles)
  - [Part 1: Repository Setup (Partner A)](#part-1-repository-setup-partner-a)
    - [Step 1: Create the Shared Repository](#step-1-create-the-shared-repository)
    - [Step 2: Add Your Partner as a Collaborator](#step-2-add-your-partner-as-a-collaborator)
  - [Part 2: Initial Project Setup (Partner A)](#part-2-initial-project-setup-partner-a)
    - [Step 3: Clone and Set Up Project Structure](#step-3-clone-and-set-up-project-structure)
    - [Step 4: Create Initial Python Script](#step-4-create-initial-python-script)
    - [Step 5: Commit and Push Initial Structure](#step-5-commit-and-push-initial-structure)
  - [Part 3: Clone Repository (Partner B)](#part-3-clone-repository-partner-b)
    - [Step 6: Partner B Clones the Repository](#step-6-partner-b-clones-the-repository)
  - [Part 4: Feature Development (Both Partners - Work Independently)](#part-4-feature-development-both-partners---work-independently)
    - [Partner A: Implement Word Counter Feature](#partner-a-implement-word-counter-feature)
      - [Step 7A: Create Feature Branch](#step-7a-create-feature-branch)
      - [Step 8A: Implement Word Counter Function](#step-8a-implement-word-counter-function)
      - [Step 9A: Test Your Feature](#step-9a-test-your-feature)
      - [Step 10A: Commit Your Changes](#step-10a-commit-your-changes)
      - [Step 11A: Push Your Feature Branch](#step-11a-push-your-feature-branch)
    - [Partner B: Implement Line Reverser Feature](#partner-b-implement-line-reverser-feature)
      - [Step 7B: Create Feature Branch](#step-7b-create-feature-branch)
      - [Step 8B: Implement Line Reverser Function](#step-8b-implement-line-reverser-function)
      - [Step 9B: Test Your Feature](#step-9b-test-your-feature)
      - [Step 10B: Commit Your Changes](#step-10b-commit-your-changes)
      - [Step 11B: Push Your Feature Branch](#step-11b-push-your-feature-branch)
  - [Part 5: Create Pull Requests (Both Partners)](#part-5-create-pull-requests-both-partners)
    - [Step 12: Partner A Creates Pull Request](#step-12-partner-a-creates-pull-request)
    - [Step 13: Partner B Creates Pull Request](#step-13-partner-b-creates-pull-request)
  - [Part 6: Code Review (Switch Roles)](#part-6-code-review-switch-roles)
    - [Step 14: Partner B Reviews Partner A's PR](#step-14-partner-b-reviews-partner-as-pr)
    - [Step 15: Partner A Reviews Partner B's PR](#step-15-partner-a-reviews-partner-bs-pr)
  - [Part 7: Merge Pull Requests](#part-7-merge-pull-requests)
    - [Step 16: Partner A Merges Partner B's PR](#step-16-partner-a-merges-partner-bs-pr)
    - [Step 17: Partner B Merges Partner A's PR](#step-17-partner-b-merges-partner-as-pr)
  - [Part 8: Sync Local Repositories (Both Partners)](#part-8-sync-local-repositories-both-partners)
    - [Step 18: Update Local Main Branch](#step-18-update-local-main-branch)
    - [Step 19: Clean Up Local Feature Branches](#step-19-clean-up-local-feature-branches)
  - [Part 9: Merge Conflict Practice (Advanced - Optional)](#part-9-merge-conflict-practice-advanced---optional)
    - [Step 20: Create Conflicting Changes](#step-20-create-conflicting-changes)
    - [Step 21: Merge First PR](#step-21-merge-first-pr)
    - [Step 22: Resolve Merge Conflict](#step-22-resolve-merge-conflict)
  - [Reflection Questions](#reflection-questions)
  - [Key Takeaways](#key-takeaways)
  - [Extensions (Try on Your Own)](#extensions-try-on-your-own)
  - [Troubleshooting](#troubleshooting)
  - [Congratulations! 🎉](#congratulations-)

## Overview
In this exercise, you'll work with a partner to practice a real-world Git collaboration workflow. You'll create a shared repository, work on separate features, and review each other's code through pull requests.

**Time Required**: 60-90 minutes

---

## Prerequisites
- GitHub account
- Git installed locally
- Python 3 installed
- Basic understanding of Git commands (commit, push, pull, branch)

---

## Team Roles

For this exercise, decide who will be:
- **Partner A** (Repository Owner)
- **Partner B** (Collaborator)

You'll switch responsibilities throughout the exercise, so both partners get practice with all aspects of the workflow.

---

## Part 1: Repository Setup (Partner A)

### Step 1: Create the Shared Repository

1. Go to [GitHub](https://github.com) and log in
2. Click the **+** icon in the top right and select **New repository**
3. Configure your repository:
   - **Repository name**: `file-processor-collab`
   - **Description**: "Collaborative file processing tool"
   - **Visibility**: Public (or Private if you prefer)
   - **Initialize with**: Check ✅ "Add a README file"
   - **Add .gitignore**: Select "Python"
4. Click **Create repository**

✅ *Check*: You should now see your new repository with a README and .gitignore file.

### Step 2: Add Your Partner as a Collaborator

1. In your new repository, click **Settings** (top right tabs)
2. In the left sidebar, click **Collaborators**
3. Click **Add people**
4. Enter **Partner B's** GitHub username or email
5. Click **Add {username} to this repository**

**Partner B**: Check your email and accept the invitation!

✅ *Check*: Partner B should now appear in the collaborators list.

---

## Part 2: Initial Project Setup (Partner A)

**Note**:  You will need to use a classic token to access your partner's repository.

### Step 3: Clone and Set Up Project Structure

Partner A will create the initial project structure:

```bash
# Clone the repository
git clone https://github.com/{YOUR_USERNAME}/file-processor-collab.git
cd file-processor-collab

# Create project structure
mkdir data
touch process_files.py
touch data/sample.txt

# Add some initial content to sample.txt
echo "Hello World
Python is awesome
Git collaboration rocks
We love coding" > data/sample.txt
```

### Step 4: Create Initial Python Script

Create a basic Python script in `process_files.py`:

```python
"""
File Processing Utility
A collaborative project to demonstrate file manipulation in Python
"""

def main():
    """Main entry point for the file processor"""
    print("File Processor v1.0")
    print("Contributors: [Add your names here]")
    print("\nAvailable operations:")
    print("1. Count words")
    print("2. Reverse lines")
    print("3. Convert to uppercase")
    print("4. Find and replace")
    
if __name__ == "__main__":
    main()
```

### Step 5: Commit and Push Initial Structure

```bash
git add .
git commit -m "Initial project setup with basic structure"
git push origin main
```

✅ *Check*: Verify the files appear on GitHub in the repository.

---

## Part 3: Clone Repository (Partner B)

### Step 6: Partner B Clones the Repository

Now Partner B gets a copy of the project:

```bash
# Clone the repository (use YOUR partner's repository URL)
git clone https://github.com/{PARTNER_A_USERNAME}/file-processor-collab.git
cd file-processor-collab

# Verify you have the files
ls -la
cat process_files.py
```

✅ *Check*: Both partners should now have identical copies of the repository locally.

---

## Part 4: Feature Development (Both Partners - Work Independently)

Now both partners will work on different features **at the same time** on separate branches.

---

### Partner A: Implement Word Counter Feature

#### Step 7A: Create Feature Branch

```bash
# Make sure you're on main and up to date
git checkout main
git pull origin main

# Create and switch to a new branch
git checkout -b feature/word-counter
```

#### Step 8A: Implement Word Counter Function

Add this function to `process_files.py` (add it before the `main()` function):

```python
def count_words(filename):
    """
    Count the total number of words in a file.
    
    Args:
        filename (str): Path to the file to process
        
    Returns:
        int: Total word count
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0
```

Update the `main()` function to include a test:

```python
def main():
    """Main entry point for the file processor"""
    print("File Processor v1.0")
    print("Contributors: [Add your names here]")
    print("\nAvailable operations:")
    print("1. Count words")
    print("2. Reverse lines")
    print("3. Convert to uppercase")
    print("4. Find and replace")
    
    # Test word counter
    print("\n--- Testing Word Counter ---")
    word_count = count_words("data/sample.txt")
    print(f"Total words in sample.txt: {word_count}")
```

#### Step 9A: Test Your Feature

```bash
# Test the script
python process_files.py
```

You should see output showing the word count.

#### Step 10A: Commit Your Changes

```bash
git add process_files.py
git commit -m "Add word counter feature with error handling"
```

#### Step 11A: Push Your Feature Branch

```bash
git push origin feature/word-counter
```

✅ *Check*: Your feature branch should now be visible on GitHub.

---

### Partner B: Implement Line Reverser Feature

#### Step 7B: Create Feature Branch

```bash
# Make sure you're on main and up to date
git checkout main
git pull origin main

# Create and switch to a new branch
git checkout -b feature/line-reverser
```

#### Step 8B: Implement Line Reverser Function

Add this function to `process_files.py` (add it before the `main()` function):

```python
def reverse_lines(input_filename, output_filename):
    """
    Reverse the order of lines in a file and save to a new file.
    
    Args:
        input_filename (str): Path to the input file
        output_filename (str): Path to save the reversed content
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(input_filename, 'r') as file:
            lines = file.readlines()
        
        # Reverse the lines
        reversed_lines = lines[::-1]
        
        with open(output_filename, 'w') as file:
            file.writelines(reversed_lines)
        
        print(f"Successfully reversed {len(lines)} lines")
        return True
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
        return False
    except Exception as e:
        print(f"Error processing file: {e}")
        return False
```

Update the `main()` function to include a test:

```python
def main():
    """Main entry point for the file processor"""
    print("File Processor v1.0")
    print("Contributors: [Add your names here]")
    print("\nAvailable operations:")
    print("1. Count words")
    print("2. Reverse lines")
    print("3. Convert to uppercase")
    print("4. Find and replace")
    
    # Test line reverser
    print("\n--- Testing Line Reverser ---")
    success = reverse_lines("data/sample.txt", "data/reversed.txt")
    if success:
        print("Check data/reversed.txt for the result!")
```

#### Step 9B: Test Your Feature

```bash
# Test the script
python process_files.py

# Check the output
cat data/reversed.txt
```

You should see the lines in reverse order.

#### Step 10B: Commit Your Changes

```bash
git add process_files.py
git commit -m "Add line reverser feature with output file creation"
```

#### Step 11B: Push Your Feature Branch

```bash
git push origin feature/line-reverser
```

✅ *Check*: Your feature branch should now be visible on GitHub.

---

## Part 5: Create Pull Requests (Both Partners)

### Step 12: Partner A Creates Pull Request

1. Go to the repository on GitHub
2. You should see a banner saying "**feature/word-counter** had recent pushes"
3. Click **Compare & pull request**
4. Fill out the PR details:
   - **Title**: "Add word counter feature"
   - **Description**: 
     ```
     ## Changes
     - Implemented count_words() function
     - Added error handling for file operations
     - Added test in main() function
     
     ## Testing
     - Tested with sample.txt
     - Verified error handling with non-existent files
     
     @{PARTNER_B_USERNAME} Please review!
     ```
5. Click **Create pull request**

### Step 13: Partner B Creates Pull Request

1. Go to the repository on GitHub
2. You should see a banner saying "**feature/line-reverser** had recent pushes"
3. Click **Compare & pull request**
4. Fill out the PR details:
   - **Title**: "Add line reverser feature"
   - **Description**: 
     ```
     ## Changes
     - Implemented reverse_lines() function
     - Creates output file with reversed line order
     - Added error handling for file operations
     - Added test in main() function
     
     ## Testing
     - Tested with sample.txt
     - Verified output file creation
     
     @{PARTNER_A_USERNAME} Please review!
     ```
5. Click **Create pull request**

✅ *Check*: Both pull requests should now be visible in the "Pull requests" tab.

---

## Part 6: Code Review (Switch Roles)

Now each partner will review the other's code. This is a critical skill in software development!

### Step 14: Partner B Reviews Partner A's PR

1. Go to the **Pull requests** tab
2. Click on Partner A's PR ("Add word counter feature")
3. Click on the **Files changed** tab
4. Review the code:
   - Check for code quality
   - Look for potential bugs
   - Verify error handling
   - Check if the function is well-documented
5. Add comments:
   - Click on a line number to add a comment
   - Example comments:
     - ✅ "Great error handling here!"
     - ✅ "I like the clear docstring"
     - 💡 "Consider adding a parameter to ignore empty lines"
     - ❓ "Does this handle files with special characters?"
6. After reviewing all changes, click **Review changes** (top right)
7. Select **Approve** (or **Request changes** if there are issues)
8. Add a summary comment like: "Looks good! The error handling is solid and the function is well-documented."
9. Click **Submit review**

### Step 15: Partner A Reviews Partner B's PR

1. Go to the **Pull requests** tab
2. Click on Partner B's PR ("Add line reverser feature")
3. Click on the **Files changed** tab
4. Review the code:
   - Check for code quality
   - Look for potential bugs
   - Verify error handling
   - Check if the function is well-documented
5. Add comments:
   - Click on a line number to add a comment
   - Example comments:
     - ✅ "Nice use of slicing to reverse the list!"
     - ✅ "Good error handling implementation"
     - 💡 "Could add a parameter to preserve/strip newlines"
     - ❓ "Should we ask the user before overwriting existing files?"
6. After reviewing all changes, click **Review changes** (top right)
7. Select **Approve** (or **Request changes** if there are issues)
8. Add a summary comment like: "Great implementation! The reversal logic is clean and efficient."
9. Click **Submit review**

✅ *Check*: Both PRs should now show a green "Approved" status.

---

## Part 7: Merge Pull Requests

### Step 16: Partner A Merges Partner B's PR

1. Go to Partner B's pull request
2. Scroll down to the bottom
3. Click **Merge pull request**
4. Add a merge commit message (or keep the default)
5. Click **Confirm merge**
6. Optionally, click **Delete branch** to clean up

### Step 17: Partner B Merges Partner A's PR

1. Go to Partner A's pull request
2. Scroll down to the bottom
3. Click **Merge pull request**
4. Add a merge commit message (or keep the default)
5. Click **Confirm merge**
6. Optionally, click **Delete branch** to clean up

✅ *Check*: Both features should now be merged into the main branch!

---

## Part 8: Sync Local Repositories (Both Partners)

Now both partners need to update their local repositories with the merged changes.

### Step 18: Update Local Main Branch

```bash
# Switch to main branch
git checkout main

# Pull the latest changes
git pull origin main

# View the updated code
cat process_files.py

# Test the combined features
python process_files.py
```

### Step 19: Clean Up Local Feature Branches

```bash
# List all branches
git branch -a

# Delete your local feature branch (it's now merged)
git branch -d feature/word-counter    # Partner A
git branch -d feature/line-reverser   # Partner B

# List branches again to confirm
git branch -a
```

✅ *Check*: Both partners should now have the complete code with both features integrated!

---

## Part 9: Merge Conflict Practice (Advanced - Optional)

Want to practice resolving merge conflicts? Try this:

### Step 20: Create Conflicting Changes

**Both partners** (simultaneously):

1. Make sure you're on main: `git checkout main`
2. Create a new branch:
   ```bash
   git checkout -b feature/update-contributors
   ```
3. Edit the **same line** in `process_files.py`:
   - **Partner A**: Change `Contributors: [Add your names here]` to `Contributors: Partner A`
   - **Partner B**: Change `Contributors: [Add your names here]` to `Contributors: Partner B`
4. Commit and push:
   ```bash
   git add process_files.py
   git commit -m "Update contributors"
   git push origin feature/update-contributors
   ```
5. Create pull requests for both branches

### Step 21: Merge First PR

Partner A's PR merges successfully!

### Step 22: Resolve Merge Conflict

Partner B's PR will now show a merge conflict. Partner B needs to:

1. Update local main:
   ```bash
   git checkout main
   git pull origin main
   ```
2. Merge main into your feature branch:
   ```bash
   git checkout feature/update-contributors
   git merge main
   ```
3. Git will show a conflict. Open `process_files.py` and you'll see:
   ```python
   <<<<<<< HEAD
   Contributors: Partner B
   =======
   Contributors: Partner A
   >>>>>>> main
   ```
4. Edit the file to resolve the conflict:
   ```python
   Contributors: Partner A and Partner B
   ```
5. Complete the merge:
   ```bash
   git add process_files.py
   git commit -m "Resolve merge conflict - add both contributors"
   git push origin feature/update-contributors
   ```
6. The PR can now be merged!

---

## Reflection Questions

Discuss these questions with your partner:

1. **What challenges did you encounter during this exercise?**

2. **Why is it important to work on separate branches?**

3. **What are the benefits of code review before merging?**

4. **How would you handle a situation where you disagree with your partner's code review feedback?**

5. **What happens if both partners modify the same line of code?**

6. **Why should you pull from main before creating a new feature branch?**

7. **In a real project, who should merge a pull request - the author or the reviewer?**

---

## Key Takeaways

🎯 **Collaboration Workflow**:
- One person creates the repo, others are added as collaborators
- Always work on feature branches, never directly on main
- Use pull requests for all changes
- Have teammates review your code before merging

🎯 **Git Commands Review**:
```bash
git clone <url>              # Get a copy of a remote repository
git checkout -b <branch>     # Create and switch to a new branch
git push origin <branch>     # Push your branch to GitHub
git pull origin main         # Get latest changes from main
git branch -d <branch>       # Delete a local branch
```

🎯 **Best Practices**:
- Write clear commit messages
- Keep PRs focused on one feature
- Test your code before pushing
- Provide constructive code reviews
- Communicate with your team

---

## Extensions (Try on Your Own)

If you finish early, try adding these features:

1. **Partner A**: Add a function to convert text to uppercase and save to a file
2. **Partner B**: Add a function to find and replace text in a file
3. **Both**: Add a command-line interface using `argparse` to select which operation to run
4. **Both**: Add unit tests using `pytest` or `unittest`
5. **Both**: Add a `.github/workflows` directory with a GitHub Actions workflow for automated testing

---

## Troubleshooting

**Problem**: Can't push to the repository
- **Solution**: Make sure Partner B accepted the collaboration invitation

**Problem**: Git push says "rejected"
- **Solution**: Run `git pull origin main` first to get latest changes

**Problem**: Don't see the "Compare & pull request" button
- **Solution**: Go to "Pull requests" tab and click "New pull request" manually

**Problem**: Can't see partner's branch
- **Solution**: Run `git fetch origin` to update remote branch information

**Problem**: Merge conflict is confusing
- **Solution**: Use `git status` to see which files have conflicts, and look for `<<<<<<<`, `=======`, and `>>>>>>>` markers

---

## Congratulations! 🎉

You've successfully completed a real-world Git collaboration workflow! These are the exact same processes used by professional development teams around the world.

**Skills You Practiced**:
- ✅ Creating and managing a shared repository
- ✅ Adding collaborators
- ✅ Working on feature branches
- ✅ Creating pull requests
- ✅ Conducting code reviews
- ✅ Merging changes
- ✅ Keeping repositories in sync
- ✅ Resolving merge conflicts (optional)

Keep practicing these skills - they're essential for any software development career!

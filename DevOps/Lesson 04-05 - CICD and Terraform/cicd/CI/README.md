# 🚀 Learning CI/CD — For Beginners!

Welcome! This repo teaches you **CI/CD** using **GitHub Actions**. Don't worry — we'll explain everything step by step!

---

## 🤔 What is CI/CD? (Simple Explanation!)

Imagine you are building a LEGO castle with your friends. Every time someone adds new bricks, you all check together to make sure the castle still looks right and nothing fell down. That checking is **CI** (Continuous Integration)!

And **CD** (Continuous Delivery/Deployment) means that when everything looks good, you automatically share the finished castle with everyone — no extra steps needed!

**In software:**
- **CI** = Every time you push code, the computer automatically runs your tests to check nothing is broken 🧪
- **CD** = When tests pass, the computer automatically sends your code to users 🚀

---

## 📁 What's in this repo?

| File | What it does |
|------|-------------|
| `hello.py` | A simple Python program with a greeting function |
| `test_hello.py` | Tests that check our program works correctly |
| `.github/workflows/learn-ci.yml` | The GitHub Actions workflow (our robot helper!) |

---

## ⚙️ How does the GitHub Action work?

Every time you **push code** or open a **Pull Request**, GitHub automatically:

1. 📥 **Checks out** your code (downloads it to the robot's computer)
2. 🐍 **Sets up Python** (installs the tools needed to run Python)
3. 📦 **Installs dependencies** (gets any extra libraries the code needs)
4. 🧪 **Runs the tests** (checks that everything still works!)

If all tests pass ✅ — great job! If a test fails ❌ — GitHub tells you what broke!

---

## 🏃 Try it yourself!

1. **Fork** this repo (make your own copy)
2. **Edit** `hello.py` — change the greeting message
3. **Push** your change
4. Watch the **Actions** tab — see the robot run your tests! 🤖

---

## 🧪 Running tests locally

```bash
# Install Python (if you don't have it)
# Then run:
python -m pytest test_hello.py -v
```

---

## 💡 Key Terms Glossary

| Term | Kid-friendly meaning |
|------|---------------------|
| **Repository (repo)** | A folder where all your project files live |
| **Push** | Sending your changes to GitHub |
| **Workflow** | A list of steps the robot follows automatically |
| **Job** | One group of steps inside a workflow |
| **Step** | A single task (like "run the tests") |
| **Action** | A ready-made helper that does common tasks |
| **Pass / Fail** | Did the tests succeed ✅ or break ❌? |

---

Happy coding! 🎉

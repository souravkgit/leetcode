# Developer Guide

A comprehensive guide for setting up your development environment and contributing to the LeetCode Solutions repository.

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Local Setup](#local-setup)
- [Development Workflow](#development-workflow)
- [Testing Your Solutions](#testing-your-solutions)
- [Code Review Checklist](#code-review-checklist)
- [Troubleshooting](#troubleshooting)

## Prerequisites

### Required Software

1. **Git** - Version control
   - [Install Git](https://git-scm.com/downloads)
   - Verify: `git --version`

2. **GitHub Account** - For forking and PRs
   - Create at [github.com](https://github.com)

### Language-Specific Requirements

#### Python
- Python 3.8+
- [Install Python](https://www.python.org/downloads/)
- Verify: `python3 --version`

Optional but recommended:
```bash
pip install black flake8 isort pylint
```

#### Java
- JDK 11+
- [Install Java](https://www.oracle.com/java/technologies/downloads/)
- Verify: `java -version`

Optional:
```bash
# For code formatting
mvn install google-java-format-maven-plugin
```

#### C++
- C++ 11 or later
- GCC 7.0+ or Clang 6.0+
- [Install GCC](https://gcc.gnu.org/install/)
- Verify: `gcc --version`

Optional:
```bash
# For code formatting
brew install clang-format  # macOS
apt-get install clang-format  # Linux
```

#### JavaScript
- Node.js 14+
- [Install Node.js](https://nodejs.org/)
- Verify: `node --version`

Optional:
```bash
npm install --save-dev eslint prettier
```

## Local Setup

### Step 1: Fork the Repository
1. Go to [GitHub repository](https://github.com/YOUR-USERNAME/LeetCode)
2. Click the **Fork** button in the top-right corner
3. This creates a copy under your GitHub account

### Step 2: Clone Your Fork
```bash
# Replace YOUR-USERNAME with your GitHub username
git clone https://github.com/YOUR-USERNAME/LeetCode.git
cd LeetCode
```

### Step 3: Add Upstream Remote
```bash
# Add the original repository as upstream
git remote add upstream https://github.com/ORIGINAL-OWNER/LeetCode.git

# Verify remotes
git remote -v
# Should show:
# origin    https://github.com/YOUR-USERNAME/LeetCode.git
# upstream  https://github.com/ORIGINAL-OWNER/LeetCode.git
```

### Step 4: Create Virtual Environment (Python)
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Install development dependencies
pip install black flake8 isort pylint
```

### Step 5: Set Up Git Hooks (Optional but Recommended)
Create `.git/hooks/pre-commit` to validate before committing:

```bash
#!/bin/bash

# Get all Python files being committed
python_files=$(git diff --cached --name-only --diff-filter=d | grep '\.py$')

if [ -n "$python_files" ]; then
    echo "Running pre-commit checks on Python files..."
    
    # Run black
    black $python_files
    
    # Run isort
    isort $python_files
    
    # Run flake8
    flake8 $python_files --max-line-length=100
fi

# Stage formatting changes
git add $python_files
```

Make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

## Development Workflow

### Step 1: Create a New Branch
```bash
# Always create branch from the latest main
git fetch upstream
git checkout -b feature/0001-two-sum upstream/main

# Or a shorter version for solving problem #1
git checkout -b add/0001-two-sum
```

Branch naming conventions:
- Feature: `feature/0001-problem-name`
- Addition: `add/0001-problem-name`
- Fix: `fix/0001-problem-name`
- Docs: `docs/add-solution-template`

### Step 2: Solve the Problem
1. Create directory: `Solutions/0001-Two-Sum/`
2. Add solution file(s): `solution.py`, `solution.java`, etc.
3. Follow the template format (see CONTRIBUTING.md)
4. Test thoroughly locally

### Step 3: Commit Your Work
```bash
# Stage your changes
git add Solutions/0001-Two-Sum/solution.py
git add README.md

# Commit with meaningful message
git commit -m "feat: add Two Sum solution in Python

- Implemented O(n) hash table solution
- Added comprehensive test cases
- Updated README with problem entry"
```

Commit message guidelines:
- Type: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Format: `type(scope): description`
- Example: `feat(0001): add Two Sum solution in Python and Java`

### Step 4: Push to Your Fork
```bash
git push origin add/0001-two-sum
```

### Step 5: Create Pull Request
1. Go to [GitHub](https://github.com/ORIGINAL-OWNER/LeetCode)
2. Click **New Pull Request**
3. Select base: `main`, compare: `YOUR-USERNAME:add/0001-two-sum`
4. Fill in the PR template
5. Submit!

### Step 6: Respond to Reviews
```bash
# Make requested changes
# Stage and commit them
git add .
git commit -m "refactor: improve solution comments as per review"

# Push to the same branch
git push origin add/0001-two-sum
```

## Testing Your Solutions

### Python
```bash
# Run the test file
python Solutions/0001-Two-Sum/solution.py

# With coverage
pip install coverage
coverage run -m pytest Solutions/0001-Two-Sum/solution.py
coverage report

# Lint your code
black --check Solutions/0001-Two-Sum/solution.py
flake8 Solutions/0001-Two-Sum/solution.py
```

### Java
```bash
# Compile
javac Solutions/0001-Two-Sum/solution.java

# Run tests (if using JUnit)
javac -cp .:junit-4.13.jar TwoSumTest.java
java -cp .:junit-4.13.jar org.junit.runner.JUnitCore TwoSumTest
```

### C++
```bash
# Compile
g++ -std=c++11 -o solution Solutions/0001-Two-Sum/solution.cpp

# Run
./solution

# Check formatting
clang-format --dry-run -Werror Solutions/0001-Two-Sum/solution.cpp
```

### JavaScript
```bash
# Run with Node.js
node Solutions/0001-Two-Sum/solution.js

# Lint (if ESLint installed)
npx eslint Solutions/0001-Two-Sum/solution.js

# Format
npx prettier --write Solutions/0001-Two-Sum/solution.js
```

## Code Review Checklist

Before submitting your PR, verify:

### 📋 Code Quality
- [ ] Code compiles/runs without errors
- [ ] No warnings in the output
- [ ] Follows language conventions (PEP 8 for Python, Google style for Java, etc.)
- [ ] Variable names are descriptive
- [ ] No commented-out code
- [ ] No console.log/print debugging statements
- [ ] DRY principle applied (no code duplication)

### 📝 Documentation
- [ ] File header includes author, date, problem link
- [ ] Problem description clearly explained
- [ ] Approach/algorithm documented
- [ ] Time and space complexity documented
- [ ] Function/method has docstring
- [ ] Comments explain complex logic
- [ ] At least 3-5 test cases included

### ✅ Testing
- [ ] All test cases pass
- [ ] Edge cases considered (empty input, single element, etc.)
- [ ] Boundary cases tested (min/max values)
- [ ] Large input tested if applicable

### 📄 README
- [ ] Problem entry added to solutions table
- [ ] Problem number, name, and link correct
- [ ] Solution file links are correct
- [ ] Difficulty level correct
- [ ] Tags/categories appropriate

### 🔍 Specific Requirements
- [ ] No API keys or credentials in code
- [ ] No large binary files
- [ ] No external libraries used (unless necessary)
- [ ] File sizes are reasonable (< 500 KB)

## Troubleshooting

### Common Issues

#### Git Issues

**Issue**: "fatal: not a git repository"
```bash
# Solution: Make sure you're in the project directory
cd path/to/LeetCode
```

**Issue**: "Your branch is behind by X commits"
```bash
# Solution: Update your branch with upstream changes
git fetch upstream
git rebase upstream/main
# or
git merge upstream/main
```

**Issue**: "Merge conflict in README.md"
```bash
# Solution: Manually edit the file to resolve conflicts, then:
git add README.md
git commit -m "resolve: merge conflicts in README"
git push
```

#### Python Issues

**Issue**: "ModuleNotFoundError: No module named 'module_name'"
```bash
# Solution: Install the module
pip install module_name

# Or create requirements file
pip freeze > requirements.txt
pip install -r requirements.txt
```

**Issue**: Black formatting changes keep reverting
```bash
# Solution: Configure Black in pyproject.toml
[tool.black]
line-length = 100
target-version = ['py38']
```

#### Java Issues

**Issue**: "javac: command not found"
```bash
# Solution: Set JAVA_HOME
export JAVA_HOME=/path/to/jdk
export PATH=$JAVA_HOME/bin:$PATH
```

**Issue**: Class definition not found
```bash
# Solution: Compile with correct classpath
javac -cp . Solution.java
java -cp . Solution
```

#### C++ Issues

**Issue**: "clang-format: command not found"
```bash
# Solution: Install clang-format
brew install clang-format  # macOS
apt-get install clang-format  # Ubuntu
```

**Issue**: Undefined reference errors
```bash
# Solution: Include necessary headers and link libraries
g++ -std=c++11 -stdlib=libc++ solution.cpp -o solution
```

### Getting Help

1. **Check existing issues** - Your question might be answered
2. **Read CONTRIBUTING.md** - Most guidelines are there
3. **Look at example solutions** - See Solutions/0001-Two-Sum/
4. **Open a discussion** - For general questions
5. **Open an issue** - For bugs or unclear requirements

## Useful Resources

- [Big O Complexity Chart](https://www.bigocheatsheet.com/)
- [LeetCode Problem List](https://leetcode.com/problemset/all/)
- [Git Guide](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com)
- [Python PEP 8](https://www.python.org/dev/peps/pep-0008/)
- [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)
- [C++ Best Practices](https://isocpp.org/wiki/faq)
- [JavaScript Standard](https://standardjs.com/)

---

Happy coding! If you have suggestions for improving this guide, please open an issue or PR! 🚀

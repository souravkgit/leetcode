# 🔄 GitHub Actions Workflows Documentation

This document explains the automated workflows that validate pull requests in the LeetCode Solutions repository.

## 📊 PR Workflow Overview

### Two-Stage Approval Process

```
┌─────────────────────────────────────┐
│  Contributor Creates Pull Request   │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│   STAGE 1: Automated Validation     │
│  (GitHub Actions Workflows)         │
│  ├─ Structure validation            │
│  ├─ Code quality checks             │
│  ├─ README validation               │
│  ├─ Security scanning               │
│  └─ Language-specific linting       │
└────────────┬────────────────────────┘
             │
             ├─ ❌ FAILS → Return for fixes
             │
             ✅ PASSES
             │
             ▼
┌─────────────────────────────────────┐
│   STAGE 2: Maintainer Review        │
│  ├─ Code logic & algorithm review   │
│  ├─ Solution correctness check      │
│  ├─ Documentation quality review    │
│  ├─ Potential feedback & changes    │
│  └─ Final approval                  │
└────────────┬────────────────────────┘
             │
             ├─ 🔄 CHANGES REQUESTED
             │   └─ Contributor updates
             │      └─ Re-runs validation
             │
             ✅ APPROVED
             │
             ▼
┌─────────────────────────────────────┐
│    PR Merged to Main Branch         │
└─────────────────────────────────────┘
```

### Key Points:
1. **Automated validation runs first** - Must pass before maintainer review
2. **Maintainer reviews code logic** - Can't merge without approval
3. **Both stages are required** - No exceptions

---

## Overview

Two main workflows run automatically on every pull request:

1. **validate-pr.yml** - Core validation rules (Stage 1)
2. **code-quality.yml** - Code formatting and quality checks (Stage 1)

After Stage 1 passes ✅, a repository maintainer reviews for Stage 2.

---

## 📋 Workflow 1: validate-pr.yml

### Trigger
Runs automatically when:
- A pull request is created, updated, or reopened
- Changes affect `Solutions/` directory, `README.md`, or the workflow itself

### Jobs

#### 1️⃣ validate-structure
**Purpose**: Ensures correct directory and file structure

**Checks**:
- ✅ Directory naming: `XXXX-Problem-Name` format
- ✅ Solution files exist: At least one `solution.*` file per problem
- ✅ File headers complete:
  - Author information present
  - Problem description/link present
  - Time complexity documented
  - Space complexity documented
  - Comments in code

**What fails the check**:
❌ Directory named `TwoSum` (should be `0001-Two-Sum`)
❌ No solution files in directory
❌ Missing author information in file header
❌ Time complexity not documented

**Example**:
```bash
✅ Passing:
Solutions/0001-Two-Sum/solution.py (has all required headers)

❌ Failing:
Solutions/TwoSum/solution.py (wrong directory name)
Solutions/0001-Two-Sum/solution.py (missing author information)
```

#### 2️⃣ validate-readme
**Purpose**: Ensures README is updated with new problems

**Checks**:
- ✅ If Solutions/ changed, README.md must also change
- ✅ README contains properly formatted solutions table
- ✅ All new problems listed in the table

**What fails the check**:
❌ Added new solution but didn't update README
❌ Solutions table format is broken or missing

**Example**:
```
Added: Solutions/0042-Trapping-Rain-Water/solution.py
If README not updated → ❌ FAIL
If README table not in correct format → ❌ FAIL
```

#### 3️⃣ lint-python
**Purpose**: Checks Python code quality

**Tools Used**:
- Black (code formatting)
- Flake8 (code style)
- Pylint (code analysis)

**Checks**:
- ✅ Code follows Black formatting style
- ✅ No obvious style issues (via Flake8)
- ✅ No common mistakes detected
- ✅ Maximum line length: 100 characters

**What triggers warnings**:
⚠️ Code not formatted with Black
⚠️ Unused imports detected
⚠️ Line too long (> 100 chars)

#### 4️⃣ lint-java
**Purpose**: Validates Java code syntax and structure

**Checks**:
- ✅ Java syntax is valid
- ✅ Can be compiled without errors

#### 5️⃣ lint-cpp
**Purpose**: Validates C++ code syntax and formatting

**Checks**:
- ✅ C++ syntax is valid
- ✅ Follows clang-format style guidelines

#### 6️⃣ check-no-sensitive-data
**Purpose**: Ensures no API keys, passwords, or sensitive data

**Scans for**:
- ❌ AWS keys: `aws_access_key_id`, `aws_secret_access_key`
- ❌ API keys: `api_key = "..."`
- ❌ Passwords: `password = "..."`
- ❌ Private keys: `private_key`, `ssh_key`
- ❌ Authorization tokens: `Bearer token`

**What fails the check**:
❌ Your code contains: `api_key = "sk-12345abcde"`
❌ Found pattern: `password.*=.*['"]`

#### 7️⃣ final-check
**Purpose**: Aggregates all results and posts summary

**Posts**:
- Summary comment on your PR
- Status: ✅ Ready for Review or ❌ Needs Fixes
- Next steps for maintainer review

---

## 🎨 Workflow 2: code-quality.yml

### Trigger
Runs automatically on pull requests that modify `Solutions/` directory

### Jobs

#### 1️⃣ auto-format-python
**Purpose**: Automatically formats Python code

**Actions**:
- Runs Black formatter
- Runs isort for import sorting
- Commits changes automatically if needed

**Benefit**: You don't need to format manually!

#### 2️⃣ check-complexity
**Purpose**: Analyzes code complexity metrics

**Reports**:
- Cyclomatic complexity (how many different paths through code)
- Maintainability index
- Warnings if complexity is too high

**Example Output**:
```
Cyclomatic Complexity: 1.0 - Simple code ✅
Maintainability Index: 10.0 - Excellent ✅
```

#### 3️⃣ spell-check
**Purpose**: Checks for typos in comments and documentation

**Scans**:
- Code comments
- Docstrings
- Function names

**Example**:
❌ Typo detected: "algoritm" (should be "algorithm")

#### 4️⃣ file-size-check
**Purpose**: Ensures files aren't too large

**Limits**:
- Maximum: 500 KB per solution file

**Why**: 
- Large files slow down repository
- Indicates overly complex solution

#### 5️⃣ test-coverage-reminder
**Purpose**: Reminds you to include test cases

**Checks**:
- Does your solution include test cases?
- Are there examples that demonstrate the solution works?

**Example**:
```python
if __name__ == "__main__":
    # These are test cases
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
```

#### 6️⃣ documentation-check
**Purpose**: Verifies all required documentation sections present

**Required sections**:
- ✅ Author
- ✅ Problem
- ✅ Approach
- ✅ Time Complexity
- ✅ Space Complexity

---

## 📊 How to Interpret Workflow Results

### On Your Pull Request

You'll see a section like this:

```
Checks (8)
✅ validate-structure - passed (2m 30s)
✅ validate-readme - passed (1m 15s)
✅ lint-python - passed (1m 45s)
⏭️ lint-java - skipped (no Java files)
✅ lint-cpp - passed (2m 10s)
✅ check-no-sensitive-data - passed (30s)
✅ final-check - passed (15s)
```

### What Different Statuses Mean

| Status | Meaning | Action |
|--------|---------|--------|
| ✅ Passed | Check completed successfully | None needed |
| ❌ Failed | Check found issues | Fix the issues |
| ⏭️ Skipped | Not applicable to your changes | Normal, no action |
| 🔄 Running | Check is currently running | Wait for completion |
| ⚠️ Warning | Minor issues detected | Address if possible |

### If a Check Fails

1. **Click on the failed check** to see details
2. **Read the error message** to understand what's wrong
3. **Fix the issue locally**
4. **Commit and push** your fixes
5. **Workflow runs automatically again**

---

## 🔧 Customization

### To Add a New Rule

Edit `.github/workflows/validate-pr.yml`:

```yaml
- name: Your New Check
  run: |
    echo "Running my custom check..."
    # Add your validation logic here
```

### To Modify Existing Rules

For example, change Python line length from 100 to 120:

```yaml
# In lint-python job
flake8 $python_files --max-line-length=120
```

### To Disable a Check

Comment out or remove the corresponding job section.

---

## 📝 Common Failures & Solutions

### ❌ "Directory name does not follow XXXX-Problem-Name format"

**Problem**: 
```
Solutions/TwoSum/solution.py  ← Wrong!
```

**Solution**:
```bash
# Rename directory
mv Solutions/TwoSum Solutions/0001-Two-Sum

# Commit and push
git add .
git commit -m "refactor: rename directory to match convention"
git push
```

### ❌ "Missing Author information"

**Problem**:
Your solution file doesn't include author details

**Solution**:
Add this to the top of your file:
```python
"""
Author: Your Name or GitHub Username
Date: 2026-03-19
Problem: ...
"""
```

### ❌ "README was not updated"

**Problem**:
You added a new problem but didn't update the README table

**Solution**:
Add a row to the table in `README.md`:
```markdown
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Array | [Python](./Solutions/0001-Two-Sum/solution.py) | - | - | - | O(n) | O(n) |
```

### ❌ "Potential sensitive data found"

**Problem**:
Your code contains API keys or credentials

**Solution**:
1. Remove the sensitive data
2. If needed, replace with placeholder:
   ```python
   api_key = "YOUR_API_KEY_HERE"
   ```
3. Add to `.gitignore` if using environment variables

### ⚠️ "Code doesn't follow black style"

**Problem**:
Python code isn't formatted consistently

**Solution**:
```bash
# Format with black
black Solutions/0001-Two-Sum/solution.py

# Commit
git add .
git commit -m "style: format Python code with black"
git push
```

---

## 🚀 Workflow Performance Tips

### Make Checks Pass Faster

1. **Test locally before pushing**:
   ```bash
   python solution.py  # Run your tests locally
   ```

2. **Format code before committing**:
   ```bash
   black solution.py
   ```

3. **Include all required headers** the first time

4. **Update README with your first commit**

### Typical Workflow Time

- Initial run: 3-5 minutes
- Re-run after fixes: 2-3 minutes
- Most checks run in parallel for efficiency

---

## 🔍 Monitoring Workflow Status

### View All Workflow Runs
1. Go to your PR
2. Click **"Actions"** tab
3. Click the specific workflow run to see details

### Enable Notifications
1. Go to GitHub Settings
2. Select **Notifications**
3. Choose when to get alerts about workflow failures

---

## 📚 Related Documentation

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [CONTRIBUTING.md](./CONTRIBUTING.md) - Contribution guidelines
- [DEVELOPER_GUIDE.md](./DEVELOPER_GUIDE.md) - Local development setup
- [README.md](./README.md) - Repository overview

---

## ❓ FAQ

**Q: Can I bypass these checks?**
A: No, these checks are required for all PRs to maintain code quality.

**Q: Why are some checks skipped?**
A: Checks are skipped if they don't apply to your changes (e.g., Java linter skipped if no Java files changed).

**Q: How long do workflows take?**
A: Usually 2-5 minutes per run. Most jobs run in parallel.

**Q: Can I test workflows locally?**
A: Yes, install [act](https://github.com/nektos/act) to run GitHub Actions locally.

**Q: What if I disagree with a rule?**
A: Open an issue to discuss! Rules can be adjusted with maintainer approval.

**Q: Can I add more languages?**
A: Yes! Modify the workflows to add linters for new languages.

---

**These workflows ensure high-quality, consistent solutions across the repository! 🎯**

# 🚀 Quick Start Guide

Get up and running with the LeetCode Solutions repository in 5 minutes!

## For Repository Maintainers

### 1️⃣ Initial Setup (One-time)
```bash
# Clone your repository
git clone https://github.com/YOUR-USERNAME/LeetCode.git
cd LeetCode

# Verify all files are in place
ls -la
# You should see: README.md, CONTRIBUTING.md, DEVELOPER_GUIDE.md, .github/, Solutions/, etc.

# Push to GitHub (if not already done)
git add .
git commit -m "initial: setup LeetCode repository"
git push origin main
```

### 2️⃣ Enable GitHub Actions
1. Go to your repository on GitHub
2. Navigate to **Settings → Actions → General**
3. Ensure "Allow all actions and reusable workflows" is selected
4. Click **Save**

✅ **Done!** Your repository is now live with automated PR validation.

---

## For Contributors

### 1️⃣ Fork & Clone
```bash
# 1. Click "Fork" on GitHub repository page
# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/LeetCode.git
cd LeetCode

# 3. Add upstream remote
git remote add upstream https://github.com/ORIGINAL-OWNER/LeetCode.git
```

### 2️⃣ Create Your Branch
```bash
# Update from original repository
git fetch upstream
git checkout -b add/0042-trapping-rain-water

# Tip: Use format: add/XXXX-problem-name
```

### 3️⃣ Add Your Solution

Create the directory and solution file:
```bash
mkdir -p Solutions/0042-Trapping-Rain-Water
touch Solutions/0042-Trapping-Rain-Water/solution.py
```

**Use this template** (also see `Solutions/0001-Two-Sum/solution.py`):
```python
"""
Author: Your Name
Date: 2026-03-19
Problem: Trapping Rain Water (https://leetcode.com/problems/trapping-rain-water/)
Difficulty: Hard
Tags: Array, Two Pointers, Dynamic Programming

Problem Description:
[Brief description]

Approach:
[Explain algorithm]

Time Complexity: O(n)
Space Complexity: O(n)
"""

def trap(height):
    # Your solution here
    pass

if __name__ == "__main__":
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    print("✅ All tests passed!")
```

### 4️⃣ Update README
Add your problem to the table in `README.md`:
```markdown
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | Array, Two Pointers | [Python](./Solutions/0042-Trapping-Rain-Water/solution.py) | - | - | - | O(n) | O(n) |
```

### 5️⃣ Commit & Push
```bash
git add Solutions/0042-Trapping-Rain-Water/solution.py
git add README.md
git commit -m "feat: add Trapping Rain Water solution in Python"
git push origin add/0042-trapping-rain-water
```

### 6️⃣ Create Pull Request
1. Go to your fork on GitHub
2. Click **"Compare & pull request"**
3. Fill in the PR template
4. Click **"Create pull request"**

✅ **Done!** GitHub Actions will automatically validate your PR.

---

## 📋 Common Commands Cheat Sheet

### Git Commands
```bash
# Update your branch with latest from upstream
git fetch upstream
git rebase upstream/main

# Undo last commit (keep changes)
git reset --soft HEAD~1

# View your changes
git diff

# Push to your fork
git push origin branch-name
```

### Python Testing
```bash
# Run your solution
python Solutions/0042-Trapping-Rain-Water/solution.py

# Install formatting tools
pip install black flake8

# Format code
black Solutions/0042-Trapping-Rain-Water/solution.py

# Check for issues
flake8 Solutions/0042-Trapping-Rain-Water/solution.py
```

---

## ✅ Pre-Submission Checklist

Before pushing, verify:

- [ ] Solution file has proper header (Author, Date, Problem, Difficulty, Tags)
- [ ] Problem description is documented
- [ ] Approach is explained
- [ ] Time & Space complexity documented
- [ ] Test cases included and passing
- [ ] Code is formatted (Black for Python, etc.)
- [ ] No syntax errors
- [ ] README updated with your problem
- [ ] Directory name follows `XXXX-Problem-Name` format
- [ ] File named `solution.EXT` (e.g., solution.py)

---

## 📚 Files You Should Know

| File | Purpose |
|------|---------|
| `README.md` | Main documentation & solutions table |
| `CONTRIBUTING.md` | Detailed contribution rules |
| `DEVELOPER_GUIDE.md` | Full setup & development guide |
| `.github/workflows/validate-pr.yml` | Automatic PR validation rules |
| `Solutions/` | Where all solutions go |

---

## 🆘 Troubleshooting

### "My PR doesn't show GitHub Actions checks"
1. Wait a few seconds for Actions to start
2. Scroll down to see the checks
3. If still not showing, go to **Actions** tab

### "GitHub Actions failed - what do I do?"
1. Click on the failed check to see details
2. Fix the issues locally
3. Commit and push again
4. PR will automatically re-validate

### "I forgot to update README"
1. Make the README changes
2. Commit: `git commit -am "docs: update README"`
3. Push: `git push origin branch-name`
4. PR will automatically re-validate

### "Directory naming is wrong"
1. Rename directory: `mv Solutions/TwoSum Solutions/0001-Two-Sum`
2. Commit: `git add .` and `git commit -m "refactor: rename directory"`
3. Push the changes

---

## 🎯 Your First Contribution (Step-by-Step)

### Scenario: Adding Two Sum solution in Python

```bash
# 1. Fork repository (one-time, via GitHub UI)

# 2. Clone
git clone https://github.com/YOUR-USERNAME/LeetCode.git
cd LeetCode

# 3. Add upstream
git remote add upstream https://github.com/ORIGINAL/LeetCode.git

# 4. Create branch
git fetch upstream
git checkout -b add/0001-two-sum

# 5. Create directory and file
mkdir Solutions/0001-Two-Sum
cat > Solutions/0001-Two-Sum/solution.py << 'EOF'
"""
Author: Your Name
Date: 2026-03-19
Problem: Two Sum (https://leetcode.com/problems/two-sum/)
Difficulty: Easy
Tags: Array, Hash Table

Problem Description:
Find two numbers that add up to target.

Approach:
Use hash table to store complements.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

if __name__ == "__main__":
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]
    print("✅ Test passed!")
EOF

# 6. Update README
# (Add one line to the table)

# 7. Commit
git add Solutions/0001-Two-Sum/solution.py README.md
git commit -m "feat: add Two Sum solution in Python"

# 8. Push
git push origin add/0001-two-sum

# 9. Create PR on GitHub UI
# Fill in template and submit!
```

✅ **Congratulations!** You've made your first contribution! 🎉

---

## 🔗 Useful Links

- **Repository**: https://github.com/YOUR-USERNAME/LeetCode
- **LeetCode**: https://leetcode.com
- **Git Docs**: https://git-scm.com/doc
- **GitHub Help**: https://docs.github.com
- **Markdown Guide**: https://guides.github.com/features/mastering-markdown/

---

## ❓ Need More Help?

1. **Detailed guide**: Read `CONTRIBUTING.md`
2. **Setup help**: Read `DEVELOPER_GUIDE.md`
3. **Examples**: Check `Solutions/0001-Two-Sum/`
4. **Issues**: Open an issue on GitHub
5. **Questions**: Start a discussion on GitHub

---

**Happy coding! 🚀**

Remember: Quality over quantity. Focus on well-documented, tested solutions!

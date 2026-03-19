# LeetCode Solutions

A comprehensive collection of LeetCode problem solutions in multiple programming languages including Python, Java, C++, and more.

## 📝 Description

This repository contains well-organized, documented solutions to LeetCode problems. Each solution includes:
- Clear problem explanation and approach
- Author information and contribution details
- Detailed comments explaining the algorithm
- Optimized code implementations in various languages
- Time and space complexity analysis
- Multiple language implementations for the same problem

## 🎯 Objectives

- Provide clear, efficient solutions to LeetCode problems
- Support multiple programming languages
- Maintain high code quality and consistency
- Help developers understand different problem-solving approaches
- Build a collaborative learning community

## 📂 Repository Structure

```
.
├── README.md
├── .github/
│   └── workflows/
│       ├── validate-pr.yml
│       └── lint-code.yml
├── Solutions/
│   ├── 0001-Two-Sum/
│   │   ├── solution.py
│   │   ├── solution.java
│   │   ├── solution.cpp
│   │   └── solution.js
│   ├── 0002-Add-Two-Numbers/
│   │   ├── solution.py
│   │   ├── solution.java
│   │   └── solution.cpp
│   └── ...
└── .gitignore
```

## 📊 Solutions Table

| # | Problem | Difficulty | Tags | Python | Java | C++ | JavaScript | Time | Space |
|---|---------|-----------|------|--------|------|-----|------------|------|-------|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Array, Hash Table | [Python](./Solutions/0001-Two-Sum/solution.py) | [Java](./Solutions/0001-Two-Sum/solution.java) | - | - | O(n) | O(n) |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | Linked List, Math, Recursion | [Python](./Solutions/0002-Add-Two-Numbers/solution.py) | - | - | - | O(max(m, n)) | O(max(m, n)) |

## 🚀 How to Contribute

### Two-Stage PR Review Process

Our repository uses an automated validation system followed by maintainer review:

```
PR Submitted
    ↓
[Automated Validation] → Must Pass ✅
├─ Directory/file naming
├─ Code quality checks
├─ README validation
└─ Security scanning
    ↓
[Maintainer Review] → Must Approve 👤
├─ Algorithm correctness
├─ Solution quality
└─ Code review feedback
    ↓
PR Merged ✨
```

**Important**: Your PR must pass automated validation (Stage 1) before a maintainer will review it (Stage 2).

### Contribution Steps

1. **Fork the repository** and create a new branch for your solution
2. **Create a problem directory** with the format: `XXXX-Problem-Name/`
3. **Add your solution** following the [Solution Template](#solution-template)
4. **Update the README** with your problem details in the solutions table
5. **Submit a Pull Request** with a descriptive title
6. **Wait for automated validation** to pass
7. **Address any feedback** from maintainer review
8. **Merge** once approved

### Solution Template

Each solution file should follow this structure:

```python
"""
Author: [Your Name/GitHub Username]
Date: [Date of submission]
Problem: [Problem Name] (https://leetcode.com/problems/[problem-slug]/)
Difficulty: [Easy/Medium/Hard]
Tags: [tag1, tag2, tag3]

Problem Description:
[Brief description of what the problem asks]

Approach:
[Explain the algorithm/approach used]

Time Complexity: O(...)
Space Complexity: O(...)
"""

# [Solution Code Here]

def solution_function(parameters):
    """
    Brief description of what this function does.
    
    Args:
        parameters: Description of parameters
        
    Returns:
        Description of return value
    """
    # Implementation
    pass


# Example usage / Test cases
if __name__ == "__main__":
    # Test case 1
    result = solution_function(...)
    assert result == expected_value
```

### Guidelines for Contributions

- **Code Quality**: Ensure your code is clean, readable, and well-commented
- **Efficiency**: Provide optimal or near-optimal solutions
- **Documentation**: Include detailed comments and complexity analysis
- **Testing**: Add test cases to verify your solution works
- **File Naming**: Use `solution.py`, `solution.java`, `solution.cpp`, `solution.js` format
- **Language**: Comments and docstrings in English

## 🏗️ Supported Languages

- Python 3.x
- Java 8+
- C++ 11+
- JavaScript (Node.js)
- (More to be added)

## 💡 Algorithm Categories

Problems are categorized by algorithm type:
- Arrays & Strings
- Hash Tables & Maps
- Linked Lists
- Stacks & Queues
- Trees & Graphs
- Dynamic Programming
- Greedy Algorithms
- Sorting & Searching
- Math & Geometry
- Design & Others

## ✅ Quality Standards

All submissions must adhere to:
- ✔️ README updated with new problem entry
- ✔️ Solution files follow the required format and template
- ✔️ Code is properly formatted and linted
- ✔️ Author information is included
- ✔️ Time and space complexity documented
- ✔️ At least one test case included
- ✔️ No syntax errors
- ✔️ Follows language-specific conventions

## 📋 Pull Request Checklist

Before submitting your PR, ensure:
- [ ] Problem directory created with correct naming format
- [ ] Solution files follow template structure
- [ ] Code is tested and works correctly
- [ ] README.md is updated with the problem entry
- [ ] Author details are included in the solution file
- [ ] Comments explain the approach and algorithm
- [ ] Time and space complexity are documented
- [ ] No unnecessary files are included
- [ ] Commit messages are clear and descriptive

## 🔗 Useful Links

- [LeetCode](https://leetcode.com)
- [Big O Notation](https://www.bigocheatsheet.com/)
- [Problem Classification by Difficulty](https://leetcode.com/problemset/all/)

## 📊 Statistics

- **Total Problems**: Increasing
- **Languages Supported**: Python, Java, C++, JavaScript
- **Contributors**: Welcome!

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributors

- [Sourav Goyal](https://github.com/souravkgit)
- [CDS](https://github.com/ClientDriven-Solutions)

## 🤝 Community Guidelines

- Be respectful and constructive in discussions
- Help others understand different approaches
- Provide feedback on pull requests
- Share knowledge and learn together

## 📞 Contact & Support

For questions or suggestions, please open an issue or contact the maintainers.

---

**Happy Coding! 🎉**

*Last Updated: March 20, 2026*

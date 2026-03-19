# Contributing to LeetCode Solutions

Thank you for your interest in contributing to this repository! This document provides guidelines to ensure consistent quality and format across all submissions.

## 📋 Table of Contents

- [Getting Started](#getting-started)
- [Solution Format Requirements](#solution-format-requirements)
- [Directory Structure](#directory-structure)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing](#testing)
- [Pull Request Process](#pull-request-process)
- [FAQ](#faq)

## Getting Started

1. **Fork** the repository
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/LeetCode.git
   cd LeetCode
   ```
3. **Create** a new branch for your solution:
   ```bash
   git checkout -b add/0001-two-sum-python
   ```
4. **Commit** your changes with clear messages
5. **Push** to your fork and submit a Pull Request

## Solution Format Requirements

### Directory Naming
- Format: `XXXX-Problem-Name` where XXXX is the problem number (zero-padded to 4 digits)
- Example: `0001-Two-Sum`, `0123-Best-Time-Buy-Sell-Stock`

### File Naming
- Solution files must be named: `solution.EXTENSION`
- Examples: `solution.py`, `solution.java`, `solution.cpp`, `solution.js`
- One solution file per language per problem

### File Header Template

Every solution file **MUST** include the following header:

#### Python
```python
"""
Author: Your Name or GitHub Username
Date: YYYY-MM-DD
Problem: Two Sum (https://leetcode.com/problems/two-sum/)
Difficulty: Easy
Tags: Array, Hash Table

Problem Description:
Given an array of integers nums and an integer target, return the indices of the two numbers 
that add up to target. You may assume each input has exactly one solution, and the same element 
cannot be used twice.

Approach:
Use a hash table to store the complement of each number as we iterate through the array.
For each number, check if its complement (target - num) exists in the hash table.

Time Complexity: O(n) - Single pass through the array
Space Complexity: O(n) - Hash table stores up to n elements
"""

# Your solution code here
```

#### Java
```java
/*
 * Author: Your Name or GitHub Username
 * Date: YYYY-MM-DD
 * Problem: Two Sum (https://leetcode.com/problems/two-sum/)
 * Difficulty: Easy
 * Tags: Array, Hash Table
 *
 * Problem Description:
 * Given an array of integers nums and an integer target, return the indices of the two numbers 
 * that add up to target. You may assume each input has exactly one solution.
 *
 * Approach:
 * Use a hash map to store the complement of each number as we iterate through the array.
 * For each number, check if its complement (target - num) exists in the hash map.
 *
 * Time Complexity: O(n) - Single pass through the array
 * Space Complexity: O(n) - Hash map stores up to n elements
 */

// Your solution code here
```

#### C++
```cpp
/*
 * Author: Your Name or GitHub Username
 * Date: YYYY-MM-DD
 * Problem: Two Sum (https://leetcode.com/problems/two-sum/)
 * Difficulty: Easy
 * Tags: Array, Hash Table
 *
 * Problem Description:
 * Given an array of integers nums and an integer target, return the indices of the two numbers 
 * that add up to target. You may assume each input has exactly one solution.
 *
 * Approach:
 * Use an unordered_map to store the complement of each number as we iterate through the array.
 * For each number, check if its complement (target - num) exists in the map.
 *
 * Time Complexity: O(n) - Single pass through the array
 * Space Complexity: O(n) - Hash map stores up to n elements
 */

// Your solution code here
```

#### JavaScript
```javascript
/*
 * Author: Your Name or GitHub Username
 * Date: YYYY-MM-DD
 * Problem: Two Sum (https://leetcode.com/problems/two-sum/)
 * Difficulty: Easy
 * Tags: Array, Hash Table
 *
 * Problem Description:
 * Given an array of integers nums and an integer target, return the indices of the two numbers 
 * that add up to target. You may assume each input has exactly one solution.
 *
 * Approach:
 * Use an object to store the complement of each number as we iterate through the array.
 * For each number, check if its complement (target - num) exists in the object.
 *
 * Time Complexity: O(n) - Single pass through the array
 * Space Complexity: O(n) - Object stores up to n elements
 */

// Your solution code here
```

## Directory Structure

Create a directory for each problem with the following structure:

```
Solutions/
└── 0001-Two-Sum/
    ├── solution.py
    ├── solution.java
    ├── solution.cpp
    └── README.md (optional - for detailed explanation)
```

## Code Style Guidelines

### Python
- Follow **PEP 8** style guidelines
- Use type hints when possible
- Use meaningful variable names
- Maximum line length: 100 characters (enforced by Black formatter)
- Use docstrings for functions

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing indices of two numbers
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Java
- Follow **Google Java Style Guide**
- Use meaningful class and variable names
- Add JavaDoc comments for public methods
- Use generics appropriately
- Maximum line length: 100 characters

```java
class Solution {
    /**
     * Find two numbers in the array that add up to target.
     *
     * @param nums array of integers
     * @param target the target sum
     * @return array containing indices of the two numbers
     */
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }
            seen.put(nums[i], i);
        }
        return new int[]{};
    }
}
```

### C++
- Follow **Google C++ Style Guide**
- Use meaningful variable names
- Include comments explaining the algorithm
- Use standard library containers (vector, unordered_map)
- Maximum line length: 100 characters

```cpp
class Solution {
public:
    // Find two numbers that add up to target
    // Time: O(n), Space: O(n)
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (seen.count(complement)) {
                return {seen[complement], i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};
```

### JavaScript
- Follow **Airbnb JavaScript Style Guide**
- Use const and let, avoid var
- Use meaningful variable names
- Use JSDoc for complex functions
- Maximum line length: 100 characters

```javascript
/**
 * Find two numbers that add up to target
 * @param {number[]} nums - Array of integers
 * @param {number} target - Target sum
 * @return {number[]} - Indices of the two numbers
 */
function twoSum(nums, target) {
    const seen = new Map();
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if (seen.has(complement)) {
            return [seen.get(complement), i];
        }
        seen.set(nums[i], i);
    }
    return [];
}
```

## Testing

### Every solution must include test cases

#### Python Example
```python
if __name__ == "__main__":
    # Test case 1
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test case 2
    assert two_sum([3, 2, 4], 6) == [1, 2]
    
    # Test case 3
    assert two_sum([3, 3], 6) == [0, 1]
    
    print("All tests passed! ✅")
```

#### Java Example
```java
// Add test cases as comments or create a separate test file
// Test case 1: nums = [2, 7, 11, 15], target = 9
// Expected output: [0, 1]

// Test case 2: nums = [3, 2, 4], target = 6
// Expected output: [1, 2]
```

## Pull Request Process

### Two-Stage Review System

Your PR will go through two approval stages:

**Stage 1: Automated Validation** ✅
- GitHub Actions automatically checks your PR
- Validates directory naming and file structure
- Runs code quality checks (linting, formatting)
- Validates README.md updates
- Scans for security issues
- **This must pass before proceeding to Stage 2**
- If validation fails, fix the issues and push again

**Stage 2: Maintainer Review** 👤
- A repository maintainer reviews your code (only after Stage 1 passes)
- Checks algorithm correctness and logic
- Reviews solution quality and approach
- Provides feedback or approves
- **Approval required to merge**

### Before Submitting

- [ ] Solution file follows the required header format
- [ ] Code is properly formatted and linted
- [ ] All test cases pass
- [ ] No unnecessary files are included
- [ ] Time and space complexity are documented
- [ ] Problem name follows the naming convention
- [ ] README.md is updated with the new problem entry

**⚠️ Remember**: Your PR must pass all automated checks (Stage 1) before a maintainer will review it (Stage 2).

### Creating Your PR

1. **Fork and branch** from the main repository
2. **Add your solution** in a properly named directory
3. **Update README.md** with the problem details:
   ```markdown
   | 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Array, Hash Table | [Python](./Solutions/0001-Two-Sum/solution.py) | [Java](./Solutions/0001-Two-Sum/solution.java) | - | - | O(n) | O(n) |
   ```
4. **Commit with clear message**:
   ```bash
   git commit -m "feat: add Two Sum solution in Python and Java"
   ```
5. **Push to your fork** and submit a Pull Request
6. **Fill out the PR template** with:
   - Problem number and name
   - Languages included
   - Brief explanation of approach
   - Any special considerations

### PR Title Format

Use the format: `[TYPE] Problem #XXX: Problem Name (Language1, Language2)`

Examples:
- `[SOLUTION] Problem #0001: Two Sum (Python, Java)`
- `[SOLUTION] Problem #0042: Trapping Rain Water (C++)`
- `[IMPROVE] Problem #0001: Two Sum - Better explanation`

### PR Description Template

```markdown
## Problem
- **Number**: 1
- **Name**: Two Sum
- **Difficulty**: Easy
- **Link**: https://leetcode.com/problems/two-sum/

## Languages
- [x] Python
- [x] Java
- [ ] C++
- [ ] JavaScript

## Approach
Explain your approach here. Use hash table to store complements...

## Changes
- Added solution.py with two sum solution
- Added solution.java with two sum solution
- Updated README with new problem entry

## Test Results
All test cases pass ✅
```

## FAQ

### Q: How do I structure my solution directory?
A: Create a folder like `0001-Two-Sum` inside `Solutions/` and add your solution file(s) inside.

### Q: Can I add multiple languages for the same problem?
A: Yes! Just add multiple `solution.EXTENSION` files in the same directory.

### Q: What if I want to update an existing solution?
A: Create a PR with the improved solution. Include a note about what was improved.

### Q: Do I need to solve the problem myself?
A: Yes, solutions should be your own implementation. Cite any external references or inspired-by links.

### Q: What if my solution has a different approach than existing ones?
A: Great! Different approaches are welcome. Each solution should document its unique approach.

### Q: Is there a format for the README update?
A: Yes, use the table format shown in the main README. Keep it organized and add details.

### Q: Can I contribute in languages other than Python, Java, C++, and JavaScript?
A: Currently, we support these four languages. If you want to add a new language, please open an issue first.

### Q: How long does the review process take?
A: Usually 1-2 weeks. Maintainers will review your code and provide feedback if needed.

## Code of Conduct

- Be respectful and constructive
- Help others learn
- No spam or promotional content
- No copying without attribution
- Focus on quality and learning

## Need Help?

- Read the existing solutions for examples
- Check the [LeetCode Documentation](https://leetcode.com)
- Open an issue if you have questions

---

Thank you for contributing! Happy coding! 🎉

"""
Author: GitHub User
Date: 2026-03-19
Problem: Two Sum (https://leetcode.com/problems/two-sum/)
Difficulty: Easy
Tags: Array, Hash Table

Problem Description:
Given an array of integers nums and an integer target, return the indices of the two numbers
that add up to target. You may assume each input has exactly one solution, and you cannot use
the same element twice. You can return the answer in any order.

Approach:
This solution uses a hash table (dictionary) to achieve O(n) time complexity.
The strategy is:
1. Create an empty dictionary to store numbers we've seen and their indices
2. Iterate through the array once
3. For each number, calculate its complement (target - current_number)
4. Check if the complement exists in our dictionary
5. If it does, we found our pair - return the indices
6. If not, add the current number to the dictionary and continue

Why this works:
- Hash table lookups are O(1) on average
- Single pass through the array means O(n) time complexity
- We trade space for time (need O(n) extra space for the dictionary)

Time Complexity: O(n) - We iterate through the array once
Space Complexity: O(n) - Hash table can store up to n elements
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Find indices of two numbers that add up to target.

    Args:
        nums: List of integers where we need to find two numbers
        target: The target sum we're looking for

    Returns:
        A list containing the indices of the two numbers that add up to target.
        Returns empty list if no such pair exists.

    Examples:
        >>> twoSum([2, 7, 11, 15], 9)
        [0, 1]
        
        >>> twoSum([3, 2, 4], 6)
        [1, 2]
        
        >>> twoSum([3, 3], 6)
        [0, 1]
    """
    # Dictionary to store number -> index mapping
    # Key: number we've seen, Value: index of that number
    seen = {}

    # Iterate through each number with its index
    for i, num in enumerate(nums):
        # Calculate what number we need to reach target
        complement = target - num

        # Check if we've already seen the complement
        if complement in seen:
            # Found our pair! Return the indices
            # The complement's index comes first, current index second
            return [seen[complement], i]

        # We haven't found the pair yet, remember this number for later
        seen[num] = i

    # No pair found that sums to target
    return []


# Alternative solution: Brute Force (for comparison)
def twoSum_bruteforce(nums: List[int], target: int) -> List[int]:
    """
    Brute force solution - check every pair.
    
    Time Complexity: O(n²) - nested loops
    Space Complexity: O(1) - no extra space needed
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# ============================================================================
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    print("Testing Two Sum Solution...")
    print("=" * 50)

    # Test case 1: Basic case with positive numbers
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = twoSum(nums1, target1)
    expected1 = [0, 1]
    assert result1 == expected1, f"Test 1 failed: {result1} != {expected1}"
    print(f"✅ Test 1 passed: {nums1} + target {target1} = {result1}")

    # Test case 2: Unordered array
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = twoSum(nums2, target2)
    expected2 = [1, 2]
    assert result2 == expected2, f"Test 2 failed: {result2} != {expected2}"
    print(f"✅ Test 2 passed: {nums2} + target {target2} = {result2}")

    # Test case 3: Duplicate numbers
    nums3 = [3, 3]
    target3 = 6
    result3 = twoSum(nums3, target3)
    expected3 = [0, 1]
    assert result3 == expected3, f"Test 3 failed: {result3} != {expected3}"
    print(f"✅ Test 3 passed: {nums3} + target {target3} = {result3}")

    # Test case 4: Negative numbers
    nums4 = [-1, -2, -3, 5, 10]
    target4 = 7
    result4 = twoSum(nums4, target4)
    expected4 = [1, 3]  # -2 + 5 = 7
    assert result4 == expected4, f"Test 4 failed: {result4} != {expected4}"
    print(f"✅ Test 4 passed: {nums4} + target {target4} = {result4}")

    # Test case 5: Large numbers
    nums5 = [1000000, 2000000, 3000000]
    target5 = 5000000
    result5 = twoSum(nums5, target5)
    expected5 = [1, 2]  # 2000000 + 3000000 = 5000000
    assert result5 == expected5, f"Test 5 failed: {result5} != {expected5}"
    print(f"✅ Test 5 passed: {nums5} + target {target5} = {result5}")

    print("=" * 50)
    print("🎉 All tests passed successfully!")
    print()

    # Performance comparison
    print("Performance Comparison:")
    print("-" * 50)
    import time

    test_array = list(range(1000))
    test_target = 1998  # Sum of 999 + 999

    # Optimized solution
    start = time.time()
    for _ in range(10000):
        twoSum(test_array, test_target)
    optimized_time = time.time() - start

    # Brute force solution
    start = time.time()
    for _ in range(10000):
        twoSum_bruteforce(test_array, test_target)
    bruteforce_time = time.time() - start

    print(f"Optimized (O(n)):  {optimized_time:.4f} seconds")
    print(f"Brute Force (O(n²)): {bruteforce_time:.4f} seconds")
    print(f"Speedup: {bruteforce_time / optimized_time:.2f}x faster")

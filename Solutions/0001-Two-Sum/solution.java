/*
 * Author: Sourav Goyal
 * Date: 2026-03-19
 * Problem: Two Sum (https://leetcode.com/problems/two-sum/)
 * Difficulty: Easy
 * Tags: Array, Hash Table
 *
 * Problem Description:
 * Given an array of integers nums and an integer target, return the indices of the two numbers
 * that add up to target. You may assume each input has exactly one solution, and you cannot use
 * the same element twice. You can return the answer in any order.
 *
 * Approach:
 * This solution uses a HashMap to achieve O(n) time complexity.
 * Strategy:
 * 1. Create a HashMap to store numbers we've seen and their indices
 * 2. Iterate through the array once
 * 3. For each number, calculate its complement (target - current_number)
 * 4. Check if the complement exists in our HashMap
 * 5. If it does, we found our pair - return the indices
 * 6. If not, add the current number to the HashMap and continue
 *
 * Why HashMap?
 * - HashMap lookups are O(1) on average
 * - Single pass through the array means O(n) time complexity
 * - Trade space for time (need O(n) extra space for the HashMap)
 *
 * Time Complexity: O(n) - Single pass through the array
 * Space Complexity: O(n) - HashMap can store up to n elements
 */

import java.util.*;

class Solution {
    /**
     * Find indices of two numbers that add up to target.
     *
     * @param nums array of integers where we need to find two numbers
     * @param target the target sum we're looking for
     * @return array containing the indices of the two numbers that add up to target
     *
     * Examples:
     *   Input: nums = [2,7,11,15], target = 9
     *   Output: [0,1]
     *   Explanation: nums[0] + nums[1] == 9, return [0, 1]
     *
     *   Input: nums = [3,2,4], target = 6
     *   Output: [1,2]
     *
     *   Input: nums = [3,3], target = 6
     *   Output: [0,1]
     */
    public int[] twoSum(int[] nums, int target) {
        // HashMap to store number -> index mapping
        // Key: number we've seen, Value: index of that number
        Map<Integer, Integer> seen = new HashMap<>();

        // Iterate through each number with its index
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];

            // Calculate what number we need to reach target
            int complement = target - num;

            // Check if we've already seen the complement
            if (seen.containsKey(complement)) {
                // Found our pair! Return the indices
                // The complement's index comes first, current index second
                return new int[]{seen.get(complement), i};
            }

            // We haven't found the pair yet, remember this number for later
            seen.put(num, i);
        }

        // No pair found that sums to target
        // Return empty array or throw exception as per requirements
        return new int[]{};
    }

    /**
     * Alternative: Brute force solution - check every pair.
     * Time Complexity: O(n²) - nested loops
     * Space Complexity: O(1) - no extra space needed
     */
    public int[] twoSumBruteForce(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }
}

/**
 * Test class to verify the Two Sum solution
 */
class TwoSumTest {
    public static void main(String[] args) {
        System.out.println("Testing Two Sum Solution...");
        System.out.println("=".repeat(50));

        Solution solution = new Solution();

        // Test case 1: Basic case with positive numbers
        int[] nums1 = {2, 7, 11, 15};
        int target1 = 9;
        int[] result1 = solution.twoSum(nums1, target1);
        int[] expected1 = {0, 1};
        assert Arrays.equals(result1, expected1) : "Test 1 failed";
        System.out.println("✅ Test 1 passed: [2, 7, 11, 15] + target 9 = " + Arrays.toString(result1));

        // Test case 2: Unordered array
        int[] nums2 = {3, 2, 4};
        int target2 = 6;
        int[] result2 = solution.twoSum(nums2, target2);
        int[] expected2 = {1, 2};
        assert Arrays.equals(result2, expected2) : "Test 2 failed";
        System.out.println("✅ Test 2 passed: [3, 2, 4] + target 6 = " + Arrays.toString(result2));

        // Test case 3: Duplicate numbers
        int[] nums3 = {3, 3};
        int target3 = 6;
        int[] result3 = solution.twoSum(nums3, target3);
        int[] expected3 = {0, 1};
        assert Arrays.equals(result3, expected3) : "Test 3 failed";
        System.out.println("✅ Test 3 passed: [3, 3] + target 6 = " + Arrays.toString(result3));

        // Test case 4: Negative numbers
        int[] nums4 = {-1, -2, -3, 5, 10};
        int target4 = 7;
        int[] result4 = solution.twoSum(nums4, target4);
        int[] expected4 = {1, 3};  // -2 + 5 = 7
        assert Arrays.equals(result4, expected4) : "Test 4 failed";
        System.out.println("✅ Test 4 passed: [-1, -2, -3, 5, 10] + target 7 = " + Arrays.toString(result4));

        // Test case 5: Large numbers
        int[] nums5 = {1000000, 2000000, 3000000};
        int target5 = 5000000;
        int[] result5 = solution.twoSum(nums5, target5);
        int[] expected5 = {1, 2};
        assert Arrays.equals(result5, expected5) : "Test 5 failed";
        System.out.println("✅ Test 5 passed: [1000000, 2000000, 3000000] + target 5000000 = " + Arrays.toString(result5));

        System.out.println("=".repeat(50));
        System.out.println("🎉 All tests passed successfully!");
    }
}

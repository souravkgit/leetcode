"""
Author: CDS
Date: 2026-03-20
Problem: Add Two Numbers (https://leetcode.com/problems/add-two-numbers/)
Difficulty: Medium
Tags: Linked List, Math, Recursion

Problem Description:
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Approach:
The solution uses a dummy head to simplify linked list construction and a carry variable.
The strategy is:
1. Initialize a dummy head node to build the result list.
2. Initialize a 'carry' variable to 0.
3. Traverse both lists (l1 and l2) simultaneously.
4. In each step, sum the values of the current nodes (if they exist) and the carry.
5. Update the carry: carry = sum // 10.
6. Create a new node with the digit: sum % 10.
7. Move to the next nodes in l1, l2, and the result list.
8. After the loop, if a carry remains, append a final node with value 1.

Time Complexity: O(max(m, n)) - where m and n are the lengths of l1 and l2.
Space Complexity: O(max(m, n)) - the length of the new list is at most max(m, n) + 1.
"""

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Adds two numbers represented by linked lists in reverse order.

    Args:
        l1: Head of the first linked list.
        l2: Head of the second linked list.

    Returns:
        The head of the linked list representing the sum.
    """
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    # Continue as long as there are nodes to process or a carry exists
    while l1 or l2 or carry:
        # Get values from current nodes, or 0 if we've reached the end of a list
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        new_digit = total % 10

        # Create new node and advance pointer
        current.next = ListNode(new_digit)
        current = current.next

        # Advance l1 and l2 if possible
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy_head.next


# ============================================================================
# HELPER FUNCTIONS FOR TESTING
# ============================================================================

def to_linked_list(nums: List[int]) -> Optional[ListNode]:
    """Converts a list to a linked list."""
    dummy = ListNode(0)
    current = dummy
    for n in nums:
        current.next = ListNode(n)
        current = current.next
    return dummy.next


def to_list(node: Optional[ListNode]) -> List[int]:
    """Converts a linked list back to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# ============================================================================
# TEST CASES
# ============================================================================

if __name__ == "__main__":
    print("Testing Add Two Numbers Solution...")
    print("=" * 50)

    # Test case 1: Standard addition (243 + 564 = 807)
    # Input: [2,4,3], [5,6,4] -> Output: [7,0,8]
    l1_1 = to_linked_list([2, 4, 3])
    l2_1 = to_linked_list([5, 6, 4])
    result1 = to_list(addTwoNumbers(l1_1, l2_1))
    expected1 = [7, 0, 8]
    assert result1 == expected1, f"Test 1 failed: {result1} != {expected1}"
    print(f"✅ Test 1 passed: [2,4,3] + [5,6,4] = {result1}")

    # Test case 2: Adding zeros
    l1_2 = to_linked_list([0])
    l2_2 = to_linked_list([0])
    result2 = to_list(addTwoNumbers(l1_2, l2_2))
    expected2 = [0]
    assert result2 == expected2, f"Test 2 failed: {result2} != {expected2}"
    print(f"✅ Test 2 passed: [0] + [0] = {result2}")

    # Test case 3: Lists of different lengths and carry at the end
    # 9999999 + 9999 = 10009998
    l1_3 = to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2_3 = to_linked_list([9, 9, 9, 9])
    result3 = to_list(addTwoNumbers(l1_3, l2_3))
    expected3 = [8, 9, 9, 9, 0, 0, 0, 1]
    assert result3 == expected3, f"Test 3 failed: {result3} != {expected3}"
    print(f"✅ Test 3 passed: [9,9,9,9,9,9,9] + [9,9,9,9] = {result3}")

    print("=" * 50)
    print("🎉 All tests passed successfully!")
    

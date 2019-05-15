#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def add2numbers(l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode((l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) // 10
        node = root
        while l1.next or l2.next:
            s = (l1.next.val if l1.next else 0) + (l2.next.val if l2.next else 0) + carry
            node.next = ListNode(s % 10)
            if l1.next:
                l1 = l1.next
            if l2.next:
                l2 = l2.next
            node = node.next
            carry = s // 10
        if carry:
            node.next = ListNode(carry)
        return root


if __name__ == '__main__':
    ln1 = ListNode(2)
    ln2 = ListNode(4)
    ln3 = ListNode(3)

    ln1.next = ln2
    ln2.next = ln3

    ln4 = ListNode(5)
    ln5 = ListNode(6)
    ln6 = ListNode(4)

    ln4.next = ln5
    ln5.next = ln6
    print(Solution().add2numbers(ln1, ln4))

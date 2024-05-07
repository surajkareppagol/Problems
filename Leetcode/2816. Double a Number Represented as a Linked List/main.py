# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        number = ""

        # 1. Get the number
        while head:
            number += str(head.val)
            head = head.next

        # 2. Double the number
        number = str(int(number) * 2)

        # 3. Create a new linked list
        head = ListNode(int(number[0]))
        head_ = head

        for i in range(1, len(number)):
            temporary = ListNode(int(number[i]))
            head.next = temporary
            head = head.next

        head.next = None

        return head_


# ====================== #


def print_list(head):
    while head:
        print(f"{head.val} -> ", end="")
        head = head.next

    print()


# ====================== #

a = ListNode(1)
b = ListNode(8)
c = ListNode(9)

a.next = b
b.next = c

result = Solution().doubleIt(a)

print_list(result)

# ====================== #

a = ListNode(9)
b = ListNode(9)
c = ListNode(9)

a.next = b
b.next = c

result = Solution().doubleIt(a)

print_list(result)

# ====================== #

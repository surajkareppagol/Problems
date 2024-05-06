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
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head

        # 1. Reverse the linked list order
        while current:
            stack.append(current)
            current = current.next

        # 2. Create result_list with maximum
        current = stack.pop()
        maximum = current.val
        result_list = ListNode(maximum)

        # 3. Loop through stack and process the linked list
        while stack:
            current = stack.pop()

            if current.val < maximum:
                continue
            else:
                new_node = ListNode(current.val)
                new_node.next = result_list
                result_list = new_node
                maximum = current.val

        return result_list


# ====================== #


def print_list(head):
    while head:
        print(f"{head.val} -> ", end="")
        head = head.next

    print()


# ====================== #

a = ListNode(5)
b = ListNode(2)
c = ListNode(13)
d = ListNode(3)
e = ListNode(8)

a.next = b
b.next = c
c.next = d
d.next = e

result = Solution().removeNodes(a)

print_list(result)

# ====================== #

a = ListNode(1)
b = ListNode(1)
c = ListNode(1)
d = ListNode(1)

a.next = b
b.next = c
c.next = d

result = Solution().removeNodes(a)

print_list(result)

# ====================== #

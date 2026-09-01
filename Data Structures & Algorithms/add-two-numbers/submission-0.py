class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        cur1 = l1
        cur2 = l2

        dummy = ListNode()
        cur = dummy

        carry = 0

        while cur1 or cur2 or carry:

            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0

            total = val1 + val2 + carry

            digit = total % 10
            carry = total // 10

            cur.next = ListNode(digit)

            cur = cur.next

            if cur1:
                cur1 = cur1.next

            if cur2:
                cur2 = cur2.next

        return dummy.next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Edge case
        if not head or not head.next:
            return

        # -----------------------------------
        # 1. FIND THE MIDDLE
        # -----------------------------------
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Example: 1 -> 2 -> 3 -> 4 -> 5
        #
        # slow is at 3
        #
        # 1 -> 2 -> 3 -> 4 -> 5
        #           ↑
        #          slow


        # -----------------------------------
        # 2. SPLIT THE LIST
        # -----------------------------------

        # second starts from node after slow
        second = slow.next

        # Cut the connection
        slow.next = None

        # Now:
        #
        # First:   1 -> 2 -> 3 -> None
        #
        # Second:  4 -> 5 -> None


        # -----------------------------------
        # 3. REVERSE THE SECOND HALF
        # -----------------------------------

        prev = None

        while second:
            
            # Save the next node
            temp = second.next

            # Reverse the arrow
            second.next = prev

            # Move prev forward
            prev = second

            # Move second forward
            second = temp

        # After reversing:
        #
        # prev
        #  ↓
        # 5 -> 4 -> None

        # prev is now the head of reversed list
        second = prev


        # -----------------------------------
        # 4. MERGE BOTH LISTS
        # -----------------------------------

        first = head

        while second:

            # Save next nodes
            temp1 = first.next
            temp2 = second.next

            # Connect first -> second
            first.next = second

            # Connect second -> remaining first
            second.next = temp1

            # Move both pointers forward
            first = temp1
            second = temp2
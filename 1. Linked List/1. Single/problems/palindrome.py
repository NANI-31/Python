class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        reversed_list = None

        # reverse left half of the list while searching
        # the start point of the right half
        while fast and fast.next:
            tmp = slow

            # keep moving guys
            slow = slow.next
            fast = fast.next.next

            # place node at the start of the reversed half
            tmp.next = reversed_list
            reversed_list = tmp

        # if there are even number of elements in the list
        # do one more step to reach the first element of
        # the second list's half
        if fast is not None:
            slow = slow.next

        # compare reversed left half with the original
        # right half
        while reversed_list is not None and reversed_list.val == slow.val:
            reversed_list = reversed_list.next
            slow = slow.next

        return reversed_list is None
    
    
    # =========================================================

    class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        while slow.next:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        slow.next = prev
        
        while head and slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True
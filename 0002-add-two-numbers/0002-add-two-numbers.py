# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = 0
        n2 = 0
        i = 1
        while (l1):
            n1 += l1.val*i
            l1 = l1.next
            i *= 10
        i=1          
        while (l2):
            n2 += l2.val*i
            l2 = l2.next
            i *= 10
        sum = n1 + n2
        resul = ListNode()
        cur = resul
        cur.val = sum%10
        sum = sum/10
        while sum:
            temp = ListNode()
            cur.next = temp
            cur = cur.next
            cur.val = sum%10
            sum = sum/10
        return resul
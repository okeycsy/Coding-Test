# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head:ListNode)->bool:
        q:list=[]

        #만약 비어있는 linked list라면 팰린드롬 성립
        if head is None:
            return True

        #Transform to List
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        #Det for Palindrome
        while len(q)>1:
            #첫번째랑 마지막과 대칭이 아니면 False
            if q.pop(0)!=q.pop():
                return False

        return True

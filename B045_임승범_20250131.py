# B045. Palindrome Linked List - LeetCode

# 시간 복잡도 O(n), 공간 복잡도 O(n) - 가장 기초적인 방법(List에 저장)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        return vals == vals[::-1]
    

# 시간 복잡도 O(n), 공간 복잡도 O(1) - 러너 기법 + 후반부 역순 변경
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True  # 노드가 1개 이하이면 회문

        # 1️⃣ 중간 찾기 (slow, fast 포인터)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2️⃣ 후반부 역순(reverse)
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # 3️⃣ 앞부분과 비교
        left, right = head, prev
        while right:  # 후반부 길이만큼 확인
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
class Solution:
    def __init__(self) -> None:
        pass

    # problem1 two sum
    def twosum(self,nums,target):
        seen={}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            if remaining in seen:
                return [i,seen[remaining]]
            seen[value]=i

    # Problem 2         
    def addTwoNumbers(self, l1, l2):
        strng = ''
        str2 = ''
        
        while l1: # adding values of l1 into an empty string
            strng += str(l1.val)
            l1 = l1.next

        while l2: # adding values of l2 into an empty string
            str2 += str(l2.val)
            l2 = l2.next

        strng = strng[::-1] # reversing the string
        str2 = str2[::-1] #reversing the string

        res = 0

        res = int(strng) + int(str2) # converting strings into intergers and adding them


        res = str(res)[::-1]

        head = None
        temp = None
        
        for i in range(len(res)): #adding the string into LinkedList one by one
            
            if head is None:
                head = ListNode(res[i])
                temp = head
            else:
                
                temp.next = ListNode(res[i])
                temp = temp.next   
            
        return head 

    # Problem 3 Maximum length string
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=mresult=0
        store={}
        for i in range(len(s)):
            if s[i] not in store or store[s[i]]<start:
                result=i-start+1
                mresult=max(result,mresult)
            else:
                start=store[s[i]]+1
            store[s[i]]=i
        return mresult




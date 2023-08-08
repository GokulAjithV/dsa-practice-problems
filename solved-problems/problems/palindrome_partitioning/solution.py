class Solution:
    def partition(self, s: str) -> List[List[str]]:


        n = len(s)

        res = []

        def isPalindrome(string):

            if(string == string[::-1]):
                return True 

            return False    

        def helper(start,temp):

            if(start == n):
                res.append(temp[:])
                return

            for i in range(start,n):

                if(isPalindrome(s[start:i+1])):
                    temp.append(s[start:i+1])
                    helper(i+1,temp)
                    temp.pop()
        
        helper(0,[])
        return res


                
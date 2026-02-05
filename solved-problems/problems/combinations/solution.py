class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        
        res = []
        def helper(i,temp):
            
            if(len(temp) == k):
                res.append(temp[:])
                return 
            if(i == n):
                return 


            temp.append(arr[i])  
            helper(i+1,temp)

            temp.pop()
            helper(i+1,temp)

        helper(0,[])
        return res    


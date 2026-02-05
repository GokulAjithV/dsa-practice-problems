class Solution:
    def reverseVowels(self, s: str) -> str:

        vowelString = []
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        l = list(s)

        for i in range(len(l)):
            if(l[i] in vowels):
                vowelString.append(l[i])
                l[i] = '*'

        for i in range(len(l)):
            if(l[i] == '*'):
                l[i] = vowelString.pop()

        ans = ''
        return ans.join(l)


        
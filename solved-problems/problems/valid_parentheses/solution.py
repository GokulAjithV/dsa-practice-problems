class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_stack = []
        parentheses_set = {"{", "[", "("}
        top = None    
        for p in s:
            if p in parentheses_set:
                parentheses_stack.append(p)
                continue
            if parentheses_stack: 
                top = parentheses_stack[-1]
            else:
                return False
            if (p == "}") and (top == "{"):
                parentheses_stack.pop()
            elif (p == ")") and (top == "("):
                parentheses_stack.pop()
            elif (p == "]") and (top == "["):
                parentheses_stack.pop()
            else:
                return False
        if (len(parentheses_stack) == 0):
            return True
        return False

                
        
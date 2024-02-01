class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        for c in s:
            if c=='(':
                stack.append(c)
            else:
                if stack:
                    if stack[-1]=='(':
                        stack.pop()
                        if stack:
                            if stack[-1]=='(' or stack[-1]==')':
                                stack.append(2)
                            else:
                                stack.append(stack.pop()+2)
                        else:
                            stack.append(2)
                    elif stack[-1]==')':
                        pass
                    else:
                        if len(stack)>=2 and stack[-2]=='(':
                            if len(stack)>=3 and stack[-3] not in ['(', ')']:
                                temp=stack.pop()
                                stack.pop()
                                stack.append(stack.pop()+2+temp)
                            else:
                                temp=stack.pop()
                                stack.pop()
                                stack.append(temp+2)
                        else:
                            stack.append(c)
                else:
                    stack.append(c)
        max=0
        for x in stack:
            if x not in [')', '('] and x>max:
                max=x

        return max

                            
                        
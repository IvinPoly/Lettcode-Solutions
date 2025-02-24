def valid(f):
    
    bracket = {'}':'{',')':'(',']':'['}
    stack=[]
    
    for char in f:
        if char in bracket:
            if stack and stack[-1]==bracket[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False
                
    
f='}()()()()()[][][][]'
print(valid(f))

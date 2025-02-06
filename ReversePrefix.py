a=input()
ch=input()
b=[]
def prefix(a,ch):
    for i in range(len(a)):
        if a[i]!=ch:
            b.append(a[i])
        else:
            break
    return ch+"".join(reversed(b))+a[a.find(ch)+1:]
print(prefix(a,ch))


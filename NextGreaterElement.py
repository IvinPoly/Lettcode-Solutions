def nextGreater(array):
    stack=[]
    for i in range(len(array)):
        f=0
        for j in range(i+1,len(array)):
            if array[j]>array[i]:
                stack.append(array[j])
                f=1
                break
        if f==0:
            stack.append(0)
    return stack


array = list(map(int,input().split()))
print(nextGreater(array))


            

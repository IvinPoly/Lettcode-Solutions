def temp(arr):
    n=len(arr)
    res=[]
    
    for i in range(n):
        j = i+1 
        count = 1 
        while j<n:
            if arr[j]>arr[i]:
                break
            count+=1 
            j+=1 
        count = 0 if j==n else count
        res.append(count)
    return res
    
arr=list(map(int,input().split()))
print(temp(arr))

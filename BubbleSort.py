def Bubble(arr):
    if arr == sorted(arr):
        return "Sorted"
    for i in range(len(arr)-1, 0 ,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
    
arr=list(map(int,input().split()))
print(Bubble(arr))

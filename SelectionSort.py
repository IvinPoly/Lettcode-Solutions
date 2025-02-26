n = int(input("Enter number of elements: "))
arr=list(map(int,input().split()))
def SelectionSort(arr):
    for i in range(len(arr)):
        temp = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                temp = j 
            arr[i],arr[temp] = arr[temp],arr[i]
    return arr

print(SelectionSort(arr))

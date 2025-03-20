def contSeq(numbers):
    #numbers = sorted(x for x in list1 if isinstance(x,int) )
    
    result = []
    temp = [numbers[0]]
    
    for i in range(1,len(numbers)):
        if numbers[i] == numbers[i-1]+1:
            temp.append(numbers[i])
        else:
            if len(temp)==3:
                result.append(temp)
            temp = [numbers[i]]
            
    if len(temp)==3:
        result.append(temp)
    return result
    
numbers = list(map(int,input().split()))
print(contSeq(numbers))
    

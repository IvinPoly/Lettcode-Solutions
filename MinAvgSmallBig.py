a=list(map(int,input().split()))
a.sort()
def Avg(a):
    start=0
    end=len(a)-1
    avgarr=[]

    if len(a)%2!=0:
        return "Enter even array!!!"

    while start<=end:
        avrg=(a[start]+a[end])/2
        avgarr.append(avrg)
        start=start+1
        end=end -1
    return min(avgarr)

print(Avg(a))

#include<stdio.h>

void main(){
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    
    int max = 0,sum;
    for(int i=0;i<n;i++)
    {
        sum+=arr[i];
        if(sum>max)
        {
            max=sum;
        }
        if(sum<1)
        {
            sum=0;
        }
        
    }
    
    printf("%d",max);
}

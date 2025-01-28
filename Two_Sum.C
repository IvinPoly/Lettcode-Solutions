#include<stdio.h>
int main(){
    int target;
    int arr[50];
    int n;
    int count=0;
    scanf("%d",&n);
    for(int i = 0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    printf("Enter Target value:");
    scanf("%d",&target);
    
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(count==0){
                
            if(arr[i]+arr[j]==target){
            printf("%d %d\n",i,j);
            count++;
        }}
    }
}
if(count==0){
    printf("Doesn't exist");
}
}

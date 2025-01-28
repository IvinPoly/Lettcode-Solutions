#include<stdio.h>
int main(){
    int n;
    int a;
    int max;
    int x = 0;
    int arr[50];
    int brr[50];
    scanf("%d",&n);
    for(int i =0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for(int i =0;i<n;i++){
        for(int j = i+1;j<n;j++){
        brr[x]=arr[j]-arr[i];
        x++;
    }}
    for(int i=0;i<(n-i)+1;i++){
        if(brr[i]<brr[i+1]){
            max=brr[i+1];
        }
    }
    printf("%d",max);
}

#include<stdio.h>
int main(){
    int n;
    int a;
    int arr[50];
    scanf("%d",&n);
    for(int i =0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for(int i =0;i<n;i++){
        for(int j = i+1;j<n;j++){
        if(arr[i]==arr[j]){
            a = arr[j];
        }
    }}
    printf("%d",a);
}

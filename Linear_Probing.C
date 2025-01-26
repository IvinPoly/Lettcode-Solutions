#include<stdio.h>
int main(){
    int n;
    int h;
    int arr[100];
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        arr[i]=-1;
    }
    for(int i=0;i<n;i++){
        int key;
        scanf("%d",&key);
        h = key % n;
        while(arr[h]!=-1){
            h=(h+1)%n;
        }
        arr[h]=key;
    }
    for(int i=0;i<n;i++){
        printf("%d",arr[i]);
    }
}

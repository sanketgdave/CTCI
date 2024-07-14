#include<stdio.h>


int main(){
    int i,nlines,nchars;

    printf("Enter Number of Lines: ");
    scanf("%d",&nlines);
    printf("Enter Number of Characters: ");
    scanf("%d",&nchars);

    for(i=1;i<=nlines*nchars;i++){
        printf("%d ",i);
        if(i % nchars == 0){
            printf("\n");
        }
    }
}


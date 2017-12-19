#include <stdio.h> //printf, scanf
//#include <stdbool.h>
#include <string.h> //strlen

//#include <math.h>
#include <stdlib.h> //malloc
#include <ctype.h> //toupper, tolower, isalpha, isupper...



int main(void){

  char* name = malloc(sizeof(char) * 10);

  printf("whats ur name?\n");
  scanf("%s", name); //into name adress?

  if(name != NULL){
    char* other = malloc((strlen(name) + 1) * sizeof(char)); //char pointer point to =

    for (int i = 0, n = strlen(name); i <= n; i++){
      other[i] = name[i];
      //*(other+i) = *(name+i)
    };

    if(strlen(name) > 0){
      *name = toupper(*name);
      for (int i = 0, n = strlen(other); i <= n; i++){
      other[i] = toupper(other[i]);
      }
      printf("hello, %s\n", name);
      printf("goodbye, %s\n", other);
    }

  }  else return 0;

//  free(name);
//  free(other);
}

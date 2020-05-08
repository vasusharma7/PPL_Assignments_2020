#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
int i = 10;
void *hello(){
	while(i > 0){
		printf("HELLO :) \n");
		sleep(1);
		i--;
	}
}
void *goodBye(){
	while(i > 0){
		sleep(1);
		printf("GOODBYE :( \n");
		i--; 
	}
}


int main(){
	printf("Execution Started\n");
	pthread_t t1,t2;
	pthread_create(&t1,NULL,hello,NULL);
	pthread_create(&t2,NULL,goodBye,NULL);
	int err1 = pthread_join(t1,NULL);	
	int err2 = pthread_join(t2,NULL);
	//printf("%d %d",err1,err2);
	printf("Terminating the program \n");
	return 0;
}

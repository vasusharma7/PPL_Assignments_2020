#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

void *hello(){
	while(1){
		sleep(1);
		printf("HELLO FROM THREAD :)\n");
	}
}

int main(){
	printf("Execution Started\n");
	pthread_t t1;
	int err = pthread_create(&t1,NULL,hello,NULL);
	err = pthread_join(t1,NULL);	
	return 0;
}

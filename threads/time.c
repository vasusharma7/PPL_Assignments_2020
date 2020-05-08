#include<stdio.h>
#include<pthread.h>
#include<unistd.h>
int seconds = 0;
int minutes = 0;
int hours = 0;


void *timer_hours(){
	while(1){
		if (minutes == 60){
			hours++;
			minutes = 0;
		}
	}
}
void *timer_minutes(){
	while(1){
		if (seconds ==60){
			minutes++;
			seconds = 0;
		}
	}
}

void *timer_seconds(){
	while(1){
		sleep(1);
		seconds++;
	}
}
void *print(){
	char hrs[3] ={ '\0' },min[3] = {'\0'},sec[3] = {'\0'};
	while(1){
		(hours < 10) ?  sprintf(hrs,"0%d",hours) : sprintf(hrs,"%d",hours);	
		(minutes < 10) ?  sprintf(min,"0%d",minutes) : sprintf(min,"%d",minutes);	
		(seconds < 10) ?  sprintf(sec,"0%d",seconds) : sprintf(sec,"%d",seconds);	
		printf("\r%s : %s : %s",hrs,min,sec);
	}
}


int main(){
	printf("TIMER STARTED\n");
	pthread_t t1,t2,t3,t4;
	pthread_create(&t1,NULL,timer_seconds,NULL);
	pthread_create(&t2,NULL,timer_minutes,NULL);
	pthread_create(&t3,NULL,timer_hours,NULL);

	pthread_create(&t4,NULL,print,NULL);
	int err1 = pthread_join(t1,NULL);	
	int err2 = pthread_join(t2,NULL);
	int err3 = pthread_join(t3,NULL);
	int err4 = pthread_join(t4,NULL);
	//printf("%d %d",err1,err2);
	printf("Terminating the program \n");

	return 0;
}

//Activation Records for Factorial

#include<stdio.h>
#include<limits.h>
int fact(int num){
	if(num < 0)
		return INT_MAX;
	if(num == 0)
		return 1;
	
	return num*fact(num - 1);

}
int main(){
	int res = 0;
	int factnum = 3;
	fact(factnum);
	return 0;
}

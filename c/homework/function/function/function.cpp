#include <stdio.h>
#include <stdbool.h>
#include <math.h>
//����� ��������� ������� c ������� ���� �����

//void main() {
//
//        double num1 = pow(2, 3);
//        double num2 = sqrt(100);
//
//        printf("num1=%.lf  num2=%.2lf", num1, num2);
//
//    }

//                                            ������ ������ �� ���� ��� ���� �� ���� ����
// 
// 
//   ����� �� ������� ��� ������� ��� �������� ���� ����
//void checkDividers(int a, int b);
//// ���� ������ �
//void main() {
//
//	int num_1, num_2;
//
//	//���� �������� �� ������� ������� ������ �� �������
//
//	checkDividers(15, 7);
//
//	//   ���� ������� �� ������� ������� �� ��� ������
//
//	printf("enter 2 numbers: ");
//	scanf_s("%d %d", &num_1, &num_2);
//
//	checkDividers(num_1, num_2);
//}
//// �������� ������
//void checkDividers(int a, int b) {
//	if (a % b == 0 || b % a == 0) 
//		printf("dividers\n");
//	
//	else
//		printf("not dividers \n");
//
//}

//    ����� ���� 28 //  ����� ������� ������ ���� ��� ������� ������ �� ������� ���


//void checkDividers(int a, int b) {
//	if (a % b == 0)
//		printf("%d\n", b);
//
//
//}
//
//
//void main() {
//
//	int user_num, test_num, i;
//
//	printf("enter num for test: ");
//	scanf_s("%d", &user_num);
//
//	for (i = 2; i <= user_num; i += 1) {
//
//		test_num = i;
//
//		checkDividers(user_num, test_num);
//
//
//	}
//}

//����� �� 29 // ������� ������ ����� ������ �� ��� ���� ������

// function that chack if the number is prime

//void primeNumber(int num_1, int i, int div = 0) {
//	
//
//	for (i = 2; i < num_1; i += 1) {
//		if (num_1 % i == 0)
//			div += 1;
//	}
//	if (div >= 1)
//		printf("the number is not prime");
//	else
//		printf("the numbet is prime");
//
//}
//void main() {
//
//	int user_number = 0, i = 0;
//
//	printf("plese enter a number: ");
//	scanf_s("%d", &user_number);
//	primeNumber(user_number, i);
//}

// ����� ���� 30 //    ����� ������� �� ����� ����� ��������� ����� �� ����� �������� ������ �� ������ ��� ����
   
//void triangular(int a, int b, int c) {
//	if (a + b > c || a + c > b || b + c > a)
//		printf("The triangle is legal");
//	else
//		printf("The triangle is illegal");
//}
//
//
//void main() {
//	int num_1, num_2, num_3;
//
//	printf("Anna enter the lengths of the three sides: ");
//	scanf_s("%d %d %d", &num_1, &num_2, &num_3);
//
//	triangular(num_1, num_2, num_3);
//
//	
//}

// ����� ���� 31 //  ���� - ����� ���� ������� ������ ����� ���

//void Factorial(int num, int result ,int i) {
//
//	for (i = 1; i < num + 1; i += 1) {
//		result = result * i;
//	}
//	printf("the result is: %d", result);
//
//}
//void main() {
//	int user_num, factor =1, a = 0;
//	printf("please enter a number: ");
//	scanf_s("%d", &user_num);
//	Factorial(user_num, factor,a);
//}



//
//void mai() {
//
//	int arr[] = { 4,5,6,7 };
//	printf("%d", arr[2]);
//}

//����� �� 32 //  ���� ������ ������� ������� ������� ���// �� ����� ���� ��������� ����� �� ��� ������ ����� ��� ������� �����

//int primeNumber(int num_1){
//	int i, isPrime = 1;
//	for (i = 2; i < num_1; i += 1) {
//		if (num_1 % i == 0)
//			isPrime = 0;
//			break;
//
//	}
//	return isPrime;
//
//}
//
//void main(){
//	int user_num = 0;
//	printf("pleas enter a number: ");
//	scanf_s("%d", &user_num);
//	if (primeNumber(user_num) == 0) {
//		printf("the number is not prime");
//	}
//	else
//		printf("the number is prime");
//	}


// ����� �� 33  // ���������// ����� ������ ���� ��� ������� �� ��� ��������

//
//int palindrom(int num) {
//	int  num_2 = 0, num_3 = 0;
//
//	num_3 = num;
//
//	while (num != 0) {
//		num_2 = num_2 * 10 + num % 10;
//
//		num = num / 10;
//	}	
//	if (num_2 == num_3) 
//	
//	return 1;
//	}
//
//void main() {
//	int user_num;
//
//	printf("please enter a number for chack if is palindrom: ");
//	scanf_s("%d", &user_num);
//	
//	if (palindrom(user_num) == 1)
//		printf("the number is palindrm");
//		
//	else
//		printf("teh number is not palindrom");
//
//}

// ����� �� 34//  ����� 1089// 

// checking if the number is palindrom
//
//int palindrom(int num) {
//	int  num_2 = 0, num_3 = 0;
//
//	num_3 = num;
//
//	while (num != 0) {
//		num_2 = num_2 * 10 + num % 10;
//
//		num = num / 10;
//		
//	}	
//	if (num_2 == num_3)
//
//	return 1;
//	}
//
//int palindrom_2(int num) {
//	int  num_2 = 0, num_3 = 0;
//
//	num_3 = num;
//
//	while (num != 0) {
//		num_2 = num_2 * 10 + num % 10;
//
//		num = num / 10;
//
//	}
//	if (num_2 != num_3)
//
//		return num_2;
//}
//
////fanction for sub low number from the highest number
//
//int sub(int num_orgin, int num_rever) {
//	int result = 0;
//	if (num_orgin > num_rever)
//		result = num_orgin - num_rever;
//	else
//		result = num_rever - num_orgin;
// 
//	return result;
//}
//
//void main() {
//	int user_num, num = 0, sum =0;
//	printf("please enter a Triple digits: ");
//	scanf_s("%d", &user_num);
//	if (palindrom(user_num) == 1)
//		printf("the number is palindrom");
//	else{
//		if (user_num < 100)
//			user_num = user_num * 10;
//		num = sub(user_num, palindrom_2(user_num));
//		if (num == 99)
//			num = 990;
//		sum = num +palindrom_2(num);
//		printf("%d", sum);}
//
//}

//  ���� 49 -- ����� ������

//void main() {
//
//	int arr[] = { 2,4,2,7,6,3,9 };
//	int i = 0;
//	int* ptr;
//	ptr = &arr[6];
//
//	for (i = 0; (i<sizeof(arr)/4); i++) {
//
//		printf("%d ", *ptr--);
//	}
//}
// ����� ���� 1 - ������� ������ ���� ��� ������� �� ����� ��� ����� ����� ����




#include <stdio.h>
#include <stdbool.h>
#include <math.h>
//דוגמא לפונקציות מספריית c שמבצעות חזקה ושורש

//void main() {
//
//        double num1 = pow(2, 3);
//        double num2 = sqrt(100);
//
//        printf("num1=%.lf  num2=%.2lf", num1, num2);
//
//    }

//                                            פוקציה לבדיקה עם מספר הוא מחלק של המפר השני
// 
// 
//   בכרזה על הפוקציה מעל התוכנית כדי שהתוכנית תכיר אותה
//void checkDividers(int a, int b);
//// הרצת התוכני ת
//void main() {
//
//	int num_1, num_2;
//
//	//הרצת הפונקציה על פרמטרים שהוכנסו בחתימה של הפוקציה
//
//	checkDividers(15, 7);
//
//	//   הרצת הפוקציה על פרמטרים שיוכנסו על ידי המשתמש
//
//	printf("enter 2 numbers: ");
//	scanf_s("%d %d", &num_1, &num_2);
//
//	checkDividers(num_1, num_2);
//}
//// פונקציתת החישוב
//void checkDividers(int a, int b) {
//	if (a % b == 0 || b % a == 0) 
//		printf("dividers\n");
//	
//	else
//		printf("not dividers \n");
//
//}

//    תרגיל מספר 28 //  כתיבת פונקציה שמקבלת מספר שלם מהמשתמש ומוצאת את המחלקים שלו


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

//תרגיל מס 29 // פונקציה המקבלת פרמטר ובודקת אם הוא מספר ראשוני

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

// תרגיל מספר 30 //    קליטה מהשתשמש של שלושה מספים שמייצגיים צלעות של משולש ופונקציה הבודקת אם המשולש הוא חוקי
   
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

// תרגיל מספר 31 //  עצרת - קליטת מספר מהמשתמש ופליטת העצרת שלו

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

//תרגיל מס 32 //  מספר ראשוני באמצעות פונקציה שמחזירה ערך// יש לקלוט מספר והפונקציה תחזיר רם הוא ראשוני במידה וכן התוכנית תדפיס

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


// תרגיל מם 33  // פולינדרום// פוקצי הקולטת מספר שלם ומחזירה אם הוא פולידרום

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

// תרגיל מס 34//  המספר 1089// 

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

//  שאלה 49 -- מהסוף להתחלה

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
// תרגיל מספר 1 - פונקציה המקבלת מספר שלם ומחזירה את ההפרש בין המספר הגדול לקטן




#include <stdio.h>
#include <limits.h>

void main() {
	//
	//	
	//	int rid1, rid2, area;
	//
	//	printf("plise, enter the kength rid 1:");
	//	scanf_s("%d", &rid1);
	//
	//	printf("plese, enter the length rid 2:");
	//	scanf_s("%d", &rid2);
	//
	//	area = rid1 * rid2;
	//	printf("the area of the rectangle is: %d", area);
	//
	//	}

	// תרגיל 2

		//int price, qantity, discount, pay;

		//printf("plese, enter price:");
		//scanf_s("%d", &price);

		//printf("plese, enter qantity:");
		//scanf_s("%d", &qantity);
		//
		//printf("plese, enetr discount:");
		//scanf_s("%d", &discount);

		//pay = price * qantity * 100 / discount;

		//printf("Teh amont to be paid is: %d", pay);

		// תרגיל 3

		/*int num1, num2, num3, avg1;


		printf(" plese enter num1:" );
		scanf_s("%d", &num1);

		printf("plese enter num2:");
		scanf_s("%d", &num2);

		printf("pkese enter num3:");
		scanf_s("%d", &num3);

		avg1 = (num1 + num2 + num3) / 3;

		printf("your avg is: %d", avg1);*/

		//  תרגיל 4 


//int hour, minute_per_hour, minute_number, minute;

//printf("plese enter hour: ");
//scanf_s("%d", &hour);

//printf("plese enter minute: ");
//scanf_s("%d", &minute);

//minute_per_hour = hour * 60;

//minute_number = minute_per_hour + minute;

//printf("The minute number is:%d", minute_number);

			  //תרגיל8 

	//int price, total_price;

	//printf("plse enter price product: ");
	//scanf_s("%d", &price);

	//total_price = price * 1.17;

	//printf("The price includes value added tax is:%d\n\n", total_price);

	//if (total_price > 10000)
	//	printf("your price higher than: 10,000");
	//else
	//	printf("your price OK");

				  // תרגיל מס 9



	//int person1, person2, person3;
	//printf("plese enter yout age:");
	//scanf_s("%d", &person1);

	//printf("plese enter your age:");
	//scanf_s("%d", &person2);

	//printf("plese enter your enter:");
	//scanf_s("%d", &person3);

	//if (person1 >= 18 && person2 >= 18 && person3 >= 18)
	//	printf("welcome to the club");
	//else
	//	printf("sory !you are not allowed to enter");

//                             // תרגיל מס 12 
//int i;
//
//for (i = 100; i <= 200; i += 2)
//	printf("%d ", i);

										//תרגיל מס 13
//
//float i;
//
//for (i = 0; i <= 5; i += 0.5)
//	printf("%.1f ", i);

									  // //תרגיל מס 14

//int i, grade, sum_of_marks = 0, avarage;
//
//for (i = 1; i <= 7; i += 1) {
//
//	printf("plese enter your geade:");
//	scanf_s("%d", &grade);
//
//	sum_of_marks += grade;
//}
//
//
//
//avarage = sum_of_marks / 7;
//
//printf("Your avarage is:%d", avarage);

								 // חישוב עצרת //תרגיל מס 15
//
//int i, number, sum_number = 1;
//
//printf("plese enter number:");
//scanf_s("%d", &number);
//for (i = 1; i <= number; i ++)
//
//	sum_number = sum_number * i;
//
//printf("the result is:%d", sum_number);

									//בדיקת אם מספר הוא עצרת של מספר כלשהוא //תרגיל מס 16

//int i, number, factorial = 1;
//
//printf("plese enter number:");
//scanf_s("%d", &number);
//
//for (i = 1; factorial < number; i++)
//	factorial *= i;
//
//if (number /  factorial == 1)
//
//printf("factorial");
//
//else
//printf("not factorial");

							   // דרך שגויה מאחר ןהמספר מתעגל//תרגיל 16 .2

//int i, number, factorial = 1;
//
//printf("plese enter number:");
//scanf_s("%d", &number);
//
//for (i = 1; number > 1; i++)
//	number /= i;
//
//if (number == 1)
//
//	printf("factorial");
//
//else
//	printf("not factorial");

							  //תרגיל 16 באמעות מודולו דוגמת מרצה

//	// declare vars
//int i, number;
//
//// input factorial result
//printf("Enter a number: ");
//scanf_s("%d", &number);
//
//for (i = 1; number % i == 0; i++) {
//	number = number / i;
//	printf("number inside loop: %d\n", number);
//}
//
//if (number == 1)
//printf("number is factorial result of %d \n\n", i - 1);
//
//else
//printf("number is not factorial result \n\n");

							//הדפסת המספר הגבוה //תרגיל מס 17


//int i, number, hieght_number = INT_MIN;
//
//for (i = 1; i <= 10; i++)
//
//{
//printf("enter a numbers:"); 
//	scanf_s("%d", &number); 
//
//	if (number > hieght_number)
//		hieght_number = number;
//}
//printf("%d", hieght_number);

					   // קליטת 2 מספרים כשהראשון הוא הקטן מביניהם ולמצא מחלק משותף //תרגיל מס 18

//
//	int i, number_s, number_b, a = 0;
//
//	printf("enter to numbers: ");
//	scanf_s("%d, %d", &number_s, &number_b);
//
//	for (i = 2; i <= number_s; i++){
//		if (number_s % i == 0 && number_b % i == 0)
//			a = i;
//			printf("%d ", a);
//}
//	if (a < 2)
//	printf("division not fuond");

												 // תרגיל מס 19 // קליטת 2 מספרים וחישוב חזקה ביניהם(מעריך ובסיס(
//
//int basis, estimator, i, calculate = 1;
//
//printf("plese enter basis number:");
//scanf_s("%d", &basis);
//
//printf("plese enter estimator number:");
//scanf_s("%d", &estimator);
//
//for (i = 1; i <= estimator; i++)
//calculate *= basis;
//printf("the result is: %d", calculate);

										 // תרגיל מס 20// קליטת 10 מספרים והדפסה אם הסכום = 0 גדול מ0 או קטן מ0

//int number =0, i =1, result = 0;
//
//for (i; i <= 10; i++) {
//	printf("plese enter a number:");
//	scanf_s("%d", &number);
//	result += number;
//}
//if (result < 0)
//printf("the result is %d it is less than zero!!!", result);
//if (result > 0)
//printf("the result is %d it is graeter than zero!!! ", result);
//else
//printf("the result is %d it equal to zero!!!", result);


	//									   // תרגיל מס 21 // קליטת מספרים עד שיקלט מס 0 והדפסת סכום המספרים שנקלטו

	//int number = 1, sum = 0, i, avarage = 0, loop = 0;
	//for (i = 0; number != 0; i++) {
	//	printf(" plese enter number:");
	//	scanf_s("%d", &number);
	//	sum += number;
	//	loop = i;
	//	
	//}
	//avarage = sum / loop; 
	//printf("the sum is: %d\n\n", sum);
	//printf("The avarage is: %d", avarage);


											 // תרגיל מס 22 //כשסכום המשתמש יעבור את 100 התוכנה תדפיס את מספר הפעמים של הקלט 

//int num_user = 0, i, sum = 0;
//for (i = 0; sum <= 100; i++) {
//	printf("plese enter number:");
//	scanf_s("%d", &num_user);
//	sum += num_user;
//
//}
//printf("The user enter: %d numbers", i);

									   //תרגיל מס 23 // קליטת זוג מספרים עד שיקלט מספר שהוא המחלק של השני

	/*int num_1 = 0, num_2 = 0, i;
	printf("plese enter a number:");
	scanf_s("%d", &num_1);
	printf("plese enter another number:");
	scanf_s("%d", &num_2);

	for (i = 0; num_1 % num_2 != 0 && num_2 % num_1 != 0; i++) {
		printf("plese enter a number:");
		scanf_s("%d", &num_1);
		printf("plese enter another number:");
		scanf_s("%d", &num_2);
	}
	printf("The find nomber");*/



	// תרגיל מס 24 // פולינדרום 


int num_1 =0, num_2 = 0, num_3 =0;

printf("pleese ente a number: ");
scanf_s("%d", &num_1);

num_3 = num_1;

while (num_1 != 0) {

	num_2 = num_2 * 10 + num_1 % 10;

	num_1 = num_1 / 10;
}
if (num_2 == num_3)
printf("The number is polindrom!");
else
printf("The num ber is not polindrom!");


}






















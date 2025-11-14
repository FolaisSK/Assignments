import java.util.Scanner;

public class AverageGrade {

public static void main (String[]args) {

Scanner input = new Scanner(System.in);

System.out.print("Enter first score :");
double firstScore = input.nextDouble();

System.out.print("Enter second score :");
double secondScore = input.nextDouble();

System.out.print("Enter third score :");
double thirdScore = input.nextDouble();

double average = (firstScore + secondScore + thirdScore) / 3;

System.out.println("The average score is " + average);

if (average >= 90 && average <= 100) {
System.out.println("A");
} else if (average >= 80 && average < 90) {
System.out.println("B");
} else if (average >= 70 && average < 80) {
System.out.println("C");
} else if (average >= 60 && average < 70) {
System.out.println("D");
} else if (average >= 0 && average < 60) {
System.out.println("F");
} 

}

}
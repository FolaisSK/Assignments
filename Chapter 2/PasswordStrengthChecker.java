import java.util.Scanner;

public class PasswordStrengthChecker {

public static void main (String[]args) {

Scanner input = new Scanner(System.in);

System.out.print("Enter Password :");

String password = input.nextLine();

int length = password.length();

if (length > 6 && length <=10) {

System.out.print("Medium");

} else if (length < 6) {

System.out.print("Weak");

} else if (length > 10) {

System.out.print("Strong");

} else if (length < 1) {

System.out.print("Invalid");

}

}

}


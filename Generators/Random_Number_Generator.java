package Generators;
import java.util.Random;
import java.util.Scanner;

public class Random_Number_Generator {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter the upper limit for the random number (inclusive): ");

        int upperLimit = scan.nextInt();
        if (upperLimit <= 0) {
            System.out.println("Please enter a positive integer.");
            scan.close();
            return;
        }

        Random random = new Random();
        int randomNumber = random.nextInt(upperLimit) + 1;
        System.out.println(randomNumber);
        scan.close();
    }
}
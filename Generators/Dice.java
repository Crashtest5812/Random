package Generators;

import java.util.Random;
import java.util.Scanner;

public class Dice {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of sides on the dice: ");

        int sides = scanner.nextInt();
        if (sides <= 0) {
            System.out.println("Please enter a positive integer.");
            scanner.close();
            return;
        }

        Random random = new Random();
        int result = random.nextInt(sides) + 1;
        System.out.println("You rolled: " + result);
        scanner.close();
    }
}

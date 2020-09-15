package com.company;
import java.util.Scanner;

public class Task2 implements Mainable{
    public void _main(){
        Scanner in = new Scanner(System.in);
        System.out.print("Input a number: ");
        int num = in.nextInt();
        if(num>12){
            System.out.println("Error");
        }
        if (num>0 & num <=2){
            System.out.println("Winter");
        }
        if (num>=3 & num <=5){
            System.out.println("Spring");
        }
        if (num>=6 & num <=8){
            System.out.println("Summer");
        }
        if (num>=9 & num <=11){
            System.out.println("Autumn");
        }
        if (num==12){
            System.out.println("Winter");
        }

    }
}

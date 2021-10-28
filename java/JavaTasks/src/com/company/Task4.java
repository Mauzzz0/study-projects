package com.company;
import java.util.Scanner;

public class Task4 implements Mainable{
    public void _main(){
        Scanner in = new Scanner(System.in);
        System.out.print("Input a number: ");
        int num = in.nextInt();

        int res = 1;
        for (int i=1; i<=num;i++){
            res = res *i;
        }
        System.out.println(res);
    }
}

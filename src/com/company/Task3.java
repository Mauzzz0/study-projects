package com.company;
import java.util.Scanner;

public class Task3 implements Mainable{
    public void _main(){
        Scanner in = new Scanner(System.in);
        System.out.print("Input a number: ");
        int num = in.nextInt();

        int res = 1;
        int isFound = 0 ;
        while(res<=num){
            if(res == num){
                isFound = 1;
                System.out.println("YES YES YES");
            }
            res = res*2;
        }
        if (isFound ==0){
            System.out.println("NO NO NO");
        }
    }
}

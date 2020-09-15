package com.company;
import java.util.Scanner;

public class Task5 implements Mainable{
    public void _main(){
        Scanner in = new Scanner(System.in);
        System.out.print("Input a number: ");
        int num = in.nextInt();

        int isFound = 0;
        while (isFound ==0){
            num = num +1;
            int tmp_num = num; // 4567
            int _1 = tmp_num%10;
            int _2 = (tmp_num%100-_1)/10;
            int _3 = (tmp_num%1000-_2-_1)/100;
            int _4 = (tmp_num-_1-_2-_3)/1000;
            if (_1 != _2 & _1 != _3 & _1 != _4 & _2 != _3 & _2 != _4 & _3 != _4){
                System.out.println(num);
                isFound = 1;
            }


        }
    }
}

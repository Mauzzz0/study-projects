package com.company;
import java.lang.Math;

public class Task1 {
    public static void Task1Main(){

        double[] arr = {0,0,0,0,0,0,0,0,0,0};
        for (int i =0; i<10;i++){
            double rnd = Math.random();
            arr[i]= rnd;
        }

        double sum =0;
        for (int i =0; i<10;i++){
            sum = sum + arr[i];
        }
        System.out.println(sum/10);

        double _min = 2;
        double _max = 0;
        for (int i =0; i<10;i++){
            if (arr[i]>_max){
                _max = arr[i];
            }
            if (arr[i]<_min){
                _min = arr[i];
            }
        }
        System.out.println(_min);
        System.out.println(_max);

    }

}

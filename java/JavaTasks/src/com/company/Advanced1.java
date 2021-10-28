package com.company;

import java.util.stream.*;

public class Advanced1 implements Mainable{
    public static void Advanced1MainInt(int x1, int x2, int y1, int y2){
        int x = Math.abs(x1-x2);
        int y = Math.abs(y2-y1);
        double n = Math.sqrt(x*x+ y*y);
        System.out.println(n);
    }

    public static void Advanced1MainDouble(double x1, double x2, double y1, double y2){
        double x = Math.abs(x1-x2);
        double y = Math.abs(y2-y1);
        double n = Math.sqrt(x*x+ y*y);
        System.out.println(n);
    }

    public static void Advanced1MainMasha(int x1, int x2, int y1, int y2){
        int x = x1-x2; int y = y2-y1;
        double n = Math.sqrt(x*x+ y*y);
        System.out.println(n);
    }

    public void _main(){
        double x1,x2,y1,y2;
        x1 = 10; x2 = 20; y1 = 30; y2=40;
        System.out.println(Math.sqrt(Math.abs(x1-x2)*Math.abs(x1-x2)+ Math.abs(y2-y1)*Math.abs(y2-y1)));
    }

    public static double getDistance(int x1, int x2, int y1, int y2){
        //x1 = 3; x2 = 5; y1 = 6; y2 = 9;
        int x = x2-x1; int y = y2-y1;
        double n = Math.sqrt(x*x+ y*y);
        System.out.println(n);
        return n;
    }


}

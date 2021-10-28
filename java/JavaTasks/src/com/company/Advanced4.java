package com.company;

public class Advanced4 implements Mainable{
    public void _main(){
        String input = "28.12.2019";
        String[] _input = input.split("\\.");
        int day = Integer.parseInt(_input[0]);
        int month = Integer.parseInt(_input[1]);
        int year = Integer.parseInt(_input[2]);
        int offset = 0;

        if (isYearLeap(year)){
            offset = 1;
        }
        if (month == 1){
            System.out.println(isOdd(day));
        }
        if (month == 2){
            System.out.println(isOdd(day+1));
        }
        if (month == 4 | month == 5 | month == 8 | month ==12){
            System.out.println(isOdd(day+offset));
        }
        if (month == 3  | month == 6 | month == 7 | month == 9 | month == 10 | month == 11){
            System.out.println(isOdd(day+offset+1));
        }
    }

    public static Boolean isYearLeap(int year){
        if (year%400 == 0){
            return true;
        }
        return year % 4 == 0 & year % 100 != 0;
    }

    public static Boolean isOdd(int input){
        return (input%2==0);
    }
}
/*

        if (month == 3){
            System.out.println(isOdd(day+offset+1));
        }
        if (month == 5){
            System.out.println(isOdd(day+offset));
        }
        if (month == 7){
            System.out.println(isOdd(day+offset+1));
        }
        if (month == 8){
            System.out.println(isOdd(day+offset));
        }
        if (month == 9){
            System.out.println(isOdd(day+offset+1));
        }
        if (month == 10){
            System.out.println(isOdd(day+offset+1));
        }
        if (month == 11){
            System.out.println(isOdd(day+offset+1));
        }
        if (month == 12){
            System.out.println(isOdd(day+offset));
        } */

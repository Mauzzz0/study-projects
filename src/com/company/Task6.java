package com.company;

public class Task6 {
    public static void Task6Main(){
        int cur1 = 1;
        int cur2 = 1;
        int _cur;

        for (int i=0; i<11;i++){
            _cur =cur1+cur2;
            System.out.println(_cur);
            cur1 = cur2;
            cur2 = _cur;
        }
    }
}

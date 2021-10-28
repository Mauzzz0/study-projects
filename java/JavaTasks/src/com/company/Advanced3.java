package com.company;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Advanced3 implements Mainable {
    public void _main(){
        Scanner in = new Scanner(System.in);
        Map<String,Integer> dict = new HashMap<String,Integer>();

        for (int i=0; i<4; i++)
        {
            String curStr = in.nextLine();
            try
            {
                int countOfCur = dict.get(curStr);
                dict.replace(curStr,countOfCur+1);
            }
            catch (Exception ex)
            {
                dict.put(curStr,1);
            }
        }
        int a =10;
    }

}


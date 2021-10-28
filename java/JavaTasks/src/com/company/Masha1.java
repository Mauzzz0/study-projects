package com.company;

public class Masha1 {
    static String[] mass = {"aadd"};
    public static void W_2_2()
    {
        char[] ch2 = new char[26];
        for(int i=0; i < 10; i++)
        {
            int sum=0;
            String str = mass[i];
            char[] ch = new char[str.length()];
            for(int j=0; j<str.length(); j++)
            {
                ch[j] = str.charAt(j);
                String let = String.valueOf(ch[j]);
                int n = 0;
                for (int h =0; h<=sum; h++)
                {
                    String let2 = String.valueOf(ch2[h]);
                    if(let.equalsIgnoreCase(let2)) n++;
                }
                if (n==0)
                {
                    ch2[sum] = ch[j];
                    sum++;
                }
            }
            System.out.println("В строке " + (i+1) + ": " + sum + " разных буквы");

            int[] nums = new int[5];

            nums = new int[5];
        }
    }
}

package com.bsbo0419.Semak.Shell;

import java.util.ArrayList;
import java.util.Random;

public class Generator {
    public static void Random(int len,ArrayList<Integer> array){
        Random rnd = new Random();
        for (int i=0; i<len;i++){
            array.add(rnd.nextInt(10000000));
        }
    }

    public static void Sequence(int len,ArrayList<Integer> array){
        for (int i=0; i<len;i++){
            array.add(i);
        }
    }
    public static void SequenceReverse(int len,ArrayList<Integer> array){
        for (int i=len-1; i>=0;i--){
            array.add(i);
        }
    }

    public static boolean isSorted(ArrayList<Integer> array){
        for (int i=0; i<array.size()-1;i++){
            if (array.get(i) > array.get(i+1)){
                return false;
            }
        }
        return true;
    }
}
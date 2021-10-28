package com.bsbo0419.Semak.Shell;
import com.bsbo0419.Semak.Main;
import java.util.ArrayList;

import static com.bsbo0419.Semak.Shell.ShellSorting.SortMultithreading;

public class main implements Main.Mainable {


    public void _main(){
        ArrayList<Integer> storage = new ArrayList<Integer>();
        Generator.SequenceReverse(2000000,storage);
        SortMultithreading(storage);
        //System.out.println(Generator.isSorted(storage));
        int a =10;
    }
}
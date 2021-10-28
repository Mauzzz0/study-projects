package com.bsbo0419.Semak.Shell;

import java.util.*;

public class ShellSorting{

    public static void Sort(ArrayList<Integer> storage){
        for (int step = storage.size() / 2; step > 0; step /= 2) {
            for (int i = step; i < storage.size(); i++) {
                for (int j = i - step; j >= 0 && storage.get(j) > storage.get(j + step) ; j -= step) {
                    int x = storage.get(j);
                    storage.set(j,storage.get(j + step));
                    storage.set(j + step,x);
                }
            }
        }
    }

    public static void LinearMerge(ArrayList<Integer> matrix){
        /// TODO: Слияние
        long startTime = System.currentTimeMillis();
        Object[] temporary_object_array = matrix.toArray();
        int[] temporary_result_array = new int[matrix.size()];
        for (int i=0; i<matrix.size(); i++)
        {
            temporary_result_array[i] = (int)temporary_object_array[i];
        }
        Merge.sort(temporary_result_array,0,temporary_result_array.length-1);
        long endTime = System.currentTimeMillis();
        System.out.println("Classic merge sort execution time: " + (endTime-startTime) + "ms");
    }

    public static void SortMultithreading(ArrayList<Integer> storage){
        ArrayList<ArrayList> matrix = new ArrayList<>();
        Scanner in = new Scanner(System.in);
        int _start=0;
        int _end =0;
        int num=0;


        // Ввод кол-ва потоков
        boolean isFound = false;
        while(!isFound){
            System.out.println("Write amount of running threads: ");
            num = in.nextInt();
            if (num*5 > storage.size()){ // Длинна должна быть минимум в 5 раз больше кол-ва потоков
                System.out.println("The number of threads must be more than 5 times the length.");
            }
            else {
                isFound = true;
            }
        }

        // Деление на равные подлисты
        for(int i=0; i<num;i++){
            int step = (int)(Math.ceil(storage.size()/(double)num));

            if (i==0){
                _end = step;
            } else if( i==num-1){
                _start = _end;
                _end = storage.size();
            } else {
                _start = _end;
                _end += step;
            }
            ArrayList<Integer> tmp = new ArrayList<>();
            for(int j=_start; j<_end;j++){
                tmp.add(storage.get(j));
            }
            matrix.add(tmp);
        }

        ArrayList<Thread> thrds = new ArrayList<>();
        for (int i=0;i<num;i++){
            int finalI = i;
            thrds.add(new Thread(() -> Sort(matrix.get(finalI))));
        }
        for (Thread thrd : thrds) {
            thrd.start();
        }

        while (true){
            int count =0;
            for (Thread x: thrds){
                if (!x.isAlive()) {
                    count ++;
                }
            }
            if (count == thrds.size()){
                break;
            }
        }

        // Выход отсортированных сублистов
        System.out.println("Sublists sorted");
        ArrayList<Integer> unsortedresult = new ArrayList<>();
        for (ArrayList arrayList : matrix) {
            unsortedresult.addAll(arrayList);
        }

        LinearMerge(unsortedresult);

    }
}
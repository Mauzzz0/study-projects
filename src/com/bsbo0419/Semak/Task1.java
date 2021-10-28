package com.bsbo0419.Semak;

public class Task1 implements Main.Mainable {
    public void _main(){
        new Thread(() -> {
            try {
                Run(1);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        new Thread(() -> {
            try {
                Run(2);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        new Thread(() -> {
            try {
                Run(3);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
    }

    public void Run(int g) throws InterruptedException {
        for (int i=0; i<10; i++) {
            System.out.println("Thread " + g);
            Thread.sleep(100);
        }
    }
}
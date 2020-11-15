package com.bsbo0419.Semak;

import java.util.ArrayList;

public class Task2 implements Main.Mainable {
    public ArrayList storage = new ArrayList();
    public ArrayList storage1 = new ArrayList();
    public ArrayList storage2 = new ArrayList();

    public void _main(){
        for (int i=0; i<10; i++){
            storage.add(0);
            storage1.add(0);
            storage2.add(0);
        }

        new Thread(() -> Read(0)).start();
        new Thread(() -> Read(1)).start();
        new Thread(() -> Write(0)).start();
        new Thread(() -> Write(2)).start();
        new Thread(() -> Write(1)).start();
        new Thread(() -> Read(2)).start();
    }



    public void Write(int g){
        ArrayList _storage;
        switch(g){
            case 0:
                _storage = storage;
                break;
            case 1:
                _storage = storage1;
                break;
            case 2:
                _storage = storage2;
                break;
            default:
                _storage = null;
                System.out.println("DEFAULT");
                break;
        }

        for (int i=0;i<10;i++){
            _storage.set(i,i);
            System.out.println("Write: "+i+" to pos "+i);
        }
    }

    public void Read(int g){
        ArrayList _storage;
        switch(g){
            case 0:
                _storage = storage;
                break;
            case 1:
                _storage = storage1;
                break;
            case 2:
                _storage = storage2;
                break;
            default:
                _storage = null;
                System.out.println("DEFAULT");
                break;
        }
        for (int i=0;i<10;i++){
            System.out.println("Read: "+_storage.get(i)+" from pos "+i);
        }
    }
}
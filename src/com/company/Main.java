package com.company;

interface Mainable{
    public void _main();
}

public class Main {

    public static void main(String[] args) {
        Mainable tmp = new Advanced2();
        tmp._main();
    }
}

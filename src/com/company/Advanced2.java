package com.company;

public class Advanced2 implements Mainable{
    public void _main(){
        for (int j=0; j<10;j++){ // Повторять следующий алгоритм n раз

        String str = "aaaaaaAAAAAAbbbBBBBBc"; // Просто тестовая строка на вход, можно получать её сканером
        char[] ch = new char[str.length()];  // Создаю массив букв такой же длины, что и строка
        for (int i = 0; i < str.length(); i++) { //
            ch[i] = str.charAt(i);               // Заполняется массив буквами
        }

        int[] letters = new int[26];                   // Массив длины 26, по одному индексу на каждую букву
        for (int i=0; i<26; i++) { letters[i] = 0; }    // Заполняется нулями

        for (int i=0; i<ch.length;i++){      // В цикле перебираются все буквы из массива "ch"
            int current_letter = Character.toLowerCase(ch[i]);                 // Очередную букву перевожу в нижний регистр
            if (current_letter != 32) {  // Проверка "ЕСЛИ ЭТО НЕ ПРОБЕЛ"      // И конвертирую в число по таблице ASCII
                letters[current_letter - 97]++; // Если это не пробел, то
            }                                   // прибавляю единичку по тому индексу,
        }                                       // которое число имеет в таблице ASCII и отнимаю 97, и так получается:
        //letters[0] - колво букв "a", letters[1] - "b", letters[2] - "c", letters[1] - "d" ......
        int counter = 0;  // Счётчик, который будет считать количество !ненулевых! цифр в массиве letters
        for (int i=0; i<letters.length;i++){ // Перебор всех значений в массиве letters
            if (letters[i] != 0) { counter++; }
        }
        System.out.println(counter); // Вывод ненулевых цифр в массиве  <=> кол-во уникальных букв в строке
    }}
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices.ComTypes;
using System.Text;
using System.Threading.Tasks;

namespace OperatingSystem._3_4pairs_My
{
    class Word
    {
        //char l1;  // l1 l2 l3 l4 l5
        //char l2;
        //char l3;
        //char l4;
        //char l5;
        char[] letters = new char[5];
        string finishword;

        public Word(string input, string _finish)
        {
            letters[0] = input[0];
            letters[1] = input[1];
            letters[2] = input[2];
            letters[3] = input[3];
            letters[4] = input[4];
            finishword = _finish;
        }

        public bool Plus(int n = 4)
        {
            if (letters[n] != 'z')
            {
                if (ToString() == finishword)
                {
                    Console.WriteLine("end");
                    return true;
                }
                else
                {
                    letters[n]++;
                }
            }
            else if (letters[n] == 'z' && n!=0)
            {
                if (ToString() == finishword)
                {
                    Console.WriteLine("end");
                    return true;
                }
                else
                {
                    letters[n] = 'a';
                    Plus(n - 1);
                }
            }
            return false;
        }

        public override string ToString()
        {
            string tmp = "";
            return tmp + Convert.ToString(letters[0]) + Convert.ToString(letters[1]) + Convert.ToString(letters[2]) + Convert.ToString(letters[3]) + Convert.ToString(letters[4]);
        }
    }
}

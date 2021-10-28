using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Security;
using static System.Console;
using System.Security.Cryptography;
using System.Dynamic;

namespace OperatingSystem
{

    class SHA256pasha
    {
        public static bool br1;
        public static bool br2;
        public static bool br3;
        public static bool br4;
        public static int iteration = 0;
        static public string ComputeHash(char[] input, HashAlgorithm algorithm)
        {
            Byte[] inputBytes = Encoding.UTF8.GetBytes(input);
            Byte[] hashedBytes = algorithm.ComputeHash(inputBytes);
            return (BitConverter.ToString(hashedBytes)).Replace("-","");
        }

        static public void fakeMain()
        {            
            char[] chars = { 'a', 'a', 'a', 'a', 'a' };
            //CoreRecursFunc(0, "11770b3ea657fe68cba19675143e4715c8de9d763d3c21a85af6b7513d43997d", chars);
            Write(chars[0]);
            Write(chars[1]);
            Write(chars[2]);
            Write(chars[3]);
            Write(chars[4]);
            ReadLine();
        }

        static public void BruteforceLinear(string _start, string _finish, string result)
        {
            int[] start = { 0, 0, 0, 0, 0 };
            int[] finish = { 0, 0, 0, 0, 0 };
            int[] current = { 0, 0, 0, 0, 0 };
            
            for (int i=0; i<5; i++)
            {
                start[i] = Convert.ToInt32(_start[i]);
                finish[i] = Convert.ToInt32(_finish[i]);
                current[i] = Convert.ToInt32(_start[i]);
            }

            for (int i = 4; i>=0; i--)
            {
                for (int j = start[i]; j <= finish[i]; j++)
                {
                    current[i] = j;
                    Write(current[0] + " ");
                    Write(current[1] + " ");
                    Write(current[2] + " ");
                    Write(current[3] + " ");
                    Write(current[4] + " ");
                    WriteLine();
                }
            }
        }
        static public void BruteforceRecursive(char[] _start, char[] _finish, string result)
        {
            // if () {}
            char[] cur = _start;
            if (_start[4] < 90)
            {
                cur[4]++; 
            }
            else
            {
                // AAAAAAAAAA
            }
        }

        static public void WordGen()
        {
            char start = 'A';
            char finish = 'C';
            char[] current = { 'A', 'A', 'A', 'A', 'A' };

            for (int i=0; i < 5; i++)
            {
                for (int j=65; j<=Convert.ToInt32(finish); j++)
                {
                    current[i] = (char)j;
                    if (j== Convert.ToInt32(finish))
                    Write(current[0] + " ");
                    Write(current[1] + " ");
                    Write(current[2] + " ");
                    Write(current[3] + " ");
                    Write(current[4] + "    ");
                    Write(current[4] + " ");
                    Write(current[3] + " ");
                    Write(current[2] + " ");
                    Write(current[1] + " ");
                    Write(current[0] + " ");
                    WriteLine();
                }
            }
            ReadKey();
        }

        public static void CoreRecursFunc(int i, string hash, char[] chars)
        {
            while (true)
            {
                string res = ComputeHash(chars, new SHA256CryptoServiceProvider()).ToLower();
                if (i != 4)
                    CoreRecursFunc(i + 1, hash, chars);
                if (!br1 && res == hash)
                    br1 = true;
                if (chars[i] == 'z' || br1)
                    break;
                Write(res+"    ");
                Write(chars[0]);
                Write(chars[1]);
                Write(chars[2]);
                Write(chars[3]);
                Write(chars[4]);
                Write("    "+iteration);
                WriteLine();
                chars[i]++;
                iteration++;
            }
            if (br1)
                return;
            chars[i] = 'a';
        }
    }
}

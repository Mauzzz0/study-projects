using System.Threading;
using System.Security.Cryptography;
using static System.Console;
using System.Text;
using System;

namespace OperatingSystem._3_4pairs_My
{
    class SHA_Main
    {
        ///static Thread thrd1, thrd2, thrd3, thrd4, thrd5, thrd6, thrd7, thrd8;
        ///static Thread[] Threads = { thrd1, thrd2, thrd3, thrd4, thrd5, thrd6, thrd7, thrd8 };
        static bool isFound = false;
        private static SHA256 sha256Hash;
        public static void fakeMain()
        {
            WriteLine("HASH: ");
            string hash = "68a55e5b1e43c67f4ef34065a86c4c583f532ae8e3cda7e36cc79b611802ac07";

            Word word1 = new Word("aaaaa","daaab");
            Word word2 = new Word("daaaa","gaaab");
            Word word3 = new Word("gaaaa","jaaab");
            Word word4 = new Word("jaaaa","maaab");
            Word word5 = new Word("maaaa","paaab");
            Word word6 = new Word("paaaa","saaab");
            Word word7 = new Word("saaaa","vaaab");
            Word word8 = new Word("vaaaa","zzzzz");

            Thread thrd1 = new Thread(new ParameterizedThreadStart((x) => Brute(word1,hash))); thrd1.Name = "1";
            Thread thrd2 = new Thread(new ParameterizedThreadStart((x) => Brute(word2,hash))); thrd2.Name = "2";
            Thread thrd3 = new Thread(new ParameterizedThreadStart((x) => Brute(word3,hash))); thrd3.Name = "3";
            Thread thrd4 = new Thread(new ParameterizedThreadStart((x) => Brute(word4,hash))); thrd4.Name = "4";
            Thread thrd5 = new Thread(new ParameterizedThreadStart((x) => Brute(word5,hash))); thrd5.Name = "5";
            Thread thrd6 = new Thread(new ParameterizedThreadStart((x) => Brute(word6,hash))); thrd6.Name = "6";
            Thread thrd7 = new Thread(new ParameterizedThreadStart((x) => Brute(word7,hash))); thrd7.Name = "7";
            Thread thrd8 = new Thread(new ParameterizedThreadStart((x) => Brute(word8,hash))); thrd8.Name = "8";
            //Thread[] Threads = { thrd1, thrd2, thrd3, thrd4, thrd5, thrd6, thrd7, thrd8 };

            thrd1.Start();
            thrd2.Start();
            thrd3.Start();
            thrd4.Start();
            thrd5.Start();
            thrd6.Start();
            thrd7.Start();
            thrd8.Start();


            ReadLine();
        }

        public static void Brute(Word word, string hash)
        {
            while (true && !(isFound))
            {
                //string hashed = ComputeHash(word.ToString(), new SHA256CryptoServiceProvider()); // slower
                string hashed = ComputeHashAlt(word.ToString());                                   // faster
                //WriteLine(hash + "   " + hashed);   x10 runtime
                if (hashed == hash)
                {
                    WriteLine("я нашёл");
                    WriteLine(word.ToString());
                    isFound = true;
                    break;
                }
                bool CanGoOn = word.Plus();
                if (CanGoOn) { break; }
                //WriteLine(word.ToString());   x10 runtime
            }
        }

        public static string ComputeHash(string input, HashAlgorithm algorithm) // slower
        {
            Byte[] inputBytes = Encoding.UTF8.GetBytes(input);
            Byte[] hashedBytes = algorithm.ComputeHash(inputBytes);
            return ((BitConverter.ToString(hashedBytes)).Replace("-", "")).ToLower();
        }

        public static string ComputeHashAlt(string input)  // faster
        {
            sha256Hash = SHA256.Create();
            byte[] bytes = sha256Hash.ComputeHash(Encoding.ASCII.GetBytes(input));
            StringBuilder builder = new StringBuilder();
            foreach (var t in bytes)
                builder.Append(t.ToString("x2"));
            return builder.ToString();
        }
    }
}

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

    class SHA256
    {
        static public string ComputeHash(string input, HashAlgorithm algorithm)
        {
            Byte[] inputBytes = Encoding.UTF8.GetBytes(input);
            Byte[] hashedBytes = algorithm.ComputeHash(inputBytes);
            return (BitConverter.ToString(hashedBytes)).Replace("-","");
        }

        static public void fakeMain()
        {
            //string inp = "AAAAA";
            //WriteLine(ComputeHash(inp,new SHA256CryptoServiceProvider()));
            Bruteforce("AAAAA","CCCCC","AA");
        }

        static public void Bruteforce(string _start, string _finish, string result)
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
    }
}

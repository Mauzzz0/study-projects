using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace OperatingSystem._1_2pairs
{
    class Files
    {
        static public void fakeMain()
        {
            string path = @"C:\dirnew\new.txt";
            FileInfo fileInf = new FileInfo(path);
            if (fileInf.Exists)
            {
                WriteLine(fileInf.Name);
                WriteLine(fileInf.CreationTime);
                WriteLine(fileInf.Length);
            }
            /// info

            if (fileInf.Exists) { fileInf.Delete(); }
            /// delete

            if (fileInf.Exists)
            {
                fileInf.MoveTo(@"C:\dirnew1\new.txt");
            }
            /// move to

            if (fileInf.Exists)
            {
                fileInf.CopyTo(@"C:\dirnew1\new.txt", true);
            }
            /// copy
        }
    }
}

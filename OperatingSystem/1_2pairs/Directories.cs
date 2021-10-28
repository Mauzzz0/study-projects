using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace OperatingSystem._1_2pairs
{
    class Directories
    {
        static public void fakeMain()
        {
            WriteLine("Write a name of new catalogue");
            string dirname = "C:\\" + ReadLine();
            if (Directory.Exists(dirname))
            {
                WriteLine("Catalogues:");
                string[] dirs = Directory.GetDirectories(dirname);
                foreach(string s in dirs)
                {
                    WriteLine(s);
                }
                WriteLine();
                WriteLine("Files:");
                string[] files = Directory.GetFiles(dirname);
                foreach (string s in files)
                {
                    WriteLine(s);
                }
            }
            ///

            string newdir = "newdir";
            DirectoryInfo dirinfo = new DirectoryInfo(dirname);
            if (dirinfo.Exists)
            {
                dirinfo.Create();
            }
            dirinfo.CreateSubdirectory(newdir);
            ///

            WriteLine(dirinfo.Name);
            WriteLine(dirinfo.FullName);
            WriteLine(dirinfo.CreationTime);
            WriteLine(dirinfo.Root);
        }
    }
}

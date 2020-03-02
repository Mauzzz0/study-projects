using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using eXCEL = Microsoft.Office.Interop.Excel;

namespace ExcelParser
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> test1 = new List<string> { };
            test1.Add("1");
            test1.Add("2");
            test1.Add("3");


            Console.WriteLine(test1[0]);
            Console.WriteLine(test1[1]);
            Console.WriteLine(test1[2]);
            //Console.WriteLine(test1[3]);
            Console.ReadLine();
        }
    }
}

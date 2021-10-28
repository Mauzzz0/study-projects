using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;
//using static System.Console;
using Excelu = Microsoft.Office.Interop.Excel;

namespace ExcelParser
{
    class Excel
    {
        internal static Excelu.Application excelApp = new Excelu.Application();
        internal static Excelu.Workbook workBook = excelApp.Workbooks.Open(@"C:\Users\rusla\source\repos\ExcelTest\KBiSP-1-kurs-2-sem-_1_.xlsx");
        internal static Excelu.Worksheet sheet = (Excelu.Worksheet)workBook.Worksheets.get_Item(1);

        internal static void ScanDayOfWeeks()
        {
            for (int i = 1; i < Convert.ToInt32(sheet.UsedRange.Columns.Count); i++)
            {
                string res = (sheet.Cells[2, i].Text);

                if (res == "День недели")
                {
                    Program.Dayoweeks.Add(i);
                }
            }
        }
        static internal string DAYOFWEEK(int X)
        {
            int k = (X - 4) / 12;
            switch (k)
            {
                case 0:
                    return "Понедельник";
                case 1:
                    return "Вторник";
                case 2:
                    return "Среда";
                case 3:
                    return "Четверг";
                case 4:
                    return "Пятница";
                case 5:
                    return "Суббота";
            }
            return "INCORRECT DAY OF WEEK";
        }
    }
}

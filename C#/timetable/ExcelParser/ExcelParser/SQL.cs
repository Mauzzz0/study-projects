//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;
using System.Runtime.InteropServices;
using System.Data.SqlClient;
using static System.Data.SqlDbType;


namespace ExcelParser
{
    internal class SQL
    {
        internal static SqlConnection connection = new SqlConnection(@"Data Source=DESKTOP-J8T2PEA;Initial Catalog=University;Integrated Security=True");
        internal static SqlCommand cmd = new SqlCommand("Insert into TESTTABLE([Group name], [Pair name], [Pair digit], [Day of week], [Teacher name], Mod, [Pair type], Audience) values(@grname, @prname, @prdigit, @dofweek, @tname, @mod, @ptype, @aud)", connection);

        internal static void Parse()
        {
            try
            {
                Excel.ScanDayOfWeeks();
                connection.Open();

                foreach (int X in Program.Dayoweeks)
                {
                    foreach (int K in new int[] { 5, 9, 13 })
                    {
                        for (int j = 4; j <= 75; j++)
                        {
                            cmd.Parameters.Add("@grname", NVarChar).Value = Excel.sheet.Cells[2, X + K].Text;
                            cmd.Parameters.Add("@prname", NVarChar).Value = Excel.sheet.Cells[j, X + K].Text;
                            cmd.Parameters.Add("@prdigit", Int).Value = (j - 4) % 12;
                            cmd.Parameters.Add("@dofweek", NVarChar).Value = Excel.DAYOFWEEK(j);
                            cmd.Parameters.Add("@tname", NVarChar).Value = Excel.sheet.Cells[j, X + K + 2].Text;
                            cmd.Parameters.Add("@ptype", NVarChar).Value = Excel.sheet.Cells[j, X + K + 1].Text;
                            cmd.Parameters.Add("@aud", NVarChar).Value = Excel.sheet.Cells[j, X + K + 3].Text;
                            cmd.Parameters.Add("@mod", TinyInt).Value = j % 2 == 0 ? 1 : 0;


                            cmd.ExecuteNonQuery();
                            cmd.Parameters.Clear();
                        }
                    }
                }
            }
            finally
            {
                connection.Close();
                Excel.excelApp.Quit();
                Marshal.ReleaseComObject(Excel.workBook);
                Marshal.ReleaseComObject(Excel.excelApp);
            }
        }
        
    }
}

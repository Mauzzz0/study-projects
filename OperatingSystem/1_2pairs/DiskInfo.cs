using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace OperatingSystem._1_2pairs
{
    class DiskInfo
    {
        static public void fakeMain()
        {
            DriveInfo[] drives = DriveInfo.GetDrives();

            foreach(DriveInfo drive in drives)
            {
                WriteLine($"Name: {drive.Name}");
                WriteLine($"Type: {drive.DriveType}");
                if (drive.IsReady)
                {
                    WriteLine($"Size:{drive.TotalSize}");
                    WriteLine($"FreeSize:{drive.TotalFreeSpace}");
                    WriteLine($"Label:{drive.VolumeLabel}");
                }
                WriteLine();
            }
        }
    }
}

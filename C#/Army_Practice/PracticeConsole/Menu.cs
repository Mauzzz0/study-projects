using static System.Console;
using static PracticeConsole.Program;

namespace PracticeConsole
{
    class Menu
    {
        public void Show()
        {
            WriteLine();
            WriteLine("1: Вывести общие характеристики армии");
            WriteLine("2: Вывести информацию о каждом бойце");
            WriteLine("3: Нанести урон армии");
            Write("Введи команду: ");
            string cmd = ReadLine();
            Clear();
            switch (cmd)
            {
                case "1":
                    DisplayGeneral();
                    break;

                case "2":
                    DisplayAll();
                    break;

                case "3":
                    Write("Введите урон: ");
                    string inp = ReadLine();
                    int t = 0;
                    bool res = int.TryParse(inp,out t);
                    if (!res)
                    {
                        WriteLine("Некорректно");
                        break;
                    }
                    TakeDamage(t);
                    break;

                default:
                    WriteLine("Некорректно");
                    break;
            }
        }
    }
}

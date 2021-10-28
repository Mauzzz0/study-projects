using System.Collections.Generic;
using static System.Console;

namespace PracticeConsole
{
    class Program
    {
        static List<Base> Storage = new List<Base> { };
        static void Main(string[] args)
        {
            MakeArmy();
            var menu = new Menu();
            while (true)
            {
                menu.Show();
            }
        }

        static void MakeArmy()
        {
            Storage.Add(new Ballista("Ballista #1", "Stone,Loud Growing ShiftBludgeoning Absorption", 10, 535, 54));
            Storage.Add(new Ballista("Ballista #2", "Stone,Loud Growing ShiftBludgeoning Absorption", 0, 535, 54)); // Демонстрация 0 патронов
            Storage.Add(new Bard("Bard #1", 30, "Glass Armor", 93, 3));
            Storage.Add(new Camel("Camel #1", 13, 12, 0));
            Storage.Add(new Camel("Camel #2", 13, 12, 0));
            Storage.Add(new Camel("Camel #3", 13, 12, 0));
            Storage.Add(new Druid("Druid #1", 30, "Glass Armor", 88, 10));
            Storage.Add(new Druid("Druid #2", 30, "Glass Armor", 88, 10));
            Storage.Add(new Elephant("Elephant #1", 15, 103, 50));
            Storage.Add(new Fighter("Fighter #1", 30, "Glass Armor", 85, 14));
            Storage.Add(new Fighter("Fighter #2", 30, "Glass Armor", 85, 14));
            Storage.Add(new Fighter("Fighter #3", 30, "Glass Armor", 85, 14));
            Storage.Add(new Rogue("Rogue #1", 20, "Leather Armor", 40, 13));
            Storage.Add(new Rider1("Rider #1", 0, 0, "Bard #2", 30, "Glass Armor", 93, 3, "Camel #4", 13, 12, 0));
        }

        static int GetHP()
        {
            int SUM = 0;
            foreach(Base X in Storage)
            {
                SUM += X.hp;
            }
            return SUM;
        }
        static int GetDamage()
        {
            int SUM = 0;
            foreach(Base X in Storage)
            {
                SUM += X.damage;
            }
            return SUM;
        }
        static int GetArmor()
        {
            int SUM = 0;
            foreach(Base X in Storage)
            {
                if (X is Unit)
                {
                    SUM += ((Unit)X).armor.defense;
                }
                if(X is Rider)
                {
                    SUM += ((Rider)X).armor;
                }
            }
            return SUM;
        }
        public static void DisplayAll()
        {
            foreach(Base X in Storage)
            {
                WriteLine();
                WriteLine(X.ToString());
            }
        }
        public static void DisplayGeneral()
        {
            int hp = GetHP();
            int damage = GetDamage();
            int armor = GetArmor();
            int count = Storage.Count;
            WriteLine();
            WriteLine("Общее здоровье армии: " + hp);
            WriteLine("Общий урон армии: " + damage);
            WriteLine("Общая броня армии: " + armor);
            WriteLine("Общая численность армии: " + count);
        }
        public static void TakeDamage(int takendamage)
        {
            List<Base> tmp = new List<Base> { }; // Т.к нельзя изменять используемую коллекцию внутри цикла foreach,
            takendamage -= GetArmor();           // то запомним в отдельный лист всех убитых, а затем их вычеркнем из главного листа
            if (takendamage <= 0) { return; }
            foreach(Base X in Storage)
            {
                if (X.hp <= takendamage)
                {
                    takendamage -= X.hp;
                    tmp.Add(X);
                }
                else
                {
                    X.TakeDamage(takendamage); // Изменение ХП в отдельном методе, чтобы не открывать изменение ХП всей программе
                    takendamage = 0;
                }
            }
            
            foreach(Base X in tmp)
            {
                Storage.Remove(X);
            }
        }
    }
}

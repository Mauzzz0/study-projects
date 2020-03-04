using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Army
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {

        ImageSource dis = new ImageSourceConverter().ConvertFromString("textures/icons/gray.png") as ImageSource;                  // Загрузка источников
        ImageSource Iball = new ImageSourceConverter().ConvertFromString("textures/icons/ballista.png") as ImageSource;            // изображений
        ImageSource Iel = new ImageSourceConverter().ConvertFromString("textures/icons/elephant.png") as ImageSource;              //
        ImageSource Icam = new ImageSourceConverter().ConvertFromString("textures/icons/icons8-camel-32.png") as ImageSource;      //
        ImageSource Idruid = new ImageSourceConverter().ConvertFromString("textures/Army/Originals/scr1_fr2.png") as ImageSource;  //
        ImageSource Irog = new ImageSourceConverter().ConvertFromString("textures/Army/Originals/npc3_fr1.png") as ImageSource;    //
        ImageSource Ibard = new ImageSourceConverter().ConvertFromString("textures/Army/Originals/gsd1_fr1.png") as ImageSource;   //
        ImageSource Ifig = new ImageSourceConverter().ConvertFromString("textures/Army/Originals/knt3_fr1.png") as ImageSource;    //
        
        
        internal static int[] start_digits = {0,0,0,0};   // Запоминание стартовых значений хп/брони/урона/количества
        internal static Random rnd = new Random();
        internal static List<Base> Storage = new List<Base> { };   // Главное хранилище
        abstract internal class Base
        {
            public string uname { get; protected set; }
            public int hp { get; protected set; }
            public int damage { get; protected set; }
            public Base()
            {
                this.hp = 0;
                this.damage = 0;
            }
            public void Kill()
            {
                this.hp = 0;
            }
            public void HpMinus(int x)
            {
                this.hp -= x;
            }
        }
        abstract class Unit : Base
        {
            public int armor { get; protected set; }
            public string armor_name { get; protected set; }
            public Unit()
            {
                this.armor = 0;
                this.armor_name = "NAME BY DEFAULT CONSTRUCTOR";
            }
        }
        abstract class Animal : Base
        {
            public int speed { get; protected set; }
            public Animal()
            {
                this.speed = 0;
            }
        }
        class Ballista : Base
        {
            public int ammo { get; protected set; }
            public string ammo_name { get; protected set; }
            public Ballista()
            {
                this.uname = "Bl"; ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                this.hp = 535;
                this.damage = 54;
                this.ammo = rnd.Next(0, 50);
                this.ammo_name = "Loud Growing ShiftBludgeoning Absorption";
            }
        }
        class Druid:Unit
        {
            public Druid()
            {
                this.uname = "D";
                this.armor = 10;
                this.armor_name = "Glass Armor";
                this.hp = 88;
                this.damage = 10;
            }
        }
        class Rogue : Unit
        {
            public Rogue()
            {
                this.uname = "R";
                this.armor = 20;
                this.armor_name = "Leather Armor";
                this.hp = 40;
                this.damage = 13;
            }
        }
        class Bard : Unit
        {
            public Bard()
            {
                this.uname = "Ba";
                this.armor = 30;
                this.armor_name = "Glass Armor";
                this.hp = 93;
                this.damage = 3;
            }
        }
        class Fighter : Unit
        {
            public Fighter()
            {
                this.uname = "F";
                this.armor = 30;
                this.armor_name = "Glass Armor";
                this.hp = 85;
                this.damage = 14;
            }
        }
        class Camel : Animal
        {
            public Camel()
            {
                this.uname = "C";
                this.speed = 13;
                this.hp = 12;
                this.damage = 0;
            }
        }
        class Elephant : Animal
        {
            public Elephant()
            {
                this.uname = "E";
                this.speed = 15;
                this.hp = 103;
                this.damage = 50;
            }
        }

        void ClearAll()
        {
            Storage.Clear();
            start_digits[0] = 0;
            start_digits[1] = 0;
            start_digits[2] = 0;
            start_digits[3] = 0;
            IBallista1.Source = dis;
            IBallista2.Source = dis;
            IBallista3.Source = dis;
            Idruid1.Source = dis;
            Idruid2.Source = dis;
            Idruid3.Source = dis;
            Irogue1.Source = dis;
            Irogue2.Source = dis;
            Irogue3.Source = dis;
            Ibard1.Source = dis;
            Ibard2.Source = dis;
            Ibard3.Source = dis;
            Ifighter1.Source = dis;
            Ifighter2.Source = dis;
            Ifighter3.Source = dis;
            Ielephant1.Source = dis;
            Ielephant2.Source = dis;
            Ielephant3.Source = dis;
            Icamel1.Source = dis;
            Icamel2.Source = dis;
            Icamel3.Source = dis;
        }  // Очищение всех данных для генерации новой армии
        void Generate()
        {
            ClearAll();
            int tmp = rnd.Next(1,4);
            for (int i = 0; i < tmp; i++)
            {
                Storage.Add(new Ballista());
            }

            tmp = rnd.Next(1, 4);
            for (int i = 0; i < tmp; i++)
            {
                Storage.Add(new Druid());
            }

            tmp = rnd.Next(1, 4);
            for (int i = 0; i < tmp; i++)
            {
                Storage.Add(new Rogue());
            }

            tmp = rnd.Next(1, 4);
            for (int i = 0; i < tmp; i++)
            {
                Storage.Add(new Bard());
            }

            tmp = rnd.Next(1, 4);
            for (int i = 0; i < tmp; i++)
            {
                Storage.Add(new Fighter());
            }

            tmp = rnd.Next(1, 4);
            for (int i = 0; i < tmp; i++)
            {
                Storage.Add(new Camel());
            }

            tmp = rnd.Next(1, 4);
            for (int i = 0; i < tmp; i++)
            {
                Storage.Add(new Elephant());
            }
            RefreshDigits(1);   // Передаю число 1, чтобы программа поняла, что это первое обновление цифр => необходимо запомнить стартовые значения в start_digits
        }

        int GetArmor()
        {
            int c = 0;
            foreach( Base X in Storage)
            {
                if (!(X is Camel | X is Elephant | X is Ballista))   // Если объект НЕ является Слоном/Верблюдом/Баллистой, то прибавить его броню к общему показателю
                {
                    c += ((Unit)X).armor;
                }
            }
            return c;
        }
        void CauseDmg(ref int damage)
        {
            List<Base> deletelist = new List<Base> { };   // внутри foreach нельзя изменять использующуюся коллекцию => занесу в список всех убитых и потом вычту из MainStorage
            damage -= GetArmor();
            //MessageBox.Show(Convert.ToString(GetArmor()));

            if (damage <= 0) { return; }


            foreach (Base X in Storage)
            {
                if (X.hp <= damage)
                {
                    damage -= X.hp;
                    X.Kill();  // Устанавливает для икса this.hp = 0, отдельным методом, чтобы не открывать возможность изменения hp для всего кода
                    deletelist.Add(X);
                }
                else
                {
                    X.HpMinus(damage); // Устанавливает для икса this.hp -= damage,  отдельным методом, чтобы не открывать возможность изменения hp для всего кода
                    damage = 0;
                }
            }

            foreach( Base X in deletelist) //   Пробегаемся по списку убитых и убираем их из MainStorage
            {
                Storage.Remove(X);
            }
        }
        void RefreshWindow()
        {
            int tmp_count = (from i in Storage where i.uname == "D" select i).Count(); // Druid
            switch (tmp_count)
            {
                case 0:
                    Idruid1.Source = dis;
                    Idruid2.Source = dis;
                    Idruid3.Source = dis;
                    break;
                case 1:
                    Idruid1.Source = Idruid;
                    Idruid2.Source = dis;
                    Idruid3.Source = dis;
                    break;
                case 2:
                    Idruid1.Source = Idruid;
                    Idruid2.Source = Idruid;
                    Idruid3.Source = dis;
                    break;
                case 3:
                    Idruid1.Source = Idruid;
                    Idruid2.Source = Idruid;
                    Idruid3.Source = Idruid;
                    break;
            }
            tmp_count = (from i in Storage where i.uname == "Bl" select i).Count(); // Ballista
            switch (tmp_count)
            {
                case 0:
                    IBallista1.Source = dis;
                    IBallista2.Source = dis;
                    IBallista3.Source = dis;
                    break;
                case 1:
                    IBallista1.Source = Iball;
                    IBallista2.Source = dis;
                    IBallista3.Source = dis;
                    break;
                case 2:
                    IBallista1.Source = Iball;
                    IBallista2.Source = Iball;
                    IBallista3.Source = dis;
                    break;
                case 3:
                    IBallista1.Source = Iball;
                    IBallista2.Source = Iball;
                    IBallista3.Source = Iball;
                    break;
            }
            tmp_count = (from i in Storage where i.uname == "R" select i).Count(); // Rogue
            switch (tmp_count)
            {
                case 0:
                    Irogue1.Source = dis;
                    Irogue2.Source = dis;
                    Irogue3.Source = dis;
                    break;
                case 1:
                    Irogue1.Source = Irog;
                    Irogue2.Source = dis;
                    Irogue3.Source = dis;
                    break;
                case 2:
                    Irogue1.Source = Irog;
                    Irogue2.Source = Irog;
                    Irogue3.Source = dis;
                    break;
                case 3:
                    Irogue1.Source = Irog;
                    Irogue2.Source = Irog;
                    Irogue3.Source = Irog;
                    break;
            }
            tmp_count = (from i in Storage where i.uname == "Ba" select i).Count(); // Bard
            switch (tmp_count)
            {
                case 0:
                    Ibard1.Source = dis;
                    Ibard2.Source = dis;
                    Ibard3.Source = dis;
                    break;
                case 1:
                    Ibard1.Source = Ibard;
                    Ibard2.Source = dis;
                    Ibard3.Source = dis;
                    break;
                case 2:
                    Ibard1.Source = Ibard;
                    Ibard2.Source = Ibard;
                    Ibard3.Source = dis;
                    break;
                case 3:
                    Ibard1.Source = Ibard;
                    Ibard2.Source = Ibard;
                    Ibard3.Source = Ibard;
                    break;
            }
            tmp_count = (from i in Storage where i.uname == "F" select i).Count(); // Fighter
            switch (tmp_count)
            {
                case 0:
                    Ifighter1.Source = dis;
                    Ifighter2.Source = dis;
                    Ifighter3.Source = dis;
                    break;
                case 1:
                    Ifighter1.Source = Ifig;
                    Ifighter2.Source = dis;
                    Ifighter3.Source = dis;
                    break;
                case 2:
                    Ifighter1.Source = Ifig;
                    Ifighter2.Source = Ifig;
                    Ifighter3.Source = dis;
                    break;
                case 3:
                    Ifighter1.Source = Ifig;
                    Ifighter2.Source = Ifig;
                    Ifighter3.Source = Ifig;
                    break;
            }
            tmp_count = (from i in Storage where i.uname == "E" select i).Count(); // Elephant
            switch (tmp_count)
            {
                case 0:
                    Ielephant1.Source = dis;
                    Ielephant2.Source = dis;
                    Ielephant3.Source = dis;
                    break;
                case 1:
                    Ielephant1.Source = Iel;
                    Ielephant2.Source = dis;
                    Ielephant3.Source = dis;
                    break;
                case 2:
                    Ielephant1.Source = Iel;
                    Ielephant2.Source = Iel;
                    Ielephant3.Source = dis;
                    break;
                case 3:
                    Ielephant1.Source = Iel;
                    Ielephant2.Source = Iel;
                    Ielephant3.Source = Iel;
                    break;
            }
            tmp_count = (from i in Storage where i.uname == "C" select i).Count(); // Camel
            switch (tmp_count)
            {
                case 0:
                    Icamel1.Source = dis;
                    Icamel2.Source = dis;
                    Icamel3.Source = dis;
                    break;
                case 1:
                    Icamel1.Source = Icam;
                    Icamel2.Source = dis;
                    Icamel3.Source = dis;
                    break;
                case 2:
                    Icamel1.Source = Icam;
                    Icamel2.Source = Icam;
                    Icamel3.Source = dis;
                    break;
                case 3:
                    Icamel1.Source = Icam;
                    Icamel2.Source = Icam;
                    Icamel3.Source = Icam;
                    break;
            }
        } // Обновление окна WPF
        void RefreshDigits(int n = 0)
        {
            int cur_hp = 0;
            int cur_dmg = 0;
            int cur_armor = 0;
            int cur_count = 0;
            int cur_ammo = 0;

            foreach(Base X in Storage)
            {
                cur_count++;  // Подсчёт количества
                cur_hp += X.hp;   // Подсчёт общего хп
                cur_dmg += X.damage;   // Подсчёт общего урона

                if  (!(X is Elephant | X is Camel | X is Ballista)) // Если X это не Слон/Верблюд/Баллиста, то прибавить броню к общему показателю брони
                {
                    cur_armor += ((Unit)X).armor;   // Подсчёт общей брони
                }

                if (X is Ballista)
                {
                    cur_ammo += ((Ballista)X).ammo;   // Подсчёт общего количества боеприпасов
                }
            }
            if (n == 1)  // Если это первое обновление цифр => только что сгенерировались войска => запомнить в start_digits стартовые показатели брони/хп и т.п.
            {
                start_digits[0] = cur_dmg;
                start_digits[1] = cur_hp;
                start_digits[2] = cur_armor;
                start_digits[3] = cur_count;
            }
            Tdamage.Text = $"{cur_dmg}/{start_digits[0]}";
            Thp.Text = $"{cur_hp}/{start_digits[1]}";
            Tarmor.Text = $"{cur_armor}/{start_digits[2]}";
            Tcount.Text = $"{cur_count}/{start_digits[3]}";
            Tammo.Text = $"{cur_ammo}";
        } // Обновление цифер в окне
        void RefreshToolTips()
        {
            List<Ballista> ballistalist = (from i in Storage where i.uname == "Bl" select (Ballista)i).ToList(); // Разложение общего MainStorage 
            List<Druid> druidlist = (from i in Storage where i.uname == "D" select (Druid)i).ToList();           // на локальные листы,
            List<Rogue> roguelist = (from i in Storage where i.uname == "R" select (Rogue)i).ToList();           // чтобы связать со
            List<Bard> bardlist = (from i in Storage where i.uname == "Ba" select (Bard)i).ToList();             // списками изображений юнитов
            List<Fighter> fighterlist = (from i in Storage where i.uname == "F" select (Fighter)i).ToList();     //
            List<Elephant> elephantlist = (from i in Storage where i.uname == "E" select (Elephant)i).ToList();  //
            List<Camel> camellist = (from i in Storage where i.uname == "C" select (Camel)i).ToList();           //

            List<Image> ballistaimages = new List<Image> { IBallista1, IBallista2, IBallista3 };  // Списки изображений
            List<Image> druidimages = new List<Image> { Idruid1, Idruid2, Idruid3 };              // 
            List<Image> rogueimages = new List<Image> { Irogue1, Irogue2, Irogue3 };              //
            List<Image> bardimages = new List<Image> { Ibard1, Ibard2, Ibard3 };                  //
            List<Image> fighterimages = new List<Image> { Ifighter1, Ifighter2, Ifighter3 };      //
            List<Image> elephantimages = new List<Image> { Ielephant1, Ielephant2, Ielephant3 };  //
            List<Image> camelimages = new List<Image> { Icamel1, Icamel2, Icamel3 };              //

            
            for (int i =0; i<3; i++)
            {
                try
                {
                    ballistaimages[i].ToolTip = String.Format("BALLISTA\nHP: {0}\nDmg: {1}\nAmmo: {2}\nAmmo: {3}", ballistalist[i].hp, ballistalist[i].damage, ballistalist[i].ammo, ballistalist[i].ammo_name);
                }
                catch (Exception) { ballistaimages[i].ToolTip = "Юнит отсутствует"; }
                try
                {
                    druidimages[i].ToolTip = String.Format("DRUID\nHP: {0}\nDmg: {1}\nArmor: {2}\nArmor: {3}", druidlist[i].hp, druidlist[i].damage, druidlist[i].armor, druidlist[i].armor_name);
                }
                catch (Exception) { druidimages[i].ToolTip = "Юнит отсутствует"; }
                try
                {
                    rogueimages[i].ToolTip = String.Format("ROGUE\nHP: {0}\nDmg: {1}\nArmor: {2}\nArmor: {3}", roguelist[i].hp, roguelist[i].damage, roguelist[i].armor, roguelist[i].armor_name);
                }
                catch (Exception) { rogueimages[i].ToolTip = "Юнит отсутствует"; }
                try
                {
                    bardimages[i].ToolTip = String.Format("BARD\nHP: {0}\nDmg: {1}\nArmor: {2}\nArmor: {3}", bardlist[i].hp, bardlist[i].damage, bardlist[i].armor, bardlist[i].armor_name);
                }
                catch (Exception) { bardimages[i].ToolTip = "Юнит отсутствует"; }
                try
                {
                    fighterimages[i].ToolTip = String.Format("FIGHTER\nHP: {0}\nDmg: {1}\nArmor: {2}\nArmor: {3}", fighterlist[i].hp, fighterlist[i].damage, fighterlist[i].armor, fighterlist[i].armor_name);
                }
                catch (Exception) { fighterimages[i].ToolTip = "Юнит отсутствует"; }
                try
                {
                    elephantimages[i].ToolTip = String.Format("ELEPHANT\nHP: {0}\nDmg: {1}\nSpeed: {2}", elephantlist[i].hp, elephantlist[i].damage, elephantlist[i].speed);
                }
                catch (Exception) { elephantimages[i].ToolTip = "Юнит отсутствует"; }
                try
                {
                    camelimages[i].ToolTip = String.Format("CAMEL\nHP: {0}\nDmg: {1}\nSpeed: {2}", camellist[i].hp, camellist[i].damage, camellist[i].speed);
                }
                catch (Exception) { camelimages[i].ToolTip = "Юнит отсутствует"; }
            }
        } // Обновление всплывающих подсказок

        public MainWindow()
        {
            InitializeComponent();
            CauseDmgButton.IsEnabled = false;
        }

        private void GenerateArmy(object sender, RoutedEventArgs e)
        {
            Generate();
            RefreshWindow();
            RefreshToolTips();
            CauseDmgButton.IsEnabled = true;
            int C = 0 + 1;
        }

        private void Cause_Dmg(object sender, RoutedEventArgs e)
        {
            if (!Int32.TryParse(Tinputdamage.Text, out int n))
            {
                MessageBox.Show("Is not digit");
            }
            else
            {
                //MessageBox.Show("[TEST]Is digit[TEST]");
                CauseDmg(ref n);
                RefreshWindow();
                RefreshToolTips();
                RefreshDigits();
                int c = 0 + 1; // Просто точка остановки для дебага
            }
        }
    }
}

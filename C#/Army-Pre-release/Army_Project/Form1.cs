using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Army_Project
{

    public partial class Name : Form
    {
        public class g
        {
            public static List<List<Array>> store_purp = new List<List<Array>>();
            public static List<List<Array>> store_green = new List<List<Array>>();
            public static List<Array> lost_purp = new List<Array>();
            public static List<Array> lost_green = new List<Array>();
            public static int starthp_purp = 0;
            public static int starthp_green = 0;
            public static Dictionary<int, string> UIDs = new Dictionary<int, string>(24);

        }
        public class f
        {
            public static void CheckPictures(List<List<Array>> purp, List<List<Array>> green,List<PictureBox> Pblist)
            {
                List<int> Alive_purp = new List<int>();
                foreach (List<Array> armytype in purp) // store  (soldiers_p)
                {
                    foreach (Array armyunits in armytype) // type of army (locl_a_p)
                    {
                        int uid = Convert.ToInt32(armyunits.GetValue(0));
                        Alive_purp.Add(uid);

                    }
                }
                foreach (int uid in Alive_purp)
                {
                    switch (uid)
                    {
                        case 1: Pblist[1].Visible = true; break;
                        case 2: Pblist[2].Visible = true; break;
                        case 3: Pblist[3].Visible = true; break;
                        case 4: Pblist[4].Visible = true; break;
                        case 5: Pblist[5].Visible = true; break;
                        case 6: Pblist[6].Visible = true; break;
                        case 7: Pblist[13].Visible = true; break;
                        case 8: Pblist[12].Visible = true; break;
                        case 9: Pblist[11].Visible = true; break;
                        case 10: Pblist[10].Visible = true; break;
                        case 11: Pblist[9].Visible = true; break;
                        case 12: Pblist[8].Visible = true; break;
                    }
                }


                List<int> Alive_green = new List<int>();
                foreach (List<Array> armytype in green) // store  (soldiers_p)
                {
                    foreach (Array armyunits in armytype) // type of army (locl_a_p)
                    {
                        int uid = Convert.ToInt32(armyunits.GetValue(0));
                        Alive_green.Add(uid);
                    }
                }
                foreach (int uid in Alive_green)
                {
                    switch (uid)
                    {
                        case 13: Pblist[20].Visible = true; break;
                        case 14: Pblist[21].Visible = true; break;
                        case 15: Pblist[22].Visible = true; break;
                        case 16: Pblist[23].Visible = true; break;
                        case 17: Pblist[24].Visible = true; break;
                        case 18: Pblist[25].Visible = true; break;
                        case 19: Pblist[14].Visible = true; break;
                        case 20: Pblist[15].Visible = true; break;
                        case 21: Pblist[16].Visible = true; break;
                        case 22: Pblist[17].Visible = true; break;
                        case 23: Pblist[18].Visible = true; break;
                        case 24: Pblist[19].Visible = true; break;
                    }
                }
            }


            public static void Victory(string way, List<PictureBox> Pblist, Label lbl, PictureBox kama)
            {
                foreach( PictureBox PB in Pblist)
                {
                    PB.Visible = false;
                }
                kama.Visible = true;
                lbl.Text = "Победили " + way + "\n" + "Впредь не воюйте, пацаны.";
            }
            public static void Attack(List<PictureBox> Pblist)
            {
                int Damage_purp = GetDamage(g.store_purp);
                int Health_purp = GetHealth(g.store_purp);
                int Armor_purp = GetArmor(g.store_purp);
                int Damage_green = GetDamage(g.store_green);
                int Health_green = GetHealth(g.store_green);
                int Armor_green = GetArmor(g.store_green);
                int Damage_taken_green = Damage_purp - Armor_green; // Damage received green by purp
                int Damage_taken_purp = Damage_green - Armor_purp; // Damage received purp by green


                foreach (List<Array> armytype in g.store_green) // purp attack green
                {
                    foreach (string[] armyunits in armytype.ToArray()) // purp attack green
                    {
                        int unit_hp = Convert.ToInt32(armyunits.GetValue(3));
                        if (unit_hp <= Damage_taken_green)
                        {
                            Damage_taken_green = Damage_taken_green - unit_hp;
                            int uid = Convert.ToInt32(armyunits.GetValue(0));
                            switch (uid)
                            {
                                case 1: Pblist[1].Visible = false; break;
                                case 2: Pblist[2].Visible = false; break;
                                case 3: Pblist[3].Visible = false; break;
                                case 4: Pblist[4].Visible = false; break;
                                case 5: Pblist[5].Visible = false; break;
                                case 6: Pblist[6].Visible = false; break;
                                case 7: Pblist[13].Visible = false; break;
                                case 8: Pblist[12].Visible = false; break;
                                case 9: Pblist[11].Visible = false; break;
                                case 10: Pblist[10].Visible = false; break;
                                case 11: Pblist[9].Visible = false; break;
                                case 12: Pblist[8].Visible = false; break;
                                case 13: Pblist[20].Visible = false; break;
                                case 14: Pblist[21].Visible = false; break;
                                case 15: Pblist[22].Visible = false; break;
                                case 16: Pblist[23].Visible = false; break;
                                case 17: Pblist[24].Visible = false; break;
                                case 18: Pblist[25].Visible = false; break;
                                case 19: Pblist[14].Visible = false; break;
                                case 20: Pblist[15].Visible = false; break;
                                case 21: Pblist[16].Visible = false; break;
                                case 22: Pblist[17].Visible = false; break;
                                case 23: Pblist[18].Visible = false; break;
                                case 24: Pblist[19].Visible = false; break;
                            }
                            armytype.Remove(armyunits);

                        }
                        else
                        {
                            unit_hp = unit_hp - Damage_taken_green;
                            Damage_taken_green = 0;
                            armyunits[3] = Convert.ToString(unit_hp);
                        }
                    }
                }

                foreach (List<Array> armytype in g.store_purp) // green attack purp
                {
                    foreach (string[] armyunits in armytype.ToArray()) // green attack purp
                    {
                        int unit_hp = Convert.ToInt32(armyunits.GetValue(3));
                        if (unit_hp <= Damage_taken_purp)
                        {
                            Damage_taken_purp = Damage_taken_purp - unit_hp;
                            int uid = Convert.ToInt32(armyunits.GetValue(0));
                            switch (uid)
                            {
                                case 1: Pblist[1].Visible = false; break;
                                case 2: Pblist[2].Visible = false; break;
                                case 3: Pblist[3].Visible = false; break;
                                case 4: Pblist[4].Visible = false; break;
                                case 5: Pblist[5].Visible = false; break;
                                case 6: Pblist[6].Visible = false; break;
                                case 7: Pblist[13].Visible = false; break;
                                case 8: Pblist[12].Visible = false; break;
                                case 9: Pblist[11].Visible = false; break;
                                case 10: Pblist[10].Visible = false; break;
                                case 11: Pblist[9].Visible = false; break;
                                case 12: Pblist[8].Visible = false; break;
                                case 13: Pblist[20].Visible = false; break;
                                case 14: Pblist[21].Visible = false; break;
                                case 15: Pblist[22].Visible = false; break;
                                case 16: Pblist[23].Visible = false; break;
                                case 17: Pblist[24].Visible = false; break;
                                case 18: Pblist[25].Visible = false; break;
                                case 19: Pblist[14].Visible = false; break;
                                case 20: Pblist[15].Visible = false; break;
                                case 21: Pblist[16].Visible = false; break;
                                case 22: Pblist[17].Visible = false; break;
                                case 23: Pblist[18].Visible = false; break;
                                case 24: Pblist[19].Visible = false; break;
                            }
                            armytype.Remove(armyunits);
                        }
                        else
                        {
                            unit_hp = unit_hp - Damage_taken_purp;
                            Damage_taken_purp = 0;
                            armyunits[3] = Convert.ToString(unit_hp);
                        }
                    }
                }

            }
            public static int GetHealth(List<List<Array>> x) // РАБОТАЕТ, НЕ ТРОГАЙ
            {
                int generalhp = 0;

                foreach (List<Array> armytype in x) // store  (soldiers_p)
                {
                    foreach (Array armyunits in armytype) // type of army (locl_a_p)
                    {


                        int unit_hp = Convert.ToInt32(armyunits.GetValue(3));
                        generalhp = generalhp + unit_hp;

                    }
                }

                return generalhp;
            }

            public static int GetArmor(List<List<Array>> x)
            {
                int generalarmor = 0;

                foreach (List<Array> armytype in x) // store  (soldiers_p)
                {
                    foreach (Array armyunits in armytype) // type of army (locl_a_p)
                    {


                        int loc_unit_armor = Convert.ToInt32(armyunits.GetValue(4));
                        generalarmor = generalarmor + loc_unit_armor;

                    }
                }

                return generalarmor;
            }

            public static int GetDamage(List<List<Array>> x)
            {
                int generaldamage = 0;

                foreach (List<Array> armytype in x) // store  (soldiers_p)
                {
                    foreach (Array armyunits in armytype) // type of army (locl_a_p)
                    {


                        int loc_unit_armor = Convert.ToInt32(armyunits.GetValue(2));
                        generaldamage = generaldamage + loc_unit_armor;

                    }
                }

                return generaldamage;
            }

            public static int GetCount(List<List<Array>> x)
            {
                int generalcount = 0;

                foreach (List<Array> armytype in x) // store  (soldiers_p)
                {
                    foreach (Array armyunits in armytype) // type of army (locl_a_p)
                    {


                        generalcount++;

                    }
                }

                return generalcount;
            }

            public static void init()
            {
                //Body of Main Function;

                // RND module
                Random rnd = new Random();
                int value = rnd.Next(1, 4);
                // RND module's finish

                // local army purple [uid, name, damage, health, armor, type, about]
                //                   [0    1     2       3       4      5     6]


                //////GLOBAL ARMY MAKING//////GLOBAL ARMY MAKING//////GLOBAL ARMY MAKING
                for (int i = 0; i <= 1; i++)
                {
                    if (i == 0)
                    {
                        string[] sh1 = { "1", "shield1", "501", "1001", "21", "Sheild unit", "its me, Armor" };
                        string[] sh2 = { "2", "shield2", "502", "1002", "22", "Sheild unit", "its me, Armor" };
                        string[] sh3 = { "3", "shield3", "503", "1003", "23", "Sheild unit", "its me, Armor" };
                        List<Array> sh0 = new List<Array> { };

                        value = rnd.Next(1, 4);
                        value = 2;

                        switch (value)
                        {
                            case 1:
                                sh0.Add(sh1);
                                break;
                            case 2:
                                sh0.Add(sh1);
                                sh0.Add(sh2);
                                break;
                            case 3:
                                sh0.Add(sh1);
                                sh0.Add(sh2);
                                sh0.Add(sh3);
                                break;

                        }


                        string[] kn1 = { "4", "knight1", "101", "1101", "31", "Knight soldier", "itsmeknight" };
                        string[] kn2 = { "5", "knight2", "102", "1102", "32", "Knight soldier", "itsmeknight" };
                        string[] kn3 = { "6", "knight3", "103", "1103", "33", "Knight soldier", "itsmeknight" };
                        List<Array> kn0 = new List<Array> { };

                        value = rnd.Next(1, 4);
                        value = 2;

                        switch (value)
                        {
                            case 1:
                                kn0.Add(kn1);
                                break;
                            case 2:
                                kn0.Add(kn1);
                                kn0.Add(kn2);
                                break;
                            case 3:
                                kn0.Add(kn1);
                                kn0.Add(kn2);
                                kn0.Add(kn3);
                                break;

                        }

                        string[] wz1 = { "7", "Wizard1", "101", "111", "21", "Wiz soldier", "itsmewiz" };
                        string[] wz2 = { "8", "Wizard2", "102", "112", "22", "Wiz soldier", "itsmewiz" };
                        string[] wz3 = { "9", "Wizard3", "103", "113", "23", "Wiz soldier", "itsmewiz" };
                        List<Array> wz0 = new List<Array> { };

                        value = rnd.Next(1, 4);
                        value = 2;

                        switch (value)
                        {
                            case 1:
                                wz0.Add(wz1);
                                break;
                            case 2:
                                wz0.Add(wz1);
                                wz0.Add(wz2);
                                break;
                            case 3:
                                wz0.Add(wz1);
                                wz0.Add(wz2);
                                wz0.Add(wz3);
                                break;

                        }

                        string[] mn1 = { "10", "mn1", "101", "111", "21", "Just monster", "mmmonster" };
                        string[] mn2 = { "11", "mn2", "102", "112", "22", "Just monster", "mmmonster" };
                        string[] mn3 = { "12", "mn3", "103", "113", "23", "Just monster", "mmmonster" };
                        List<Array> mn0 = new List<Array> { };

                        value = rnd.Next(1, 4);
                        value = 2;

                        switch (value)
                        {
                            case 1:
                                mn0.Add(mn1);
                                break;
                            case 2:
                                mn0.Add(mn1);
                                mn0.Add(mn2);
                                break;
                            case 3:
                                mn0.Add(mn1);
                                mn0.Add(mn2);
                                mn0.Add(mn3);
                                break;

                        }
                        g.store_purp.Add(sh0);
                        g.store_purp.Add(kn0);
                        g.store_purp.Add(wz0);
                        g.store_purp.Add(mn0);
                    }
                    else
                    {
                        string[] sh1 = { "13", "shield1", "501", "1001", "21", "Sheild unit", "its me, Armor" };
                        string[] sh2 = { "14", "shield2", "502", "1002", "22", "Sheild unit", "its me, Armor" };
                        string[] sh3 = { "15", "shield3", "503", "1003", "23", "Sheild unit", "its me, Armor" };
                        List<Array> sh0 = new List<Array> { };

                        value = rnd.Next(1, 4);
                        value = 2;

                        switch (value)
                        {
                            case 1:
                                sh0.Add(sh1);
                                break;
                            case 2:
                                sh0.Add(sh1);
                                sh0.Add(sh2);
                                break;
                            case 3:
                                sh0.Add(sh1);
                                sh0.Add(sh2);
                                sh0.Add(sh3);
                                break;

                        }


                        string[] kn1 = { "16", "knight1", "101", "1101", "31", "Knight soldier", "itsmeknight" };
                        string[] kn2 = { "17", "knight2", "102", "1102", "32", "Knight soldier", "itsmeknight" };
                        string[] kn3 = { "18", "knight3", "103", "1103", "33", "Knight soldier", "itsmeknight" };
                        List<Array> kn0 = new List<Array> { };

                        value = rnd.Next(1, 4);
                        value = 2;

                        switch (value)
                        {
                            case 1:
                                kn0.Add(kn1);
                                break;
                            case 2:
                                kn0.Add(kn1);
                                kn0.Add(kn2);
                                break;
                            case 3:
                                kn0.Add(kn1);
                                kn0.Add(kn2);
                                kn0.Add(kn3);
                                break;

                        }

                        string[] wz1 = { "19", "Wizard1", "101", "111", "21", "Wiz soldier", "itsmewiz" };
                        string[] wz2 = { "20", "Wizard2", "102", "112", "22", "Wiz soldier", "itsmewiz" };
                        string[] wz3 = { "21", "Wizard3", "103", "113", "23", "Wiz soldier", "itsmewiz" };
                        List<Array> wz0 = new List<Array> { };

                        value = rnd.Next(1, 4);
                        value = 2;

                        switch (value)
                        {
                            case 1:
                                wz0.Add(wz1);
                                break;
                            case 2:
                                wz0.Add(wz1);
                                wz0.Add(wz2);
                                break;
                            case 3:
                                wz0.Add(wz1);
                                wz0.Add(wz2);
                                wz0.Add(wz3);
                                break;

                        }

                        string[] mn1 = { "22", "mn1", "101", "111", "21", "Just monster", "mmmonster" };
                        string[] mn2 = { "23", "mn2", "102", "112", "22", "Just monster", "mmmonster" };
                        string[] mn3 = { "24", "mn3", "103", "113", "23", "Just monster", "mmmonster" };
                        List<Array> mn0 = new List<Array> { };

                        value = rnd.Next(1, 4);
                        value = 2;

                        switch (value)
                        {
                            case 1:
                                mn0.Add(mn1);
                                break;
                            case 2:
                                mn0.Add(mn1);
                                mn0.Add(mn2);
                                break;
                            case 3:
                                mn0.Add(mn1);
                                mn0.Add(mn2);
                                mn0.Add(mn3);
                                break;

                        }
                        g.store_green.Add(sh0);
                        g.store_green.Add(kn0);
                        g.store_green.Add(wz0);
                        g.store_green.Add(mn0);
                    }

                }
            }
        }
        public Name()
        {
            InitializeComponent();

            List<Button> buttons = new List<Button> { button1, button2, button3 };
            List<PictureBox> PictureBoxes = new List<PictureBox> {pictureBox1, pictureBox2, pictureBox3,
                pictureBox4, pictureBox5, pictureBox6, pictureBox7, pictureBox8, pictureBox9,
                pictureBox10, pictureBox11,pictureBox12,pictureBox13,pictureBox14,pictureBox15,
                pictureBox16,pictureBox17,pictureBox18,pictureBox19,pictureBox20,pictureBox21,
                pictureBox22,pictureBox23,pictureBox24,pictureBox25,pictureBox26};
            List<RichTextBox> RTBoxes = new List<RichTextBox> { richTextBox1, richTextBox2,
                richTextBox3, richTextBox4, richTextBox5, richTextBox6 };
            progressBar1.Visible = false;
            progressBar2.Visible = false;
            pictureBox27.Visible = false;
                
            f.init(); // АЛО ДЯДЯ КАК ТЫ ЗАБЫТЬ МОГ???????

            foreach (Button btn in buttons) { btn.Visible = false; }
            foreach (PictureBox Pb in PictureBoxes) { Pb.Visible = false; }
            foreach (RichTextBox Rtb in RTBoxes) { Rtb.Visible = false; }

            button1.Visible = true;
            button1.Text = "Начать";

        }

        private void button1_Click(object sender, EventArgs e)
        {
            button1.Visible = false;
            button2.Visible = true;

            List<PictureBox> PictureBoxes = new List<PictureBox> { pictureBox1, pictureBox8 };
            List<RichTextBox> RTBoxes = new List<RichTextBox> { richTextBox1, richTextBox2,
                richTextBox3, richTextBox4, richTextBox5, richTextBox6 };
            foreach (PictureBox Pb in PictureBoxes) { Pb.Visible = true; }
            foreach (RichTextBox Rtb in RTBoxes) { Rtb.Visible = true; }
            progressBar1.Visible = true;
            progressBar2.Visible = true;
            button2.Text = "Сгенерировать случайные войска";
        }


        private void button2_Click(object sender, EventArgs e)
        {
            button2.Visible = false;
            button3.Visible = true;
            button3.Text = "Начать сражение";
            richTextBox1.Text = Convert.ToString(f.GetHealth(g.store_purp));
            richTextBox2.Text = Convert.ToString(f.GetArmor(g.store_purp));
            richTextBox3.Text = Convert.ToString(f.GetDamage(g.store_purp));
            richTextBox4.Text = Convert.ToString(f.GetDamage(g.store_green));
            richTextBox5.Text = Convert.ToString(f.GetArmor(g.store_green));
            richTextBox6.Text = Convert.ToString(f.GetHealth(g.store_green));
            g.starthp_green = f.GetHealth(g.store_green);
            g.starthp_purp = f.GetHealth(g.store_purp);
            List<PictureBox> tmp_pboxes = new List<PictureBox>{pictureBox1, pictureBox2, pictureBox3,
                pictureBox4, pictureBox5, pictureBox6, pictureBox7, pictureBox8, pictureBox9,
                pictureBox10, pictureBox11,pictureBox12,pictureBox13,pictureBox14,pictureBox15,
                pictureBox16,pictureBox17,pictureBox18,pictureBox19,pictureBox20,pictureBox21,
                pictureBox22,pictureBox23,pictureBox24,pictureBox25,pictureBox26};
            f.CheckPictures(g.store_purp, g.store_green,tmp_pboxes);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            List<PictureBox> tmp_pboxes = new List<PictureBox>{pictureBox1, pictureBox2, pictureBox3,
                pictureBox4, pictureBox5, pictureBox6, pictureBox7, pictureBox8, pictureBox9,
                pictureBox10, pictureBox11,pictureBox12,pictureBox13,pictureBox14,pictureBox15,
                pictureBox16,pictureBox17,pictureBox18,pictureBox19,pictureBox20,pictureBox21,
                pictureBox22,pictureBox23,pictureBox24,pictureBox25,pictureBox26};
            f.CheckPictures(g.store_purp, g.store_green,tmp_pboxes);
            f.Attack(tmp_pboxes);
            int Health_purp = f.GetHealth(g.store_purp);
            int Health_green = f.GetHealth(g.store_green);
            richTextBox1.Text = Convert.ToString(Health_purp);
            richTextBox2.Text = Convert.ToString(f.GetArmor(g.store_purp));
            richTextBox3.Text = Convert.ToString(f.GetDamage(g.store_purp));
            richTextBox4.Text = Convert.ToString(f.GetDamage(g.store_green));
            richTextBox5.Text = Convert.ToString(f.GetArmor(g.store_green));
            richTextBox6.Text = Convert.ToString(Health_green);
            progressBar1.Value = (int)(100 * (double)Health_purp / g.starthp_purp);
            progressBar2.Value = (int)(100 * (double)Health_green / g.starthp_green);

            
            f.CheckPictures(g.store_purp, g.store_green,tmp_pboxes);


            if ((f.GetHealth(g.store_purp) == 0) || (f.GetHealth(g.store_green) == 0))
            {
                List<PictureBox> PictureBoxes = new List<PictureBox> { pictureBox1, pictureBox8 };
                List<RichTextBox> RTBoxes = new List<RichTextBox> { richTextBox1, richTextBox2,
                richTextBox3, richTextBox4, richTextBox5, richTextBox6 };
                foreach (PictureBox Pb in PictureBoxes) { Pb.Visible = false; }
                foreach (RichTextBox Rtb in RTBoxes) { Rtb.Visible = false; }
                progressBar1.Visible = false;
                progressBar2.Visible = false;
            }

            if (f.GetHealth(g.store_purp) == 0 && f.GetHealth(g.store_green) == 0)
            {
                button3.Visible = false;
                f.Victory("draw", tmp_pboxes, label1, pictureBox27);
            }
            else
            {


                if (f.GetHealth(g.store_purp) == 0)
                {
                    button3.Visible = false;
                    f.Victory("green", tmp_pboxes, label1, pictureBox27);
                }

                else
                {
                    if (f.GetHealth(g.store_green) == 0)
                    {
                        button3.Visible = false;
                        f.Victory("purp", tmp_pboxes, label1, pictureBox27);
                    }
                }
            }
        }
    }
}

﻿namespace PracticeConsole
{
    abstract class Unit : Base
    {
        public Armor armor;
        
        public Unit(string name, int armor, string armor_name, int hp, int damage) : base(name, hp, damage)
        {
            this.armor = new Armor(armor_name, armor);
        }
        public override string ToString()
        {
            string s = $"{name}\nБроня: {armor.name}\nЗащита: {armor.defense}\nЗдоровье: {hp}\nУрон: {damage}";
            return s;
        }
    }
}

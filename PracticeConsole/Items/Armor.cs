namespace PracticeConsole
{
    class Armor
    {
        public string name { get; }  // Можно было реализовать другую логику брони, где были бы классы:
        public int defense { get; }  // abstract BaseArmor -> ( GlassArmor | Leather Armor ), но решил всё же полегче сделать
        public Armor(string name, int defense)
        {
            this.name = name;
            this.defense = defense;
        }
    }
}

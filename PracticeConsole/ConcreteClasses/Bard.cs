namespace PracticeConsole
{
    class Bard : Unit
    {
        public Bard(string name, int armor, string armor_name, int hp, int damage) : base(name, armor, armor_name, hp, damage)
        {

        }
        public override void Attack()
        {
            /// <summary>
            /// Конкретная реализация нанесения урона Бардом по цели
            /// </summary>
        }
    }
}

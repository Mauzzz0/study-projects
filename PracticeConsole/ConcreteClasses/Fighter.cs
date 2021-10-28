namespace PracticeConsole
{
    class Fighter : Unit
    {
        public Fighter(string name, int armor, string armor_name, int hp, int damage) : base(name, armor, armor_name, hp, damage)
        {

        }
        public override void Attack()
        {
            /// <summary>
            /// Конкретная реализация нанесения урона Бойцом по цели
            /// </summary>
        }
    }
}

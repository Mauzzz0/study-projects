namespace PracticeConsole
{
    class Camel : Animal
    {
        public Camel(string name, int speed, int hp, int damage) : base(name, speed, hp, damage)
        {

        }
        public override void Attack()
        {
            /// <summary>
            /// Конкретная реализация нанесения урона Верблюдом по цели
            /// </summary>
        }
    }
}

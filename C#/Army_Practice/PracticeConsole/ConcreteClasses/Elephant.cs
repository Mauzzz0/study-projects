namespace PracticeConsole
{
    class Elephant : Animal
    {
        public Elephant(string name, int speed, int hp, int damage) : base(name,speed,hp,damage)
        {

        }
        public override void Attack()
        {
            /// <summary>
            /// Конкретная реализация нанесения урона Слоном по цели
            /// </summary>
        }
    }
}

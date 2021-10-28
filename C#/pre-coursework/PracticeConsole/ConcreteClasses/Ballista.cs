namespace PracticeConsole
{
    class Ballista : Mechanism
    {
       public Ballista(string name, string ammo_type, int ammo_count, int hp, int damage) : base(name, ammo_type, ammo_count, hp, damage)
       {

       }
        public override void Attack()
        {
            /// <summary>
            /// Конкретная реализация нанесения урона Баллистой по цели
            /// </summary>
        }
    }
}

namespace PracticeConsole
{
    abstract class Base
    {
        public string name { get; }
        public int hp { get; protected set; }
        public int damage { get; protected set; }
        public abstract void Attack(); // Необходимое по заданию умение атаковывать, которое не используется
        public void TakeDamage(int x) // Изменение ХП в отдельном методе, чтобы не открывать изменение ХП всей программе
        {
            hp -= x;
        }
        public abstract override string ToString();
        public Base(string name, int hp, int damage)
        {
            this.name = name;
            this.hp = hp;
            this.damage = damage;
        }
    }
}

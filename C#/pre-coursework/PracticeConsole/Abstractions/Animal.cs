namespace PracticeConsole
{
    abstract class Animal : Base
    {
        public int speed { get; }
        public Animal(string name, int speed, int hp, int damage) : base(name,hp, damage)
        {
            this.speed = speed;
        }
        public override string ToString()
        {
            string s = $"{name}\nСкорость: {speed}\nЗдоровье: {hp}\nУрон: {damage}";
            return s;
        }
    }
}

namespace PracticeConsole
{
    class Bullet
    {
        public string name { get; }
        public int count { get; }
        public int damage { get; protected set; }
        public Bullet(string name, int count, int damage)
        {
            this.name = name;
            this.count = count;
            this.damage = damage;
        }
        public void NotEnoughtBullets()
        {
            this.damage = 0;
        }
    }
}

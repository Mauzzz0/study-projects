namespace PracticeConsole
{
    abstract class Mechanism : Base
    {
        //string ammo_type; /// TODO: Патрон выделить в отдельный класс
        //int ammo_count; 
        Bullet bullet;
        public Mechanism(string name,string ammo_type, int ammo_count, int hp, int damage) : base(name,hp, damage)
        {
            this.bullet = new Bullet(ammo_type, ammo_count, damage);
            //this.ammo_type = ammo_type;
            //this.ammo_count = ammo_count;
            Refresh();
        }
        void Refresh()
        {
            if (bullet.count <= 0)
            {
                bullet.NotEnoughtBullets(); // 0 патронов => урон = 0
                base.damage = 0;
            }
        }
        public override string ToString()
        {
            string s = $"{name}\nБоеприпас: {bullet.name}\nПрипасы: {bullet.count}\nЗдоровье: {hp}\nУрон: {bullet.damage}";
            return s;
        }
    }
}

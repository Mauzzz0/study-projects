namespace PracticeConsole
{
    abstract class Rider : Base // САМЫЙ УЖАСНЫЙ КЛАСС
    {
        new string name;
        public int armor { get; }
        new public int hp { get; }
        Animal animal; // Нарушение принципа инверсии зависимостей,
        Unit unit;     // фикс выйдет громоздким

        public Rider(string name, int hp, int damage, string uname, int uarmor, string uarmor_name, int uhp, int udamage, string aname, int aspeed, int ahp, int adamage)
            : base(name,hp,damage) // ":base(..)" - костыль, чтобы всадник поместить в один список со всей армией
        {                          // hp,damage - неиспользуемые переменные
            this.name = name;
            animal = new Camel(aname, aspeed, ahp, adamage);
            unit = new Bard(uname, uarmor, uarmor_name, uhp, udamage);
            base.damage = animal.damage + unit.damage; // До конца не смог понять почему нужно использовать "base.", но
            base.hp = animal.hp + unit.hp;             // с "this.hp" выдаёт неверные данные
            armor = uarmor;
        }
        public override string ToString()
        {
            string s = $"{name}\nВсадник: {unit.name}\nЖивотное: {animal.name}\nЗдоровье: {base.hp}\nУрон: {damage}\nЗащита: {armor}\nСкорость: {animal.speed}";
            return s;
        }
    }
}

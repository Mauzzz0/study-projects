namespace PracticeConsole
{
    class Rider1 : Rider
    { // "Rider1" - конкретный класс, "Rider" - абстракция. 
        public Rider1(string name, int hp, int damage, string uname, int uarmor, string uarmor_name, int uhp, int udamage, string aname, int aspeed, int ahp, int adamage)
            : base(name, hp, damage, uname,uarmor,uarmor_name,uhp,udamage,aname,aspeed,ahp,adamage)
        {

        }
        public override void Attack()
        {
            /// <summary>
            /// Конкретная реализация нанесения урона Всадником по цели
            /// </summary>
        }
    }
}

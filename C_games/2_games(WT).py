import random
class makeCH() :
    def __init__(self) :
        self.hp = random.randrange(150, 200)
        self.ammo = random.randrange(10, 50)
        self.crew = random.randrange(3,10)
    def HE(self) :
        return self.hp * 0.04
    def AP(self) :
        return self.hp * 0.06
    def repair(self) :
        return self.hp * 0.05
atAP = 0
atHE = 0
a = makeCH()
print('A tank hp : {}   , ammo {}, crew {}   '.format(a.hp, a.ammo, a.crew))
b = makeCH()
print('B tank hp : {}   , ammo {}, crew {}   '.format(b.hp, b.ammo, a.crew))

while not b.hp <= 0 or a.hp <= 0 :
    print('a = 공격, f = 수리 r = 재보급')
    print('A tank hp : {}   , ammo {}, crew {}   '.format(a.hp, a.ammo, a.crew))
    chat = input()
    if chat == 'a' :
        print('He = h AP = a')
        shall = input()
        if shall == 'a' :
            atAP = random.randrange(2)
        if shall == 'h' :
            atHE = 1
    if atHE == 1 :
        b.hp = b.hp - a.HE()
        a.ammo = a.ammo - 1
        print("after b tank hp : {}  ".format(b.hp))
        atAP = 3
    if atAP  == 1 :
        b.hp = b.hp - a.AP()
        a.ammo = a.ammo - 1
        print("after b tank hp : {}  ".format(b.hp))
    if chat == 'f' :
        if not a.crew == 0 :
            a.hp = a.hp + a.repair()
            a.crew = a.crew - 1
        atAP = 3
        atHE = 3
        print('A tank hp : {}  '.format(a.hp))
    if atAP == 0 :
        print("적 공격 도탄")
    if chat == 'r' :
        a.ammo = a.ammo + 1
        a.crew = a.crew + 1
        atAP =  3
        atHE = 3
    v = random.randrange(2)
    if v == 1 :
        if not b.ammo == 0 :
            a.hp = a.hp - b.AP()
            b.ammo = b.ammo - 1
            print('A tank hp : {} '.format(a.hp))
        elif b.ammo == 0 :
            b.ammo = b.ammo + random.randrange(1, 4)
            b.crew = b.crew + 2
    if v == 0 :
        print("(도탄되는 소리)")

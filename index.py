
import json
import random
from classes.jatekosunk import Jatekos


def kockadobas():
    return random.randint(1, 6)


def duplakockadobas():
    return random.randint(1, 6) + random.randint(1, 6)


def szerencseproba():
    if Jatekos.Elixir:
        if duplakockadobas()+1 <= Jatekos.Luck:
            Jatekos.minuszluck(1)
            print("Szerencsés voltál!")
            return True
        else:
            Jatekos.minuszluck(1)
            print("Nem volt szerencséd most!")
            return False
    else:
        if duplakockadobas() <= Jatekos.Luck:
            Jatekos.minuszluck(1)
            print("Szerencséd volt!")
            return True
        else:
            Jatekos.minuszluck(1)
            print("Nem volt szerencséd most")
            return False


def igenvagynem():
    print("igen vagy nem?")
    while True:
        inp = input()
        if inp == "igen":
            return True
        elif inp == "nem":
            return False
        else:
            print("Ilyen lehetőség nincsen,helyes szót írj be!!")

def harc(csatamod, name, hp, skill):
    while True:
        EllensegAttackSTR = duplakockadobas() + skill  # 1.lépés a játékunkban 
        JatekosAttackSTR = duplakockadobas() + Jatekos.Skill  # 2.lépés a játékunkban
        if Jatekos.combatblessed:
            JatekosAttackSTR = JatekosAttackSTR + 1
        if csatamod > 0:
            JatekosAttackSTR = JatekosAttackSTR - csatamod

        if EllensegAttackSTR < JatekosAttackSTR:
            hp = hp - 2
            print("Megsebezted a méltó ellenfeled!")
            if Jatekos.HP < 1:
                print("Vesztettél sajnos!")
                Jatekos.gameover()
                return False
            elif hp < 1:
                print("!")
                return True
            print("Akarsz szerencsét próbálni azonnal?")
            if not igenvagynem():
                print("Gyáva vagy és nem próbálsz szerencsét!")
            else:
                if szerencseproba():
                    print("Merész vagy és súlyos sebet ejtettél!")
                    hp = hp - 2
                else:
                    print("A seb puszta karcolás!")
                    hp = hp + 1
        elif EllensegAttackSTR > JatekosAttackSTR:
            Jatekos.jatekosSebzes(2)
            print("Az ellenfél megsebzett téged!")
            if Jatekos.HP < 1:
                print("Nem nyertél!")
                Jatekos.gameover()
                return False
            elif hp < 1:
                print("Nyertél!")
                return True
            print("Akarsz szerencsét próbálni azonnal?")
            if not igenvagynem():
                print("Gyáva vagy és nem próbálsz szerencsét!")
            else:
                if not szerencseproba():
                    print("Súlyos sebzést Kaptál!")
                    Jatekos.jatekosSebzes(2)
                else:
                    print("A seb puszta karcolás!")
                    Jatekos.jatekosHeal(1)
        else:
            print("Kivédtétek egymás ütését!")
        print(f"{name} Életereje: {hp}")
        print(f"Játékos Életereje: {Jatekos.HP} \n")



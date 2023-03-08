
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

Nyert = False
probaltemar = False
fellvettekopenyt = False
csatamod = 0
input("Új játék inditásához írj be bármit és nyomd meg az entert: ")

Jatekos = Jatekos(duplakockadobas() + 12, kockadobas() + 6, kockadobas() + 6, 20)  # HP Luck Skill Gold

with open("Kaland.json", "r", encoding="utf-8") as jsn:
    advDict = json.load(jsn)

while not Nyert:
    LepettEMar = False
    Jatekos.lokaciostr()
    print(advDict['kaland'][Jatekos.lokacio]['szoveg'] + "\n")

    # stat váltosztatások
    if "eleterovesztes" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.jatekosSebzes(advDict['kaland'][Jatekos.lokacio]['ertek'])
    if "hplossrng" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.jatekosSebzes(kockadobas())
    if "szerencsevesztes" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.minuszluck(advDict['kaland'][Jatekos.lokacio]['ertek'])
    if "Eleteronyeres" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.jatekosHeal(advDict['kaland'][Jatekos.lokacio]['ertek'])
    if "szerencsenyeres" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszluck(advDict['kaland'][Jatekos.lokacio]['ertek'])
    if "luckblessing" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.JatekosBlessing()
    if "combatblessing" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.JatekosCombatBlessing()
    if "kezdetiszerencsenoveles" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.kezdetiszerencsenoveles(advDict['kaland'][Jatekos.lokacio]['ertek'])
    if "szerencse+hpminusz" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.minuszluck(advDict['kaland'][Jatekos.lokacio]['ertek'][0])
        Jatekos.jatekosSebzes(advDict['kaland'][Jatekos.lokacio]['ertek'][1])
    if "elixir" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.SzerencseElixirf()
    if "tortenetkezdes" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.tortenetkezdes()

    # tárgy felvételek
    if "pluszlebeges" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszitem("Lebegés Köpenye")
    if "pluszgyuru" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszitem("Ügyesség Gyürüje")
    if "pluszarany" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszitem("Aranykulcs")

    if "+penz" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszpenz(int(advDict['kaland'][Jatekos.lokacio]['mennyiseg'][0]))

    if "+kristaly" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        Jatekos.pluszcrystal(advDict['kaland'][Jatekos.lokacio]['targy'])
    # harc
    if "csatamod" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        csatamod = int(advDict['kaland'][Jatekos.lokacio]['ertek'][0])

    if "onharc" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        if advDict['kaland'][Jatekos.lokacio]['ellenfelek'] == 1:
            harc(csatamod, "te", Jatekos.HP, Jatekos.Skill)
            csatamod = 0

    if "harc" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        if advDict['kaland'][Jatekos.lokacio]['ellenfelek'] == 1:
            harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel']['nev'],
                 advDict['kaland'][Jatekos.lokacio]['ellenfel']['HP'],
                 advDict['kaland'][Jatekos.lokacio]['ellenfel']['ugyesseg'])
            csatamod = 0
        elif advDict['kaland'][Jatekos.lokacio]['ellenfelek'] == 2:
            if harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel']['nev'],
                    advDict['kaland'][Jatekos.lokacio]['ellenfel']['HP'],
                    advDict['kaland'][Jatekos.lokacio]['ellenfel']['ugyesseg']):
                csatamod = 0
                harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel2']['nev'],
                     advDict['kaland'][Jatekos.lokacio]['ellenfel2']['HP'],
                     advDict['kaland'][Jatekos.lokacio]['ellenfel2']['ugyesseg'])
        elif advDict['kaland'][Jatekos.lokacio]['ellenfelek'] == 3:
            if harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel']['nev'],
                    advDict['kaland'][Jatekos.lokacio]['ellenfel']['HP'],
                    advDict['kaland'][Jatekos.lokacio]['ellenfel']['ugyesseg']):
                csatamod = 0
                if harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel2']['nev'],
                        advDict['kaland'][Jatekos.lokacio]['ellenfel2']['HP'],
                        advDict['kaland'][Jatekos.lokacio]['ellenfel2']['ugyesseg']):
                    harc(csatamod, advDict['kaland'][Jatekos.lokacio]['ellenfel3']['nev'],
                         advDict['kaland'][Jatekos.lokacio]['ellenfel3']['HP'],
                         advDict['kaland'][Jatekos.lokacio]['ellenfel3']['ugyesseg'])


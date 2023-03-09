
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
            print("Nincs ilyen lehetőség, írd be a megfelelő szót!")

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
            print("Megsebesítetted tiszteletreméltó ellenfeledet!")
            if Jatekos.HP < 1:
                print("Vesztettél sajnos!")
                Jatekos.gameover()
                return False
            elif hp < 1:
                print("!")
                return True
            print("Szeretnél azonnal szerencsét próbálni?")
            if not igenvagynem():
                print("Gyáva vagy és nem próbálsz szerencsét!")
            else:
                if szerencseproba():
                    print("Merész vagy és súlyosan megsérült az ellenség!")
                    hp = hp - 2
                else:
                    print("A seb csak egy kaparás!")
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
                print("Gyáva vagy, ne kockáztass!")
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
input("Új játék indításához írjon be bármit, és nyomja meg az Enter billentyűt: ")

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

    # item felvetel
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
    # fight
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
    if Jatekos.halott:
        break

    # win/lose detektor
    if advDict['kaland'][Jatekos.lokacio]['akcio'] == "gyozelem":
        Nyert = True
        break
    elif advDict['kaland'][Jatekos.lokacio]['akcio'] == "gameover":
        Nyert = False
        Jatekos.gameover()
        break

    # lepesek
    if "rollllll" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        while True:
            if kockadobas()>4:
                LepettEMar = True
                break
            else:
                Jatekos.jatekosSebzes(2)
    if "kisebbnagyonbb" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        if duplakockadobas() > Jatekos.Skill:
            Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['ugras'][0])
            LepettEMar = True
        else:
            Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['ugras'][1])
            LepettEMar = True
    if "szerencseproba" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        if szerencseproba():
            Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['HaVan'])
            LepettEMar = True
    if not probaltemar:
        if "gyuruproba" in advDict['kaland'][Jatekos.lokacio]['akcio']:
            print("Szeretnéd felprobálni a gyűrűt?")
            if igenvagynem():
                Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['haszeretne'])
                LepettEMar = True
                probaltemar = True
    if not fellvettekopenyt:
        if "kopeny" in advDict['kaland'][Jatekos.lokacio]['akcio']:
            print("Szeretnéd felprobálni a köpenyt?")
            if igenvagynem():
                Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['haszeretnekopenyt'])
                LepettEMar = True
                fellvettekopenyt = True
    if "targy" in advDict['kaland'][Jatekos.lokacio]['akcio']:
        if (advDict['kaland'][Jatekos.lokacio]['TargyInfo']['szukseges']) in Jatekos.Items:
            Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['TargyInfo']['HaVan'])
            LepettEMar = True
    if not LepettEMar:
        if len(advDict['kaland'][Jatekos.lokacio]['ugras']) == 1:
            StartInp = input("Az instrukció szerint lehet folytatni a programot, amennyiben megnyomják az Enter gombot, vagy beírják egy parancsot a további műveletek elvégzéséhez.[statok, kilepes]: ")
            if StartInp == "statok":
                print(Jatekos)
                print("")
            elif StartInp == "kilepes":
                exit()
            Jatekos.lokaciovaltoztatas(advDict['kaland'][Jatekos.lokacio]['ugras'][0])
        elif len(advDict['kaland'][Jatekos.lokacio]['ugras']) > 1:
            print("Irja be merre szeretne haladni vagy irjon be egy commandot [statok, kilepes]?")
            while True:
                inp = input()
                if not inp == "":
                    if inp in str(advDict['kaland'][Jatekos.lokacio]['ugras']):
                        Jatekos.lokaciovaltoztatas(inp)
                        break
                    elif inp == "statok":
                        print(Jatekos)
                        print("")
                    elif inp == "kilepes":
                        exit()
                    else:
                        print("Ilyen opció nincsen")
                else:
                    print("Ilyen opció nincsen")

if not Nyert:
    print("Nem nyertél!")
elif Nyert:
    print("Gratulálunk megnyerted a játékot!")


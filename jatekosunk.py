class Jatekos:
    def __init__(self, HP, Luck, Skill, Gold, Items=None, Crystals=None, Potions=None, Food=None, lokacio="0",
                 blessed=False, combatblessed=False, Halott=False, Elixir=False):
        if Food is None:
            Food = []
        if Potions is None:
            Potions = []
        if Crystals is None:
            Crystals = []
        if Items is None:
            Items = []
        self.HP = HP
        self.Luck = Luck
        self.Skill = Skill
        self.Gold = Gold
        self.Items = Items
        self.Crystals = Crystals
        self.Potions = Potions
        self.Food = Food
        self.lokacio = lokacio
        self.kezdetiHP = HP
        self.kezdetiLuck = Luck
        self.kezdetiSkill = Skill
        self.blessed = blessed
        self.combatblessed = combatblessed
        self.halott = Halott
        self.Elixir = Elixir

    def tortenetkezdes(self):
        self.Items.append("Kard")
        self.Items.append("Bőrvért")

    def kezdetiszerencsenoveles(self, ertek):
        self.kezdetiLuck = self.kezdetiLuck + ertek
        self.Luck = self.kezdetiLuck

    def minuszluck(self, ertek):
        if self.blessed:
            if 6 > self.Luck - ertek:
                self.Luck = 6
        else:
            self.Luck = self.Luck - ertek

    def pluszluck(self, ertek):
        if self.Luck + ertek > self.kezdetiLuck:
            self.Luck = self.kezdetiLuck
        else:
            self.Luck = self.Luck + ertek

    def jatekosSebzes(self, szam):
        self.HP = self.HP - szam

    def jatekosHeal(self, szam):
        if self.HP + szam > self.kezdetiHP:
            self.HP = self.kezdetiHP
        else:
            self.HP = self.HP + szam

    def lokaciovaltoztatas(self, szoba):
        self.lokacio = szoba

    def gameover(self):
        self.HP = 0
        self.Items.clear()
        self.Potions.clear()
        self.Crystals.clear()
        self.halott = True

    def pluszitem(self, inp):
        self.Items.append(inp)

    def pluszpenz(self, inp):
        self.Gold = self.Gold + inp

    def pluszcrystal(self, inp):
        self.Crystals.append(inp)

    def JatekosBlessing(self):
        self.blessed = True

    def JatekosCombatBlessing(self):
        self.combatblessed = True

    def SzerencseElixirf(self):
        self.Elixir = True

    def lokaciostr(self):
        self.lokacio = str(self.lokacio)

    def __repr__(self):
        return f'Életerőd: {self.HP}\nSzerencséd: {self.Luck}\nÜgyeséged: {self.Skill}\nHelyzeted: {self.lokacio}\nPénzed: {self.Gold}\nTárgyaid: {self.Items}\nKristályaid: {self.Crystals}\nItalaid: {self.Potions}\nÉteleid: {self.Food}'
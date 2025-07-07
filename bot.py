from robot import Robot  # importujeme třídu Robot ze souboru robot.py

class Bot(Robot):
    # pass  # zatím nic nepřidáváme, Bot dědí vše z Robot

    # Přídáno pouze z důvodu přidání dalšího atributu, jinak by se vše dědilo s robota a nic by se nic nepsalo
    # Přepsat konstruktor (__init__) v Bot
    def __init__(self, nazev, baterie, delka_rukou, zbrane, barva, stit_aktivni=False):
        # Zavolat konstruktor rodiče (super().__init__()), abys zachoval původní vlastnosti
        super().__init__(nazev, baterie, delka_rukou)
        self.zbrane = zbrane  # nový atribut
        self.barva = barva  # nový atribut
        self.stit_aktivni = stit_aktivni # nová metoda

    def krok_vpred(self):
        print(f"Bot {self.nazev} kráčí kupředu")
        if not self.stit_aktivni:
            self.ukony_do_kontroly -= 1
        else:
            print("Štít je aktivní – úkon se nezapočítává.")
        print(f"Zbývá {self.ukony_do_kontroly} úkonů do kontroly")

    def krok_vzad(self):
        print(f"Bot {self.nazev} udělal krok vzad")
        self.ukony_do_kontroly += 10
        print(f"Zbývá {self.ukony_do_kontroly} do zničení ")

    # Přidání nové metody
    def zapni_stit(self):
        self.stit_aktivni = True
        self.ukony_do_kontroly -= 1
        print(f"{self.nazev} aktivoval štít!")
        print(f"Zbývá {self.ukony_do_kontroly} do zničení ")

    # Přidání nové metody
    def vypni_stit(self):
        self.stit_aktivni = False
        self.ukony_do_kontroly -= 1
        print(f"{self.nazev} deaktivoval štít!")
        print(f"Zbývá {self.ukony_do_kontroly} do zničení ")

    # přidání zbraně do výpisu
    def vypis(self):
        super().vypis()
        print(f"Výzbroj: {self.zbrane}")
        print(f"\033[31;43mVýzbroj: {self.zbrane}\033[0m")
        print(f"Barva: {self.barva}")
        # Výpis (přidání) nové metody - zapni_stit
        print(f"Štít aktivní: {self.stit_aktivni}")
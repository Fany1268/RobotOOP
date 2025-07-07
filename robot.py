class Robot:
    # constructor
    def __init__(self, nazev, baterie, delka_rukou):
        self.nazev = nazev
        self.baterie = baterie
        self.delka_rukou = delka_rukou
        #zadání defoultní hodnoty
        self.ukony_do_kontroly = 1000

    def krok_vpred(self):
        print(f"\033[32mRobot {self.nazev} udělal krok vpřed \033[0m")
        #self.ukony_do_kontroly = self.ukony_do_kontroly - 1
        #zkrácený zápis
        self.ukony_do_kontroly -= 1
        # print(f"Zbývá {robot_1.ukony_do_kontroly} úkonú do kontroly")
        #objektový zápis
        print(f"Zbývá {self.ukony_do_kontroly} úkonů do kontroly")

    def krok_vzad(self):
        if self.ukony_do_kontroly > 998:
            print(f"\033[31mRobot {self.nazev} udělal krok vzad\033[0m")
            self.ukony_do_kontroly -= 1
            print(f"Zbývá {self.ukony_do_kontroly} úkonů do kontroly")
        else:
             print(f"\033[30;41m" + f"Robot {self.nazev} is destroy" + "\033[0m")



    def vypis(self):
        print(self.nazev)
        print(self.baterie)
        print(self.delka_rukou)
        print(self.ukony_do_kontroly)












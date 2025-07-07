from robot import Robot
from bot import Bot
import sys
from dual_output import DualOutput



# Cesty, kam chceš ukládat výstup (můžeš si je měnit)
cesty = [
    r"C:\Users\Domča\Downloads\vystup.txt",
    r"C:\Users\Domča\Documents\vystup.txt",
    r"C:\Users\Domča\Desktop\Táta projekty\programování\PycharmProjects\RobotOOP\vystup.txt"
]

# Otevření všech souborů najednou
soubory = [open(cesta, "w", encoding="utf-8") for cesta in cesty]
# Přidáme konzoli do seznamu výstupů
vystupy = [sys.stdout] + soubory
# Přesměrování výstupu do konzole i do všech souborů
sys.stdout = DualOutput(*vystupy)



# Tvoříme objekty podle classy
robot_1 = Robot("robot_1", 24, 0.6)
robot_2 = Robot("robot_2", 48, 0.5)
robot_3 = Robot("robot_3", 50, 0.6)
robot_4 = Robot("robot_4", 38, 0.4)

bot_1 = Bot("bot_1", 24, 0.8, "plazmový kanón", "bílá")

print("Tisknu do konzole i do všech souborů zároveň...")

robot_4.krok_vpred()
robot_3.krok_vzad()
# robot_3.krok_vzad()
# robot_3.krok_vzad()
# robot_3.krok_vzad()
# robot_3.krok_vzad()
# robot_3.krok_vzad()
# bot_1.zapni_stit()
bot_1.krok_vzad()
# bot_1.krok_vpred()
# bot_1.krok_vpred()
# bot_1.vypni_stit()





moji_roboti = [robot_1, robot_3, bot_1]
for robot in moji_roboti:
    robot.vypis()
    print()  # print() bez argumentů vytvoří prázdný řádek v konzoli a v souboru mezi roboty.



# Po skončení výpisu zavřeme všechny otevřené soubory
for f in soubory:
    f.close()

# Vrátíme výstup zpět na konzoli (standardní výstup)
sys.stdout = sys.__stdout__

print("Výpis byl uložen do souborů i vidět v konzoli.")

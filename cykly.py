print("Řádek 1\nŘádek 2")
print("Sloupec A\tSloupec B")

for i in range(10,-1,-1,):
    print(i, end=" \n")
for i in range(0,11,1,):
    print(i, end=" ")
for i in range(11):
    print(i,end=" \t")
for i in range(11, 1, -2):
    print(i,end=" \n")

    print()

    # stejný úkol
for i in range(1, 6):
    print(i)

i = 1
while i <= 5:
    print(i)
    i += 1


# barvy = ["červená", "zelená", "modrá"]
# for i in range(6):
#     print(barvy[i % 3])
'''
-len(seznam) vrátí počet prvků v seznamu.
- i % len(seznam) zajistí, že index bude vždy v rozmezí od 0 do len(seznam)-1.
- Tím pádem nikdy nezpůsobíš chybu IndexError, protože index nikdy nepřesáhne platný rozsah.
'''
barvy = ["červená", "zelená", "modrá"]
for i in range(5):
    print(barvy[i % len(barvy)])

hraci = ["Alice", "Bob", "Charlie"]
for tah in range(5):
    print(f"Táhne hráč: {hraci[tah % len(hraci)]}")



heslo = ""
while heslo != "tajne":
    heslo = input("Zadej heslo: ")
print("Správné heslo!")


spravne_heslo = "tajne"
zadane_heslo = ""

while zadane_heslo != spravne_heslo:
    zadane_heslo = input("Zadej heslo: ")
    if zadane_heslo != spravne_heslo:
        print("❌ Nesprávné heslo!")

print("✅ Správné heslo!")

